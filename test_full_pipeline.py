#!/usr/bin/env python3
import json
import os
import subprocess
import urllib.parse
import yt_dlp
import requests

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
            print(f"    Error fetching subtitles: {e}")
    
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

print("Fetching playlist...")
ydl_opts = {'extract_flat': True, 'quiet': True}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    playlist_info = ydl.extract_info(PLAYLIST_URL, download=False)
    videos = playlist_info['entries']

print(f"Found {len(videos)} videos\n")

video = videos[0]
video_url = f"https://www.youtube.com/watch?v={video['id']}"
title = video['title']

print(f"Processing: {title}")

# Search catalog
print("  Searching catalog...")
session_data = search_session(title)
if not session_data:
    print("  ✗ No catalog data found")
    exit(1)

session_code = session_data.get("code", "UNKNOWN")
print(f"  Found session: {session_code}")

# Translate
print("  Translating title...")
title_cn = translate_text(title)
print(f"  Title (CN): {title_cn}")

abstract = session_data.get("abstract", "")[:200]  # Limit for testing
if abstract:
    print("  Translating abstract...")
    abstract_cn = translate_text(abstract)
    print(f"  Abstract (CN): {abstract_cn[:100]}...")
else:
    abstract_cn = ""

# Get subtitles
print("  Fetching subtitles...")
subtitles = get_subtitles(video_url)
if subtitles:
    print(f"  Got {len(subtitles)} characters of subtitles")
    
    print("  Generating summary (this may take a minute)...")
    summary = generate_summary(subtitles)
    print(f"  Summary length: {len(summary)} characters")
    print(f"  Summary preview: {summary[:200]}...")
else:
    print("  ✗ No subtitles available")

print("\n✓ Full pipeline test completed successfully!")
