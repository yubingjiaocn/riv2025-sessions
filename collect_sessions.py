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
        return items[0] if items else None
    return None

def get_subtitles(video_url):
    """Fetch subtitles from YouTube video"""
    import tempfile
    import glob

    with tempfile.TemporaryDirectory() as tmpdir:
        ydl_opts = {
            'skip_download': True,
            'writesubtitles': True,
            'writeautomaticsub': True,
            'subtitleslangs': ['en'],
            'subtitlesformat': 'vtt',
            'quiet': True,
            'noprogress': True,
            'cookiefile': 'cookies.txt',
            'outtmpl': f'{tmpdir}/subtitle'
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])

            # Find the downloaded subtitle file
            vtt_files = glob.glob(f'{tmpdir}/*.vtt')
            if vtt_files:
                with open(vtt_files[0], 'r', encoding='utf-8') as f:
                    return f.read()

        except Exception as e:
            logger.error(f"    Error fetching subtitles: {e}")

    return None

def generate_summary(subtitles):
    """Generate summary using Kiro CLI"""
    # Clean VTT format - remove timestamps and metadata, keep only text
    import re
    lines = subtitles.split('\n')
    text_lines = []
    for line in lines:
        line = line.strip()
        # Skip VTT headers, timestamps, and empty lines
        if line and not line.startswith('WEBVTT') and not '-->' in line and not line.isdigit():
            # Remove VTT tags like <c>
            line = re.sub(r'<[^>]+>', '', line)
            text_lines.append(line)

    clean_text = ' '.join(text_lines)

    # Limit to ~100K characters to avoid context overflow
    if len(clean_text) > 100000:
        clean_text = clean_text[:100000] + '...'

    prompt = f"Please summarize this AWS session based on the following subtitles:\n\n{clean_text}"
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
                "session_code": session_code
            }

            with open(os.path.join(session_dir, "metadata.json"), "w", encoding="utf-8") as f:
                json.dump(metadata, f, ensure_ascii=False, indent=2)

            # Get subtitles and generate summary
            logger.info(f"  Fetching subtitles...")
            subtitles = get_subtitles(video_url)

            if subtitles:
                logger.info(f"  Generating summary...")
                summary = generate_summary(subtitles)

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
