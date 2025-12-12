#!/usr/bin/env python3
"""
Find and delete sessions where title_cn or abstract_cn don't contain Chinese characters
"""

import json
import os
import shutil
import re
from pathlib import Path


def contains_chinese(text):
    """Check if text contains Chinese characters"""
    if not text:
        return False
    # Unicode range for Chinese characters (CJK Unified Ideographs)
    chinese_pattern = re.compile(r'[\u4e00-\u9fff]+')
    return bool(chinese_pattern.search(text))


def find_untranslated_sessions():
    """Find sessions where translations don't contain Chinese characters"""
    sessions_dir = Path("/home/ubuntu/riv2025/sessions")
    docs_sessions_dir = Path("/home/ubuntu/riv2025/docs/sessions")

    untranslated = []

    # Scan all session directories
    for session_dir in sorted(sessions_dir.iterdir()):
        if not session_dir.is_dir():
            continue

        metadata_file = session_dir / "metadata.json"
        if not metadata_file.exists():
            continue

        try:
            with open(metadata_file, 'r', encoding='utf-8') as f:
                data = json.load(f)

            session_code = data.get('session_code', session_dir.name)
            title_cn = data.get('title_cn', '')
            abstract_cn = data.get('abstract_cn', '')

            # Check if either title_cn or abstract_cn doesn't contain Chinese
            title_has_chinese = contains_chinese(title_cn)
            abstract_has_chinese = contains_chinese(abstract_cn)

            if not title_has_chinese or not abstract_has_chinese:
                untranslated.append({
                    'session_code': session_code,
                    'session_dir': session_dir,
                    'docs_dir': docs_sessions_dir / session_dir.name,
                    'title_has_chinese': title_has_chinese,
                    'abstract_has_chinese': abstract_has_chinese,
                    'title_cn': title_cn[:100] + '...' if len(title_cn) > 100 else title_cn,
                    'abstract_cn': abstract_cn[:100] + '...' if len(abstract_cn) > 100 else abstract_cn
                })

        except Exception as e:
            print(f"Error processing {session_dir.name}: {e}")
            continue

    return untranslated


def delete_sessions(untranslated_sessions):
    """Delete the untranslated session directories"""
    deleted = []
    errors = []

    for session in untranslated_sessions:
        session_code = session['session_code']
        session_dir = session['session_dir']
        docs_dir = session['docs_dir']

        try:
            # Delete from sessions directory
            if session_dir.exists():
                shutil.rmtree(session_dir)
                print(f"✓ Deleted: {session_dir}")
                deleted.append(session_code)

            # Delete from docs/sessions directory
            if docs_dir.exists():
                shutil.rmtree(docs_dir)
                print(f"✓ Deleted: {docs_dir}")

        except Exception as e:
            print(f"✗ Error deleting {session_code}: {e}")
            errors.append((session_code, str(e)))

    return deleted, errors


def main():
    import sys

    print("Scanning for untranslated sessions...\n")

    untranslated = find_untranslated_sessions()

    if not untranslated:
        print("No untranslated sessions found!")
        return

    print(f"Found {len(untranslated)} untranslated sessions:\n")

    for session in untranslated:
        print(f"Session: {session['session_code']}")
        print(f"  Title has Chinese: {session['title_has_chinese']}")
        print(f"  Abstract has Chinese: {session['abstract_has_chinese']}")

        if not session['title_has_chinese']:
            print(f"  Title CN (untranslated): {session['title_cn']}")

        if not session['abstract_has_chinese']:
            print(f"  Abstract CN (untranslated): {session['abstract_cn']}")

        print()

    # Check for --yes flag for automatic confirmation
    auto_confirm = '--yes' in sys.argv or '-y' in sys.argv

    if not auto_confirm:
        # Ask for confirmation
        print(f"\nAbout to delete {len(untranslated)} sessions.")
        try:
            response = input("Continue? (yes/no): ").strip().lower()
        except EOFError:
            print("\nNo input provided. Use --yes flag to auto-confirm.")
            return

        if response != 'yes':
            print("Cancelled.")
            return

    print("\nDeleting sessions...\n")
    deleted, errors = delete_sessions(untranslated)

    print(f"\n{'='*60}")
    print(f"Summary:")
    print(f"  Total found: {len(untranslated)}")
    print(f"  Successfully deleted: {len(deleted)}")
    print(f"  Errors: {len(errors)}")

    if errors:
        print("\nErrors:")
        for session_code, error in errors:
            print(f"  {session_code}: {error}")


if __name__ == "__main__":
    main()
