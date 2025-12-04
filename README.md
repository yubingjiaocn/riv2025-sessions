# AWS re:Invent 2025 Session Catalog

Automated system to fetch, translate, and catalog AWS re:Invent sessions from YouTube.

## Features

- Fetches videos from YouTube playlist
- Searches AWS Events catalog for session details
- Translates titles and abstracts to Chinese using Kiro CLI
- Extracts subtitles and generates summaries
- Creates static website with filtering capabilities
- Publishes to GitHub Pages

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Ensure Kiro CLI is installed and configured

3. Export YouTube cookies to `cookies.txt` in Netscape format
   - Use a browser extension like "Get cookies.txt LOCALLY" 
   - Place the file in the project root directory

## Usage

### Collect All Sessions
```bash
bash run_all.sh
```

This will:
1. Fetch all videos from the playlist
2. Search for session details
3. Translate content to Chinese
4. Extract subtitles and generate summaries
5. Generate website data

### Publish to GitHub

```bash
bash publish_to_github.sh
```

Follow the prompts to publish to your GitHub repository.

### Enable GitHub Pages

1. Go to your repository settings
2. Navigate to Pages
3. Set Source to: `main` branch, `/docs` folder
4. Save

Your site will be available at: `https://<username>.github.io/<repo-name>/`

## Project Structure

```
.
├── sessions/              # Session data (metadata + summaries)
│   └── <SESSION_CODE>/
│       ├── metadata.json
│       └── summary.md
├── docs/                  # Static website
│   ├── index.html
│   ├── session.html
│   ├── style.css
│   ├── app.js
│   ├── session.js
│   ├── sessions.json
│   └── sessions/         # Copy of session data
├── .kiro/
│   └── agents/           # Kiro CLI agent configs
│       ├── translator.json
│       └── summarizer.json
└── collect_sessions.py   # Main data collection script
```

## Manual Steps

If you want to run individual steps:

```bash
# Collect sessions
python3 collect_sessions.py

# Generate website data
python3 generate_website_data.py
```
