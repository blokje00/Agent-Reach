# XiaoHongShu (Little Red Book) Setup Guide

## Feature Overview
Read and search XiaoHongShu notes. Powered by [xiaohongshu-mcp](https://github.com/xpzouying/xiaohongshu-mcp) (⭐9K+, Go, built-in Chrome browser).

## Prerequisites
- Docker (to run the xiaohongshu-mcp service)
- mcporter CLI (MCP protocol bridge tool)

## Steps the Agent Can Complete Automatically

### 1. Install mcporter
```bash
npm install -g mcporter
```

### 2. Start the xiaohongshu-mcp service
```bash
docker run -d \
  --name xiaohongshu-mcp \
  -p 18060:18060 \
  xpzouying/xiaohongshu-mcp
```

> If a proxy is needed (recommended for server deployments):
> ```bash
> docker run -d \
>   --name xiaohongshu-mcp \
>   -p 18060:18060 \
>   -e XHS_PROXY=http://user:pass@ip:port \
>   xpzouying/xiaohongshu-mcp
> ```

### 3. Register with mcporter
```bash
mcporter config add xiaohongshu http://localhost:18060/mcp
```

### 4. Verify
```bash
agent-reach doctor
```

You should see XiaoHongShu showing ✅ or ⚠️ (MCP connected but not logged in).

## Steps Requiring Manual User Action

If doctor shows "MCP connected but not logged in":

> XiaoHongShu requires a one-time login (the session is remembered afterwards).
>
> Open http://localhost:18060 and scan the QR code with the XiaoHongShu mobile app to log in.
> After login, cookies are automatically saved inside the Docker container and remain valid for about 1–3 months.

## FAQ

**Q: Cookies lost after Docker container restart?**
A: Mount a data volume for persistence:
```bash
docker run -d \
  --name xiaohongshu-mcp \
  -p 18060:18060 \
  -v xhs-data:/app/data \
  xpzouying/xiaohongshu-mcp
```

**Q: XiaoHongShu shows IP risk on a server?**
A: Add the proxy parameter `-e XHS_PROXY=http://user:pass@ip:port`. Residential proxies are recommended.

**Q: Docker image doesn't support ARM64 / Apple Silicon?**
A: The upstream image does not yet have an ARM64 build. Two options:

Option 1: Use Rosetta emulation (recommended, simplest)
```bash
docker run -d \
  --name xiaohongshu-mcp \
  -p 18060:18060 \
  --platform linux/amd64 \
  xpzouying/xiaohongshu-mcp
```

Option 2: Build a native ARM64 image from source
```bash
git clone https://github.com/xpzouying/xiaohongshu-mcp
cd xiaohongshu-mcp
docker build -t xiaohongshu-mcp .
docker run -d --name xiaohongshu-mcp -p 18060:18060 xiaohongshu-mcp
```

**Q: I don't want to use Docker?**
A: You can compile from source: https://github.com/xpzouying/xiaohongshu-mcp
