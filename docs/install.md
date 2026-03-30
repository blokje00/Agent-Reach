# Agent Reach — Installation Guide

## For Humans

Copy this to your AI Agent:

```
Install Agent Reach for me: https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/install.md
```

> 🛡️ **Security-conscious?** Use safe mode — it won't auto-install system packages:
> ```
> Install Agent Reach for me (safe mode): https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/install.md
> Use the --safe flag during installation
> ```

---

## For AI Agents

### Goal

Install Agent Reach and all upstream tools so your user's agent has full internet access. After installation, you'll use the upstream tools directly (bird CLI, yt-dlp, mcporter, gh CLI, etc.) — Agent Reach is just the installer and health checker.

### ⚠️ Boundaries

When fixing issues, stay within these limits:

- **DO NOT** run commands with `sudo` unless the user explicitly approved
- **DO NOT** modify system files outside `~/.agent-reach/`
- **DO NOT** install packages not listed in this guide
- **DO NOT** disable firewalls, security settings, or system protections
- **DO NOT** clone repos, create files, or run commands inside the agent workspace / working directory
- If something requires elevated permissions, **tell the user** what's needed and let them decide

### 📁 Directory Rules

All Agent Reach files go in dedicated directories — **never in the agent workspace**:

| Purpose | Directory | Example |
|---------|-----------|---------|
| Config & tokens | `~/.agent-reach/` | `~/.agent-reach/config.json` |
| Upstream tool repos | `~/.agent-reach/tools/` | `~/.agent-reach/tools/douyin-mcp-server/` |
| Temporary files | `/tmp/` | `/tmp/yt-dlp-output/` |
| Skills | `~/.openclaw/skills/agent-reach/` | SKILL.md |

**Why?** If you clone repos or create files in the workspace, it pollutes the user's project directory and can break their agent over time. Keep the workspace clean.

### Step 1: Install

**Default (fully automatic):**

```bash
# Recommended: pipx (simplest)
pipx install https://github.com/Panniantong/agent-reach/archive/main.zip
agent-reach install --env=auto

# If your Python comes from Homebrew / you get PEP 668 (externally-managed-environment)
# Use a virtual environment:
python3 -m venv ~/.agent-reach-venv
source ~/.agent-reach-venv/bin/activate
pip install https://github.com/Panniantong/agent-reach/archive/main.zip
agent-reach install --env=auto
```

This auto-installs system dependencies (gh CLI, Node.js, mcporter, bird), configures Exa search, detects environment, and tests all channels.

> 💡 **macOS / Homebrew Python showing `externally-managed-environment`?**
> This is PEP 668 protection, not an Agent Reach issue. Prefer `pipx install ...`, or create a `venv` first.


**Safe mode (no automatic system changes):**

If the user asked for safe mode, or you're on a production machine:

```bash
pip install https://github.com/Panniantong/agent-reach/archive/main.zip
agent-reach install --env=auto --safe
```

Safe mode checks what's installed and tells you what's missing, but doesn't auto-install system packages. You can then install each dependency manually.

**Dry run (preview only):**

```bash
agent-reach install --env=auto --dry-run
```

Shows what would be done without making any changes.

**Read the output carefully**, then run:

```bash
agent-reach doctor
```

### Step 2: Fix what's broken

`agent-reach doctor` shows you which channels are active and which aren't.

Try to get as many channels to ✅ as possible. If something failed during install or shows as ❌/⚠️ in doctor, diagnose the problem and try to fix it — but stay within the boundaries above. If a fix requires elevated permissions or system changes, ask the user first.

Only ask the user when you genuinely need their input (credentials, permissions, etc.).

### Step 3: Configure things that need user input

Some channels need credentials only the user can provide. Based on the doctor output, ask for what's missing:

> 🔒 **Security tip:** For platforms that need cookies (Twitter, XiaoHongShu), we recommend using a **dedicated/secondary account** rather than your main account. Cookie-based auth carries two risks:
> 1. **Account ban** — platforms may detect non-browser API calls and restrict or ban the account
> 2. **Credential exposure** — cookies grant full account access; using a secondary account limits the blast radius if credentials are ever compromised

