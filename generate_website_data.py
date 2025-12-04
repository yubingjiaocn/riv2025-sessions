#!/usr/bin/env python3
import json
import os
import shutil

SESSIONS_DIR = "sessions"
DOCS_DIR = "docs"

def main():
    sessions = []
    
    for session_code in os.listdir(SESSIONS_DIR):
        session_path = os.path.join(SESSIONS_DIR, session_code)
        if not os.path.isdir(session_path):
            continue
        
        metadata_file = os.path.join(session_path, "metadata.json")
        if not os.path.exists(metadata_file):
            continue
        
        with open(metadata_file, 'r', encoding='utf-8') as f:
            metadata = json.load(f)
        
        summary_file = os.path.join(session_path, "summary.md")
        metadata['summary'] = os.path.exists(summary_file)
        
        sessions.append(metadata)
    
    # Write sessions.json
    with open(os.path.join(DOCS_DIR, "sessions.json"), 'w', encoding='utf-8') as f:
        json.dump(sessions, f, ensure_ascii=False, indent=2)
    
    # Copy session folders to docs
    docs_sessions = os.path.join(DOCS_DIR, "sessions")
    if os.path.exists(docs_sessions):
        shutil.rmtree(docs_sessions)
    shutil.copytree(SESSIONS_DIR, docs_sessions)
    
    print(f"Generated website data with {len(sessions)} sessions")

if __name__ == "__main__":
    main()
