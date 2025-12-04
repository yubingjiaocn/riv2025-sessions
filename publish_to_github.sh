#!/bin/bash

# Ask for GitHub repo URL
# echo "Please create a new GitHub repository and enter the URL:"
REPO_URL=https://github.com/yubingjiaocn/riv2025-sessions

# Initialize git repo if not exists
if [ ! -d .git ]; then
    git init
    git branch -M main
    git remote add origin "$REPO_URL" 2>/dev/null || git remote set-url origin "$REPO_URL"
fi

# Add all files
git add .

# Commit
git commit -m "Add AWS re:Invent 2025 session catalog"

git push -u origin main

echo "Published to GitHub! Enable GitHub Pages in repository settings (Settings > Pages > Source: main branch /docs folder)"
