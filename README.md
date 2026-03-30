<h1 align="center">👁️ Agent Reach</h1>

<p align="center">
  <strong>One-click internet capabilities for your AI Agent</strong>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge" alt="MIT License"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.10+-green.svg?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.8+"></a>
  <a href="https://github.com/Panniantong/agent-reach/stargazers"><img src="https://img.shields.io/github/stars/Panniantong/agent-reach?style=for-the-badge" alt="GitHub Stars"></a>
</p>

<p align="center">
  <a href="#quick-start">Quick Start</a> · <a href="#supported-platforms">Supported Platforms</a> · <a href="#design-philosophy">Design Philosophy</a>
</p>

---

## Why Agent Reach?

AI Agents can already help you write code, edit documents, and manage projects — but ask one to look something up online and it hits a wall:

- 📺 "Summarize this YouTube tutorial for me" → **Can't**, subtitles not accessible
- 🐦 "Search Twitter to see what people think of this product" → **Can't**, Twitter API requires payment
- 📖 "Check Reddit for anyone who hit this same bug" → **403 blocked**, server IP rejected
- 📕 "Look up reviews of this product on XiaoHongShu" → **Can't open**, login required
- 📺 "There's a tech video on Bilibili, summarize it" → **Can't connect**, overseas/server IP blocked
- 🔍 "Search the web for the latest LLM framework comparison" → **No good search**, either paid or poor quality
- 🌐 "Check what this webpage says" → **Returns raw HTML**, completely unreadable
- 📦 "What does this GitHub repo do? What's in the Issues?" → Works, but auth configuration is painful
- 📡 "Subscribe to these RSS feeds and notify me of updates" → Need to install libraries and write code

**These aren't hard to solve — they just require a bit of setup**

Every platform has its own barrier — paid APIs, IP blocks, logins, data cleanup. You have to troubleshoot each one individually: install tools, configure settings, set up auth. Just getting an Agent to read a tweet takes forever.

**Agent Reach turns this into a single command:**

```
Install Agent Reach for me: https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/install.md
```

Send that to your Agent. A few minutes later it can read Twitter, search Reddit, watch YouTube, and browse XiaoHongShu.

**Already installed? Updates are just as easy:**

```
Update Agent Reach: https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/update.md
```

> ⭐ **Star this project** and we'll keep tracking platform changes and adding new channels. You don't need to monitor anything — when a platform breaks we'll fix it, when there's a new channel we'll add it.

### ✅ Before you use it, you might want to know

| | |
|---|---|
| 💰 **Completely free** | All tools are open-source, all APIs are free. The only optional cost is a server proxy (~$1/month); local computers don't need one |
| 🔒 **Privacy-first** | Cookies are stored locally only — never uploaded or shared. Code is fully open-source and auditable |
| 🔄 **Continuously updated** | Upstream tools (yt-dlp, bird, Jina Reader, etc.) are regularly tracked and updated; you don't have to watch them |
| 🤖 **Works with any Agent** | Claude Code, OpenClaw, Cursor, Windsurf… any Agent that can run CLI commands can use it |
| 🩺 **Built-in diagnostics** | `agent-reach doctor` tells you what's working, what isn't, and how to fix it |

---

## Supported Platforms

