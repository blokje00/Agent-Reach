# Twitter Advanced Features Setup Guide (bird CLI)

Twitter basic reading is available for free via Jina Reader, no setup required.

Advanced features require bird CLI (@steipete/bird):

- Search tweets (`bird search`)
- Read full tweets and conversation threads (`bird read`, `bird thread`)
- User timelines (`bird user-tweets`)

bird is a free open-source tool (npm package @steipete/bird), but requires your Twitter account cookie.

## Quick Setup

1. Check if bird is installed:
```bash
bird check
```

2. Install bird:
```bash
npm install -g @steipete/bird
```

> Alternative package: `npm install -g @connormartin/bird`

3. Test if configured:
```bash
bird check
```

## Get Cookie (Cookie-Editor method, recommended)

1. Install the [Cookie-Editor](https://cookie-editor.com/) browser extension
2. Log in to x.com
3. Click the Cookie-Editor icon → Export → Copy all
4. Run the configuration command:
```bash
agent-reach configure twitter-cookies "paste the cookie JSON here"
```

This automatically extracts `auth_token` and `ct0` and writes them as environment variables.

## Manual Cookie Setup

If you already know your `auth_token` and `ct0`:

1. Install bird (if not already installed): `npm install -g @steipete/bird`

2. Set environment variables:
```bash
export AUTH_TOKEN="your_auth_token"
export CT0="your_ct0"
```

3. Test:
```bash
bird check
bird search "test query"
```

## Proxy Configuration

> bird CLI supports proxies via environment variables:
```bash
export HTTP_PROXY="http://user:pass@ip:port"
export HTTPS_PROXY="http://user:pass@ip:port"
```

You can also use a system-wide proxy tool.
