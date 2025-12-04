#!/usr/bin/env python3
import json
import urllib.parse
import yt_dlp
import requests

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
print("Fetching playlist...")
ydl_opts = {'extract_flat': True, 'quiet': True}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    playlist_info = ydl.extract_info(PLAYLIST_URL, download=False)
    videos = playlist_info['entries']

print(f"Found {len(videos)} videos")

# Test first video
if videos:
    video = videos[0]
    video_url = f"https://www.youtube.com/watch?v={video['id']}"
    title = video['title']
    
    print(f"\nTesting first video: {title}")
    print(f"URL: {video_url}")
    
    # Test catalog search
    print("\nSearching catalog...")
    session_data = search_session(title)
    if session_data:
        print(f"Found session: {session_data.get('code')}")
        print(f"Type: {session_data.get('type')}")
        print(f"Speakers: {len(session_data.get('participants', []))}")
        print(f"Abstract: {session_data.get('abstract', '')[:100]}...")
    else:
        print("No session data found")
    
    # Test subtitles
    print("\nChecking subtitles...")
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
        print(f"Has subtitles: {has_subs}")
        print(f"Has auto captions: {has_auto}")
