#!/bin/bash
set -e

echo "=== Installing dependencies ==="
pip install -r requirements.txt

echo ""
echo "=== Collecting session data ==="
python3 collect_sessions.py

echo ""
echo "=== Generating website data ==="
python3 generate_website_data.py

echo ""
echo "=== Setup complete! ==="
echo "To publish to GitHub, run: bash publish_to_github.sh"
