#!/usr/bin/env python3
import json
import logging
import os
import subprocess
import urllib.parse
import yt_dlp
import requests

# Configure logging with timestamps
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

PLAYLISTS = [
    "https://www.youtube.com/playlist?list=PL2yQDdvlhXf9gdFFBcDPUHAJS7kkIkIet",
    "https://www.youtube.com/playlist?list=PL2yQDdvlhXf9iyxIQQf-E4tXlGI0Fr_P7",
    "https://www.youtube.com/playlist?list=PL2yQDdvlhXf9Eey6tKOH0K4adBz-VF83G",
    "https://www.youtube.com/playlist?list=PL2yQDdvlhXf9Ypc5vLyhoJObwzMc98K8R"
]

# Individual videos to process (add individual YouTube video URLs here)
INDIVIDUAL_VIDEOS = [
    "https://www.youtube.com/watch?v=3Y1G9najGiI",
    "https://www.youtube.com/watch?v=JeUpUK0nhC0",
    "https://www.youtube.com/watch?v=JVj-r7B0gOU",
    "https://www.youtube.com/watch?v=prVdCIHlipg",
    "https://www.youtube.com/watch?v=q3Sb9PemsSo"
]

CATALOG_API = "https://catalog.awsevents.com/api/search"
OUTPUT_DIR = "sessions"

def clean_kiro_output(text):
    """Remove Kiro CLI UI elements from output"""
    import re
    # Remove ANSI escape codes
    text = re.sub(r'\x1b\[[0-9;]*m', '', text)
    # Remove Kiro prompt markers
    text = re.sub(r'^>\s*', '', text, flags=re.MULTILINE)
    # Remove credits/time info
    text = re.sub(r'▸ Credits:.*', '', text)
    return text.strip()

def translate_text(text):
    """Translate text using Kiro CLI"""
    result = subprocess.run(
        ["kiro-cli", "chat", "--no-interactive", "--agent=translator"],
        input=text,
        capture_output=True,
        text=True,
        timeout=300
    )
    return clean_kiro_output(result.stdout)

def search_session(title):
    """Search AWS Events catalog for session details"""
    import re

    # Extract session code from title (e.g., "CNS205", "AIM107-S" from "...title (CNS205)")
    # Handles: standard format (CNS205), with suffix (AIM107-S), formatting variations
    # Returns None for sessions without codes (like keynotes)
    session_code_match = re.search(r'\(([A-Z]{3}\d{3,4}(?:-[A-Z]+)?)\)|[- ]([A-Z]{3}\d{3,4}(?:-[A-Z]+)?)(?:\s|$)', title)
    expected_code = None
    if session_code_match:
        expected_code = session_code_match.group(1) or session_code_match.group(2)

    payload = f"search={urllib.parse.quote(title)}&type=session&browserTimezone=Asia%2FShanghai&catalogDisplay=list"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "origin": "https://registration.awsevents.com",
        "referer": "https://registration.awsevents.com/",
        "rfapiprofileid": "wxvHRIp7KuBcYrKpvzg4XTLENwBhrsvl",
        "rfwidgetid": "mEfLbtbGGZ3nYtnoTlf7AvZZXoAYU6Ny"
    }
    response = requests.post(CATALOG_API, data=payload, headers=headers)
    data = response.json()

    if data.get("responseCode") == "0" and data.get("sections"):
        items = data["sectionList"][0].get("items", [])

        # If we extracted a session code from the title, try to find exact match
        if expected_code and items:
            for item in items:
                if item.get("code") == expected_code:
                    logger.info(f"  ✓ Matched session code: {expected_code}")
                    return item

            # Fallback: If code doesn't already have a suffix, try adding "-S"
            if not re.search(r'-[A-Z]+$', expected_code):
                fallback_code = f"{expected_code}-S"
                logger.info(f"  ⚠ Session code {expected_code} not found, trying {fallback_code}...")

                # Search again with the -S suffix
                fallback_title = title.replace(expected_code, fallback_code)
                fallback_payload = f"search={urllib.parse.quote(fallback_title)}&type=session&browserTimezone=Asia%2FShanghai&catalogDisplay=list"
                fallback_response = requests.post(CATALOG_API, data=fallback_payload, headers=headers)
                fallback_data = fallback_response.json()

                if fallback_data.get("responseCode") == "0" and fallback_data.get("sections"):
                    fallback_items = fallback_data["sectionList"][0].get("items", [])
                    for item in fallback_items:
                        if item.get("code") == fallback_code:
                            logger.info(f"  ✓ Matched fallback session code: {fallback_code}")
                            return item

                logger.warning(f"  ⚠ Fallback code {fallback_code} not found either, using first result from original search")
            else:
                logger.warning(f"  ⚠ Session code {expected_code} not found in results, using first result")

        return items[0] if items else None
    return None