| Platform | Ready out of the box | Unlocked after setup | How to configure |
|----------|---------------------|---------------------|-----------------|
| 🌐 **Web** | Read any web page | — | No config needed |
| 📺 **YouTube** | Subtitle extraction + video search | — | No config needed |
| 📡 **RSS** | Read any RSS/Atom feed | — | No config needed |
| 🔍 **Web Search** | — | Full semantic web search | Auto-configured (MCP, free, no key) |
| 📦 **GitHub** | Read public repos + search | Private repos, Issues, PRs, Fork | Tell Agent "log me into GitHub" |
| 🐦 **Twitter/X** | Read individual tweets | Search tweets, timeline, post | Tell Agent "set up Twitter for me" |
| 📺 **Bilibili** | Local: subtitle extraction + search | Works on servers too | Tell Agent "set up a proxy for me" |
| 📖 **Reddit** | Search (via Exa, free) | Read posts and comments | Tell Agent "set up a proxy for me" |
| 📕 **XiaoHongShu** | — | Read, search, post, comment, like | Tell Agent "set up XiaoHongShu for me" |
| 🎵 **Douyin** | — | Video parsing, watermark-free download links | Tell Agent "set up Douyin for me" |
| 💼 **LinkedIn** | Jina Reader for public pages | Profile details, company pages, job search | Tell Agent "set up LinkedIn for me" |
| 💬 **WeChat Official Accounts** | Search + read articles (full Markdown) | — | No config needed |
| 📰 **Weibo** | Trending, search content/users/topics, user posts, comments | — | No config needed |
| 💻 **V2EX** | Hot topics, node topics, topic details + replies, user info | — | No config needed |
| 📈 **Xueqiu** | Stock quotes, stock search, hot posts, hot stocks ranking | — | No config needed |
| 🎙️ **Xiaoyuzhou Podcast** | — | Podcast audio transcription (Whisper, free key) | Tell Agent "set up Xiaoyuzhou podcast for me" |

