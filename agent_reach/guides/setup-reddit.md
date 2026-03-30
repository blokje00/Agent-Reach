# Reddit Proxy Setup Guide

## Feature Overview
Reddit blocks many server IPs; direct access returns 403. An ISP/Residential Proxy is required to read full Reddit posts and comments.

**Note:** Even without a proxy, you can find Reddit content via Exa search (just configure the Exa key). A proxy is only needed for reading complete posts and comments.

## Steps the Agent Can Complete Automatically

1. Check current status:
```bash
agent-reach doctor | grep "Reddit"
```

2. If the user has provided a proxy, test connectivity:
```bash
curl -s --proxy "user_provided_proxy" \
  -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36" \
  "https://www.reddit.com/r/test.json?limit=1" \
  -o /dev/null -w "%{http_code}"
```
Returns 200 = working, 403 = proxy blocked, other = configuration error

3. Write the configuration:
```python
from agent_reach.config import Config
c = Config()
c.set("reddit_proxy", "http://username:password@IP:port")
```

## Steps Requiring Manual User Action

Tell the user:

> To read full Reddit posts and comments, you need an ISP proxy (~$3–10/month).
>
> Recommended proxy providers (pick one):
> 1. **Smartproxy** (https://smartproxy.com) — ISP proxy, pay-as-you-go
> 2. **Bright Data** (https://brightdata.com) — Enterprise, ISP proxy
> 3. **IPRoyal** (https://iproyal.com) — Affordable, good for beginners
> 4. **ProxyEmpire** (https://proxyempire.io) — Has Reddit-specific proxies
>
> When purchasing, choose:
> - Type: **ISP Proxy** (not Datacenter — it will get blocked)
> - Region: **United States**
> - Protocol: **HTTP**
>
> After purchase you'll receive a proxy address in this format:
> `http://username:password@IP:port`
>
> Just send me that address.
>
> ⚠️ If you don't want to spend money, you can skip this. I can still find Reddit content through search engines, just without reading complete posts and comments.

## Agent Actions After Receiving a Proxy

1. Test the proxy: use curl to check if reddit.com returns 200
2. If successful, write the configuration: `config.set("reddit_proxy", proxy_url)`
3. Report back: "✅ Reddit full reading enabled! Now I can read Reddit posts and all their comments."
4. If it fails, tell the user: "❌ This proxy cannot access Reddit. Please check if the proxy is valid, or try a different one."