def get_video_info(video_url):
    """Fetch video info including duration"""
    ydl_opts = {
        'skip_download': True,
        'quiet': True,
        'cookiefile': 'cookies.txt'
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=False)
            return {
                'duration': info.get('duration', 0),
                'duration_minutes': info.get('duration', 0) / 60
            }
    except Exception as e:
        logger.error(f"    Error fetching video info: {e}")
        return None

def get_subtitles(video_url, output_path=None):
    """Fetch subtitles from YouTube video and optionally save to file"""
    import tempfile
    import glob
    import shutil

    with tempfile.TemporaryDirectory() as tmpdir:
        ydl_opts = {
            'skip_download': True,
            'writesubtitles': True,
            'writeautomaticsub': False,
            'subtitleslangs': ['en.*'],
            'subtitlesformat': 'srt',
            'quiet': True,
            'noprogress': True,
            'cookiefile': 'cookies.txt',
            'outtmpl': f'{tmpdir}/subtitle'
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])

            # Find the downloaded subtitle file
            srt_files = glob.glob(f'{tmpdir}/*.srt')
            if srt_files:
                with open(srt_files[0], 'r', encoding='utf-8') as f:
                    content = f.read()

                # Save to output path if provided
                if output_path:
                    with open(output_path, 'w', encoding='utf-8') as f:
                        f.write(content)

                return content

        except Exception as e:
            logger.error(f"    Error fetching subtitles: {e}")

    return None