> 🍪 **Cookie import (universal for all platforms requiring login):**
>
> For all platforms that require cookies (Twitter, XiaoHongShu, etc.), **prefer Cookie-Editor import** — it's the simplest and most reliable method:
> 1. Log in to the platform in your own browser
> 2. Install the [Cookie-Editor](https://chromewebstore.google.com/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm) Chrome extension
> 3. Click the extension → Export → Header String
> 4. Send the exported string to the Agent
>
> **Local computer users** can also use `agent-reach configure --from-browser chrome` for one-click automatic extraction (supports Twitter + XiaoHongShu).

**Twitter search & posting:**
> "To unlock Twitter search, I need your Twitter cookies. Install the Cookie-Editor Chrome extension, go to x.com/twitter.com, click the extension → Export → Header String, and paste it to me."

```bash
agent-reach configure twitter-cookies "PASTED_STRING"
```

> **Proxy note (networks requiring a VPN/proxy, e.g. mainland China):**
>
> bird CLI uses Node.js; in environments that need a proxy you can configure it via environment variables.
> Agent Reach automatically installs `undici` (`npm install -g undici`) during setup for proxy support.
>
> **What you (the Agent) need to do:**
> 1. Confirm the user configured a proxy: `agent-reach configure proxy http://user:pass@ip:port`
> 2. Set environment variables: `export HTTP_PROXY="..." HTTPS_PROXY="..."`
> 3. Agent Reach handles the rest automatically — no extra steps needed from the user
>
> If the user reports "fetch failed", see [troubleshooting.md](troubleshooting.md)

**Reddit & Bilibili full access (server users):**
> "Reddit and Bilibili block server IPs. To unlock full access, I need a residential proxy. You can get one at https://webshare.io ($1/month). Send me the proxy address."

```bash
agent-reach configure proxy http://user:pass@ip:port
```

**XiaoHongShu (requires Docker):**
> "XiaoHongShu requires an MCP service. You need Docker on your machine. Once Docker is installed, I'll take care of the rest."

```bash
docker run -d --name xiaohongshu-mcp -p 18060:18060 xpzouying/xiaohongshu-mcp
mcporter config add xiaohongshu http://localhost:18060/mcp
```

> On a server, add a proxy to avoid IP risk:
> `docker run -d --name xiaohongshu-mcp -p 18060:18060 -e XHS_PROXY=http://user:pass@ip:port xpzouying/xiaohongshu-mcp`
>
> **Login method (prefer Cookie-Editor — simplest):**
> 1. Log in to XiaoHongShu (xiaohongshu.com) in your own browser
> 2. Export cookies with [Cookie-Editor](https://chromewebstore.google.com/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm) (JSON or Header String format both work)
> 3. Send the cookie string to the Agent
> 4. Agent runs the command to complete login:
>
> ```bash
> # JSON format (Cookie-Editor → Export → JSON)
> agent-reach configure xhs-cookies '[{"name":"web_session","value":"xxx","domain":".xiaohongshu.com",...}]'
>
> # Or Header String format (Cookie-Editor → Export → Header String)
> agent-reach configure xhs-cookies "key1=val1; key2=val2; ..."
> ```
>
> **Alternative:** On a local computer with a browser, open http://localhost:18060 and scan the QR code to log in.

**Weibo (mcp-server-weibo):**
> "Weibo is installed by default and ready to use. You can search Weibo content, view trending topics, and get user posts and comments."

If automatic installation fails, install manually:

```bash
pip install git+https://github.com/Panniantong/mcp-server-weibo.git
mcporter config add weibo --command 'mcp-server-weibo'
```

> No login, no cookies, no proxy needed. Works directly from overseas servers too.

**Xiaoyuzhou Podcast (Groq Whisper):**
> "Xiaoyuzhou podcast transcription is installed by default — just needs a free Groq API Key."

The script is automatically installed with Agent Reach; the user only needs to provide the key:

```bash
agent-reach configure groq-key gsk_xxxxx
```

> **Get a Groq API Key (free, no credit card, done in 30 seconds):**
> 1. Open https://console.groq.com
> 2. Sign in with Google/GitHub (or sign up)
> 3. Left menu → API Keys → Create API Key
> 4. Copy the key (starts with `gsk_`) and send it to the Agent
>
> **How it works:**
> User sends a Xiaoyuzhou link to the Agent; the Agent automatically calls:
> ```bash
> bash ~/.agent-reach/tools/xiaoyuzhou/transcribe.sh https://www.xiaoyuzhoufm.com/episode/xxxxx
> ```
>
> Downloads audio → transcodes and segments → Groq Whisper transcription → outputs full text.
>
> **Free tier and limits:**
> - ~2 hours of audio per hour (7200 seconds); auto-recovers after 15 minutes if exceeded
> - More than sufficient for listening to a few podcast episodes a day
> - High transcription quality (Whisper large-v3), but no speaker diarization
> - For podcasts over 2 hours, process in batches

**Douyin (douyin-mcp-server):**
> "Douyin video parsing requires an MCP service. After installing douyin-mcp-server you can parse videos and get watermark-free download links."

```bash
# 1. Install
pip install douyin-mcp-server

# 2. Start the HTTP service (port 18070)
# Method 1: with uv (recommended)
mkdir -p ~/.agent-reach/tools && cd ~/.agent-reach/tools
git clone https://github.com/yzfly/douyin-mcp-server.git && cd douyin-mcp-server
uv sync && uv run python run_http.py

# Method 2: start directly with Python
python -c "
from douyin_mcp_server.server import mcp
mcp.settings.host = '127.0.0.1'
mcp.settings.port = 18070
mcp.run(transport='streamable-http')
"

# 3. Register with mcporter
mcporter config add douyin http://localhost:18070/mcp
```

> No authentication required to parse video info and get download links.
> For AI speech recognition to extract transcripts, configure a SiliconFlow API Key (`export API_KEY="sk-xxx"`).
>
> See https://github.com/yzfly/douyin-mcp-server

**LinkedIn (optional — linkedin-scraper-mcp):**
> "LinkedIn basic content can be read via Jina Reader. Full functionality (Profile details, job search) requires linkedin-scraper-mcp."

```bash
pip install linkedin-scraper-mcp
```

> **Login method (requires a browser UI):**
>
> linkedin-scraper-mcp uses a Chromium browser to log in; you need to be able to see a browser window.
>
> - **Local computer (with desktop):** Run directly:
>   ```bash
>   linkedin-scraper-mcp --login --no-headless
>   ```
>   A browser will open; log in to LinkedIn manually.
>
> - **Server (no UI):** Requires VNC remote desktop:
>   ```bash
>   # 1. Install and start VNC on the server (skip if already set up)
>   apt install -y tigervnc-standalone-server
>   vncserver :1 -geometry 1280x720
>   
>   # 2. Connect with a VNC client to server_IP:5901
>   
>   # 3. In the VNC desktop terminal, run:
>   export DISPLAY=:1
>   linkedin-scraper-mcp --login --no-headless
>   ```
>   Log in manually when the browser appears in VNC. The session is saved to `~/.linkedin-mcp/profile/`.
>
> **After login, start the MCP service:**
> ```bash
> linkedin-scraper-mcp --transport streamable-http --port 8001
> mcporter config add linkedin http://localhost:8001/mcp
> ```
>
> See https://github.com/stickerdaniel/linkedin-mcp-server

### Step 4: Final check

Run `agent-reach doctor` one final time and report the results to your user.

### Step 5: Set up daily monitoring (OpenClaw only)

If you are running inside **OpenClaw**, ask your user:

> "Agent Reach is installed. Would you like me to set up a daily automated check? It will monitor whether the channels are working and whether there are new versions. It only notifies you if something needs attention."

If the user agrees, create a **cron job** (daily, `sessionTarget: "isolated"`, `delivery: "announce"`) with this task:

```
Run the agent-reach watch command.
If the output contains "All OK", no notification is needed — exit silently.
If the output contains issues (❌ ⚠️) or a new version (🆕), send the full report to the user and suggest fixes.
If a new version is available, ask the user whether to upgrade (upgrade command: pip install --upgrade https://github.com/Panniantong/agent-reach/archive/main.zip).
```

If the user wants a different agent to handle it, let them choose.

---

## Quick Reference

| Command | What it does |
|---------|-------------|
| `agent-reach install --env=auto` | Full auto-setup (installs deps + configures) |
| `agent-reach install --env=auto --safe` | Safe setup (no auto system changes) |
| `agent-reach install --env=auto --dry-run` | Preview what would be done |
| `agent-reach doctor` | Show channel status |
| `agent-reach watch` | Quick health + update check (for scheduled tasks) |
| `agent-reach check-update` | Check for new versions |
| `agent-reach configure twitter-cookies "..."` | Unlock Twitter search + posting |
| `agent-reach configure proxy URL` | Unlock Reddit + Bilibili on servers |
| `agent-reach configure groq-key gsk_xxx` | Unlock Xiaoyuzhou podcast transcription |

After installation, use upstream tools directly. See SKILL.md for the full command reference:

| Platform | Upstream Tool | Example |
|----------|--------------|---------|
| Twitter/X | `bird` | `bird search "query" -n 10` |
| YouTube | `yt-dlp` | `yt-dlp --dump-json URL` |
| Bilibili | `yt-dlp` | `yt-dlp --dump-json URL` |
| Reddit | `curl` | `curl -s "https://reddit.com/r/xxx.json"` |
| GitHub | `gh` | `gh search repos "query"` |
| Web | `curl` + Jina | `curl -s "https://r.jina.ai/URL"` |
| Exa Search | `mcporter` | `mcporter call 'exa.web_search_exa(...)'` |
| XiaoHongShu | `mcporter` | `mcporter call 'xiaohongshu.search_feeds(...)'` |
| Weibo | `mcporter` | `mcporter call 'weibo.get_trendings(limit: 10)'` |
| Xiaoyuzhou Podcast | `transcribe.sh` | `bash ~/.agent-reach/tools/xiaoyuzhou/transcribe.sh <URL>` |
| Douyin | `mcporter` | `mcporter call 'douyin.parse_douyin_video_info(...)'` |
| LinkedIn | `mcporter` | `mcporter call 'linkedin.get_person_profile(...)'` |
| RSS | `feedparser` | `python3 -c "import feedparser; ..."` |
