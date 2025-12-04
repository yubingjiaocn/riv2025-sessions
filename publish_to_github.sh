#!/bin/bash

# Initialize git repo if not exists
if [ ! -d .git ]; then
    git init
    git branch -M main
fi

# Add all files
git add .

# Commit
git commit -m "Add AWS re:Invent 2025 session catalog"

# Ask for GitHub repo URL
echo "Please create a new GitHub repository and enter the URL:"
read REPO_URL

# Add remote and push
git remote add origin "$REPO_URL" 2>/dev/null || git remote set-url origin "$REPO_URL"
git push -u origin main

echo "Published to GitHub! Enable GitHub Pages in repository settings (Settings > Pages > Source: main branch /docs folder)"
