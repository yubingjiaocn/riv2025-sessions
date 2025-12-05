#!/usr/bin/env python3
import json
import logging
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

# Test fetching playlist
logger.info("Fetching playlist...")
ydl_opts = {'extract_flat': True, 'quiet': True}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    playlist_info = ydl.extract_info(PLAYLIST_URL, download=False)
    videos = playlist_info['entries']

logger.info(f"Found {len(videos)} videos")

# Test first video
if videos:
    video = videos[0]
    video_url = f"https://www.youtube.com/watch?v={video['id']}"
    title = video['title']

    logger.info(f"Testing first video: {title}")
    logger.info(f"URL: {video_url}")

    # Test catalog search
    logger.info("Searching catalog...")
    session_data = search_session(title)
    if session_data:
        logger.info(f"Found session: {session_data.get('code')}")
        logger.info(f"Type: {session_data.get('type')}")
        logger.info(f"Speakers: {len(session_data.get('participants', []))}")
        logger.info(f"Abstract: {session_data.get('abstract', '')[:100]}...")
    else:
        logger.warning("No session data found")

    # Test subtitles
    logger.info("Checking subtitles...")
    ydl_opts = {
        'skip_download': True,
        'writesubtitles': True,
        'writeautomaticsub': True,
        'subtitleslangs': ['en'],
        'quiet': True,
        'cookiefile': 'cookies.txt'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=False)
        has_subs = 'subtitles' in info and 'en' in info['subtitles']
        has_auto = 'automatic_captions' in info and 'en' in info['automatic_captions']
        logger.info(f"Has subtitles: {has_subs}")
        logger.info(f"Has auto captions: {has_auto}")