> **Not sure how to configure something?** Don't bother with the docs. Just tell your Agent "set up XXX for me" — it knows what's needed and will walk you through it step by step.
>
> 🍪 For platforms requiring cookies (Twitter, XiaoHongShu, etc.), **prefer** using the Chrome extension [Cookie-Editor](https://chromewebstore.google.com/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm) to export cookies and send them to your Agent. Unified workflow: log in via browser → Cookie-Editor export → send to Agent. Simpler and more reliable than QR codes.
>
> 🔒 Cookies are stored locally only — never uploaded or shared. Code is fully open-source and auditable.
> 💻 Local computers don't need a proxy. A proxy is only needed when deployed on a server (~$1/month).

---

## Quick Start

> ⚠️ **OpenClaw users: confirm exec permission is enabled first**
>
> Agent Reach relies on the Agent being able to execute shell commands (`pip install`, `mcporter`, `bird`, etc.). If your OpenClaw is using the default `messaging` tool profile, the Agent cannot run commands. **Enable exec permission before installing**:
>
> ```bash
> openclaw config set tools.profile "coding"
> ```
> Or set `"tools": { "profile": "coding" }` in `~/.openclaw/openclaw.json`.
> After setting it, restart the Gateway (`openclaw gateway restart`) and start a new conversation. Other platforms (Claude Code, Cursor, Windsurf, etc.) are not affected.

Copy this to your AI Agent (Claude Code, OpenClaw, Cursor, etc.):

```
Install Agent Reach for me: https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/install.md
```

That's it. The Agent will handle everything else.

> 🔄 **Already installed?** Updates are just as easy:
> ```
> Update Agent Reach: https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/update.md
> ```

> 🛡️ **Security-conscious?** Use safe mode — won't auto-install system packages, just tells you what's needed:
> ```
> Install Agent Reach for me (safe mode): https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/install.md
> Use the --safe flag during installation
> ```

<details>
<summary>What does it do? (click to expand)</summary>

1. **Installs CLI tools** — `pip install` sets up the `agent-reach` command
2. **Installs system dependencies** — auto-detects and installs Node.js, gh CLI, mcporter, bird, etc.
3. **Configures search** — connects Exa via MCP (free, no API Key)
4. **Detects environment** — determines local vs server and gives relevant advice
5. **Registers SKILL.md** — installs the usage guide in the Agent's skills directory, so the Agent automatically knows which upstream tool to call when it encounters needs like "search Twitter" or "watch a video"

After installation, `agent-reach doctor` tells you the status of every channel.
</details>

---

## Ready Out of the Box

No configuration needed — just tell your Agent:

- "Check this link for me" → `curl https://r.jina.ai/URL` reads any web page
- "What does this GitHub repo do?" → `gh repo view owner/repo`
- "What's in this video?" → `yt-dlp --dump-json URL` extracts subtitles
- "Read this tweet for me" → `bird read URL`
- "Subscribe to this RSS feed" → `feedparser` parses it
- "Search GitHub for LLM frameworks" → `gh search repos "LLM framework"`

**No need to memorize commands.** After reading SKILL.md the Agent knows what to call.

---

## Design Philosophy

**Agent Reach is scaffolding, not a framework.**

Every time you set up a new Agent environment, you spend time finding tools, installing dependencies, and configuring settings — what to use for Twitter? How to bypass Reddit blocks? How to extract YouTube subtitles? You have to work through it every time.

Agent Reach does one thing: **handles those choices and configuration steps for you.**

After installation, the Agent calls upstream tools directly (bird CLI, yt-dlp, mcporter, gh CLI, etc.) — no Agent Reach wrapper layer needed.

### 🔌 Every channel is pluggable

Each platform is backed by an independent upstream tool. **Not happy? Swap it out.**

```
channels/
├── web.py          → Jina Reader     ← swap with Firecrawl, Crawl4AI…
├── twitter.py      → bird              ← swap with Nitter, official API…
├── youtube.py      → yt-dlp          ← swap with YouTube API, Whisper…
├── github.py       → gh CLI          ← swap with REST API, PyGithub…
├── bilibili.py     → yt-dlp          ← swap with bilibili-api…
├── reddit.py       → JSON API + Exa  ← swap with PRAW, Pushshift…
├── xiaohongshu.py  → mcporter MCP    ← swap with other XHS tools…
├── douyin.py       → mcporter MCP    ← swap with other Douyin tools…
├── linkedin.py     → linkedin-mcp    ← swap with LinkedIn API…
├── wechat.py       → camoufox+miku   ← search + read WeChat Official Account articles
├── rss.py          → feedparser      ← swap with atoma…
├── exa_search.py   → mcporter MCP    ← swap with Tavily, SerpAPI…
└── __init__.py     → channel registry (used by doctor checks)
```

Each channel file is only responsible for checking whether its upstream tool is available (the `check()` method), providing status information to `agent-reach doctor`. Actual reading and searching is done by the Agent calling upstream tools directly.

### Current Tool Choices

| Use case | Tool | Why |
|----------|------|-----|
| Read web pages | [Jina Reader](https://github.com/jina-ai/reader) | 9.8K Stars, free, no API Key |
| Read Twitter | [bird](https://www.npmjs.com/package/@steipete/bird) | Cookie auth, free. Official API is per-request ($0.005/read) |
| Video subtitles + search | [yt-dlp](https://github.com/yt-dlp/yt-dlp) | 148K Stars, supports YouTube + Bilibili + 1800 sites |
| Search the web | [Exa](https://exa.ai) via [mcporter](https://github.com/steipete/mcporter) | AI semantic search, MCP integration, no key needed |
| GitHub | [gh CLI](https://cli.github.com) | Official tool, full API access after auth |
| Read RSS | [feedparser](https://github.com/kurtmckee/feedparser) | Python ecosystem standard, 2.3K Stars |
| XiaoHongShu | [xiaohongshu-mcp](https://github.com/xpzouying/xiaohongshu-mcp) | ⭐9K+, Go, Docker one-click deploy |
| Douyin | [douyin-mcp-server](https://github.com/yzfly/douyin-mcp-server) | MCP service, no login, video parsing + watermark-free download |
| LinkedIn | [linkedin-scraper-mcp](https://github.com/stickerdaniel/linkedin-mcp-server) | ⭐900+, MCP service, browser automation |
| WeChat Official Accounts | [wechat-article-for-ai](https://github.com/Panniantong/wechat-article-for-ai) + [miku_ai](https://github.com/GobinFan/Miku_Spider) | Camoufox stealth browser for full-text reading + Sogou search |

> 📌 These are "current choices". Not happy with one? Swap out the corresponding file. That's exactly what scaffolding is for.

---

## Security

Agent Reach is designed with security in mind:

| Measure | Details |
|---------|---------|
| 🔒 **Local credential storage** | Cookies and tokens are stored only on your machine at `~/.agent-reach/config.yaml`, with permissions set to 600 (owner-only). Never uploaded or shared |
| 🛡️ **Safe mode** | `agent-reach install --safe` won't modify the system automatically — it lists what's needed and lets you decide |
| 👀 **Fully open-source** | Code is transparent and auditable at any time. All upstream tools are also open-source projects |
| 🔍 **Dry Run** | `agent-reach install --dry-run` previews all operations without making any changes |
| 🧩 **Pluggable architecture** | Don't trust a component? Swap out the corresponding channel file without affecting anything else |

### 🍪 Cookie Security Tips

> ⚠️ **Account ban risk:** Using Cookie auth on platforms like Twitter and XiaoHongShu carries a risk of being detected by the platform and having your account restricted or banned. Always use a **dedicated secondary account** — never your main account.

For platforms requiring cookies (Twitter, XiaoHongShu), use a **dedicated secondary account** for two reasons:
1. **Ban risk** — platforms may detect non-browser API behavior and restrict or ban the account
2. **Security risk** — cookies are equivalent to full login access; using a secondary account limits the impact if credentials are ever compromised

### 📦 Installation Methods

| Method | Command | Best for |
|--------|---------|---------|
| One-click auto (default) | `agent-reach install --env=auto` | Personal computers, dev environments |
| Safe mode | `agent-reach install --env=auto --safe` | Production servers, shared machines |
| Preview only | `agent-reach install --env=auto --dry-run` | See what will happen first |

### 🗑️ Uninstall

```bash
agent-reach uninstall
```

Removes: `~/.agent-reach/` (including all tokens/cookies), Agent skill files, MCP configurations in mcporter.

```bash
# Preview without deleting
agent-reach uninstall --dry-run

# Remove skill files only, keep token config (for reinstalling)
agent-reach uninstall --keep-config
```

Uninstall the Python package: `pip uninstall agent-reach`

---

## Contributing

This project was built with pure vibe coding 🎸 There may be some rough edges — please bear with it. If you find a bug, feel free to open an [Issue](https://github.com/Panniantong/agent-reach/issues) and I'll fix it as quickly as I can.

**Want a new channel?** Open an Issue and let us know, or submit a PR yourself.

**Want to add one locally?** Just have your Agent clone and modify it — each channel is a single independent file, easy to add.

[PRs](https://github.com/Panniantong/agent-reach/pulls) are always welcome!

---

## ⭐ Why it's worth starring

I use this project myself every day, so I'll keep maintaining it.

- New features and requested channels will be added over time
- Every channel will be kept **working, useful, and free**
- When platforms change anti-scraping or APIs break, I'll find solutions

Contributing to the infrastructure of Web 4.0 in my own small way.

Star it so you can find it next time you need it. ⭐

---

## FAQ

<details>
<summary><strong>How can an AI Agent search Twitter/X for free (no API costs)?</strong></summary>

Agent Reach uses [bird CLI](https://www.npmjs.com/package/@steipete/bird) with cookie auth to access Twitter — completely free. After installing Agent Reach, export your Twitter cookies with the Cookie-Editor extension, run `agent-reach configure twitter-cookies "your_cookies"`, and your Agent can search with `bird search "query"`.
</details>

<details>
<summary><strong>Reddit returning 403 / server IP blocked?</strong></summary>

Reddit blocks datacenter IPs. Configure a residential proxy: `agent-reach configure proxy http://user:pass@ip:port`. Webshare is recommended ($1/month). Local computers generally won't encounter this issue.
</details>

<details>
<summary><strong>How to get YouTube video transcripts for AI?</strong></summary>

`yt-dlp --dump-json "https://youtube.com/watch?v=xxx"` extracts video metadata; `yt-dlp --write-sub --skip-download "URL"` extracts subtitles. Uses yt-dlp under the hood, supports multiple languages. No API key needed.
</details>

<details>
<summary><strong>How do I get an AI Agent to read XiaoHongShu?</strong></summary>

XiaoHongShu requires running an MCP service via Docker. After installing Docker, `agent-reach install` configures it automatically. The Agent can then use `mcporter call 'xiaohongshu.get_feed_detail(...)'` to read notes or `mcporter call 'xiaohongshu.search_feeds(keyword: "query")'` to search.
</details>

<details>
<summary><strong>How do I get an AI Agent to parse Douyin videos?</strong></summary>

After installing douyin-mcp-server, the Agent can use `mcporter call 'douyin.parse_douyin_video_info(share_link: "share_link")'` to parse video info and get watermark-free download links. No login required — just send the Douyin share link to the Agent. See https://github.com/yzfly/douyin-mcp-server
</details>

<details>
<summary><strong>Compatible with Claude Code / Cursor / OpenClaw / Windsurf?</strong></summary>

Yes! Agent Reach is an installer + configuration tool — any AI coding agent that can run shell commands can use it. Works with Claude Code, Cursor, OpenClaw, Windsurf, Codex, and more. Just `pip install agent-reach`, run `agent-reach install`, and the agent can start using the upstream tools immediately.

**OpenClaw note:** If your OpenClaw is using the default `messaging` tool profile, the agent won't be able to run shell commands. Enable exec first: `openclaw config set tools.profile "coding"` (or set `"tools": { "profile": "coding" }` in `~/.openclaw/openclaw.json`), then restart the Gateway and start a new conversation before installing.
</details>

<details>
<summary><strong>Is this free? Any API costs?</strong></summary>

100% free. All backends are open-source tools (bird CLI, yt-dlp, Jina Reader, Exa, etc.) that don't require paid API keys. The only optional cost is a residential proxy (~$1/month) if you need Reddit/Bilibili access from a server.
</details>

---

## Acknowledgements

[Jina Reader](https://github.com/jina-ai/reader) · [yt-dlp](https://github.com/yt-dlp/yt-dlp) · [bird](https://www.npmjs.com/package/@steipete/bird) · [Exa](https://exa.ai) · [mcporter](https://github.com/steipete/mcporter) · [feedparser](https://github.com/kurtmckee/feedparser) · [xiaohongshu-mcp](https://github.com/xpzouying/xiaohongshu-mcp) · [douyin-mcp-server](https://github.com/yzfly/douyin-mcp-server) · [linkedin-scraper-mcp](https://github.com/stickerdaniel/linkedin-mcp-server)

## Contact

- 📧 **Email:** pnt01@foxmail.com
- 🐦 **Twitter/X:** [@Neo_Reidlab](https://x.com/Neo_Reidlab)

> Bug reports and feature requests go to [GitHub Issues](https://github.com/Panniantong/Agent-Reach/issues) — easier to track.

## License

[MIT](LICENSE)

## Friends

[FluxNode](https://fluxnode.org) — Affordable AI API relay, official pricing at a fraction of the cost, pay-as-you-go or by package. Works with OpenClaw, Claude Code, and any Agent.

[OpenClaw for Enterprise](https://github.com/littleben/openclaw-for-enterprise) — Enterprise multi-user OpenClaw deployment, use AI directly in Feishu, container isolation, one-command management.

[Tencent Cloud OpenClaw](https://www.tencentcloud.com/act/pro/intl-openclaw?referral_code=G76Y819A&lang=zh&pg=) — Deploy OpenClaw on Tencent Cloud Lighthouse in seconds, connect Agent Reach through conversation to give your OpenClaw full internet capabilities.

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Panniantong/Agent-Reach&type=Date&v=20260309)](https://star-history.com/#Panniantong/Agent-Reach&Date)
