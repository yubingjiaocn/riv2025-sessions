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

PLAYLIST_URL = "https://www.youtube.com/playlist?list=PL2yQDdvlhXf9gdFFBcDPUHAJS7kkIkIet"
CATALOG_API = "https://catalog.awsevents.com/api/search"
OUTPUT_DIR = "sessions_test"

def translate_text(text):
    """Translate text using Kiro CLI"""
    result = subprocess.run(
        ["kiro-cli", "chat", "--no-interactive", "--agent=translator"],
        input=text,
        capture_output=True,
        text=True,
        timeout=300
    )
    return result.stdout.strip()

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
    # Limit subtitle length for testing
    subtitles_preview = subtitles[:5000] if len(subtitles) > 5000 else subtitles
    prompt = f"Please summarize this AWS session based on the following subtitles:\n\n{subtitles_preview}"
    result = subprocess.run(
        ["kiro-cli", "chat", "--no-interactive", "--agent=summarizer"],
        input=prompt,
        capture_output=True,
        text=True,
        timeout=600
    )
    return result.stdout.strip()

# Test with first video
os.makedirs(OUTPUT_DIR, exist_ok=True)

logger.info("Fetching playlist...")
ydl_opts = {'extract_flat': True, 'quiet': True}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    playlist_info = ydl.extract_info(PLAYLIST_URL, download=False)
    videos = playlist_info['entries']

logger.info(f"Found {len(videos)} videos")

video = videos[0]
video_url = f"https://www.youtube.com/watch?v={video['id']}"
title = video['title']

logger.info(f"Processing: {title}")

# Search catalog
logger.info("  Searching catalog...")
session_data = search_session(title)
if not session_data:
    logger.error("  ✗ No catalog data found")
    exit(1)

session_code = session_data.get("code", "UNKNOWN")
logger.info(f"  Found session: {session_code}")

# Translate
logger.info("  Translating title...")
title_cn = translate_text(title)
logger.info(f"  Title (CN): {title_cn}")

abstract = session_data.get("abstract", "")[:200]  # Limit for testing
if abstract:
    logger.info("  Translating abstract...")
    abstract_cn = translate_text(abstract)
    logger.info(f"  Abstract (CN): {abstract_cn[:100]}...")
else:
    abstract_cn = ""

# Get subtitles
logger.info("  Fetching subtitles...")
subtitles = get_subtitles(video_url)
if subtitles:
    logger.info(f"  Got {len(subtitles)} characters of subtitles")

    logger.info("  Generating summary (this may take a minute)...")
    summary = generate_summary(subtitles)
    logger.info(f"  Summary length: {len(summary)} characters")
    logger.info(f"  Summary preview: {summary[:200]}...")
else:
    logger.warning("  ✗ No subtitles available")

logger.info("✓ Full pipeline test completed successfully!")
