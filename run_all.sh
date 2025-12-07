#!/bin/bash
set -e

source .venv/bin/activate

echo ""
echo "=== Collecting session data ==="
python3 collect_sessions.py

echo ""
echo "=== Generating website data ==="
python3 generate_website_data.py

echo ""
echo "=== Setup complete! ==="
bash publish_to_github.sh

echo ""
echo "=== Push complete! ==="