def generate_summary(subtitles, duration_minutes=None):
    """Generate summary using Kiro CLI"""
    # Clean srt format - remove timestamps and metadata, keep only text
    import re
    lines = subtitles.split('\n')
    text_lines = []
    for line in lines:
        line = line.strip()
        # Skip srt headers, timestamps, and empty lines
        if line and not line.startswith('WEBsrt') and not '-->' in line and not line.isdigit():
            # Remove srt tags like <c>
            line = re.sub(r'<[^>]+>', '', line)
            text_lines.append(line)

    clean_text = ' '.join(text_lines)

    # Limit to ~100K characters to avoid context overflow
    if len(clean_text) > 100000:
        clean_text = clean_text[:100000] + '...'

    # Build prompt with duration info if available
    duration_info = ""
    if duration_minutes:
        duration_info = f"\n\nVideo Duration: {duration_minutes:.1f} minutes (ensure timeline does not exceed this duration)"

    prompt = f"Please summarize this AWS session based on the following subtitles:{duration_info}\n\n{clean_text}"
    result = subprocess.run(
        ["kiro-cli", "chat", "--no-interactive", "--agent=summarizer"],
        input=prompt,
        capture_output=True,
        text=True,
        timeout=600
    )
    return clean_kiro_output(result.stdout)

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Get playlist videos
    ydl_opts = {
        'extract_flat': True,
        'quiet': True,
        'cookiefile': 'cookies.txt'
    }

    all_videos = []

    # Fetch videos from playlists
    for playlist_url in PLAYLISTS:
        logger.info(f"Fetching playlist: {playlist_url}")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            playlist_info = ydl.extract_info(playlist_url, download=False)
            videos = playlist_info['entries']
            all_videos.extend(videos)
            logger.info(f"  Found {len(videos)} videos")

    # Fetch individual videos
    if INDIVIDUAL_VIDEOS:
        logger.info(f"Fetching {len(INDIVIDUAL_VIDEOS)} individual videos...")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            for video_url in INDIVIDUAL_VIDEOS:
                try:
                    video_info = ydl.extract_info(video_url, download=False)
                    all_videos.append(video_info)
                    logger.info(f"  Added: {video_info.get('title', 'Unknown')}")
                except Exception as e:
                    logger.error(f"  Error fetching {video_url}: {e}")

    logger.info(f"Processing {len(all_videos)} total videos...")

    for video in all_videos:
        try:
            video_url = f"https://www.youtube.com/watch?v={video['id']}"
            title = video['title']
            logger.info(f"Processing: {title}")

            # Search catalog
            session_data = search_session(title)
            if not session_data:
                logger.warning(f"  ⚠ No catalog data found for: {title}")
                continue

            session_code = session_data.get("code", "UNKNOWN")
            session_dir = os.path.join(OUTPUT_DIR, session_code)

            # Skip if session already exists
            if os.path.exists(os.path.join(session_dir, "metadata.json")):
                logger.info(f"  ⏭ Skipping {session_code} (already exists)")
                continue

            os.makedirs(session_dir, exist_ok=True)

            # Translate title and abstract
            logger.info(f"  Translating...")
            title_cn = translate_text(title)
            abstract = session_data.get("abstract", "")
            abstract_cn = translate_text(abstract) if abstract else ""

            # Extract speakers
            speakers = []
            for participant in session_data.get("participants", []):
                speakers.append({
                    "name": participant.get("fullName", ""),
                    "title": participant.get("jobTitle", ""),
                    "company": participant.get("companyName", "")
                })

            # Extract attributes from attributevalues
            topic = ""
            services = []
            area_of_interest = []

            for attr in session_data.get("attributevalues", []):
                attr_id = attr.get("attribute_id", "")
                value = attr.get("value", "")

                if attr_id == "Topic":
                    topic = value
                elif attr_id == "Services":
                    services.append(value)
                elif attr_id == "AreaofInterest":
                    area_of_interest.append(value)

            # Get video info (duration)
            logger.info(f"  Fetching video info...")
            video_info = get_video_info(video_url)
            duration_minutes = video_info['duration_minutes'] if video_info else None

            # Create metadata
            metadata = {
                "title": title,
                "title_cn": title_cn,
                "abstract": abstract,
                "abstract_cn": abstract_cn,
                "presenter": speakers,
                "attributes": {
                    "topic": topic,
                    "area_of_interest": area_of_interest,
                    "services": services,
                    "type": session_data.get("type", "")
                },
                "video_url": video_url,
                "session_code": session_code,
                "duration_seconds": video_info['duration'] if video_info else None,
                "duration_minutes": round(duration_minutes, 1) if duration_minutes else None
            }

            with open(os.path.join(session_dir, "metadata.json"), "w", encoding="utf-8") as f:
                json.dump(metadata, f, ensure_ascii=False, indent=2)

            # Get subtitles and generate summary
            logger.info(f"  Fetching subtitles...")
            subtitle_path = os.path.join(session_dir, "subtitles.srt")
            subtitles = get_subtitles(video_url, output_path=subtitle_path)

            if subtitles:
                logger.info(f"  Generating summary (duration: {duration_minutes:.1f} min)...")
                summary = generate_summary(subtitles, duration_minutes=duration_minutes)

                with open(os.path.join(session_dir, "summary.md"), "w", encoding="utf-8") as f:
                    f.write(summary)

                logger.info(f"  ✓ Completed: {session_code}")
            else:
                logger.warning(f"  ⚠ No subtitles available for: {session_code}")

        except Exception as e:
            logger.error(f"  ✗ Error processing {video.get('title', 'unknown')}: {e}")
            continue

if __name__ == "__main__":
    main()
