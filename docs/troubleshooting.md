# Troubleshooting Common Issues

## Twitter/X: bird CLI connection failure

**Symptom:** `bird search` or other commands return an error

**Cause:** bird CLI requires AUTH_TOKEN and CT0 environment variables to access the Twitter API. If your network environment needs a proxy to reach x.com, you need to configure one.

**Solutions:**

### Option 1: Set proxy environment variables

```bash
export HTTP_PROXY="http://user:pass@host:port"
export HTTPS_PROXY="http://user:pass@host:port"
bird search "test" -n 1
```

### Option 2: Use a system-wide proxy tool

Let a proxy tool handle all network traffic so bird requests go through it too:

```bash
# macOS — ClashX / Surge with "Enhanced Mode" enabled
# Linux — proxychains or tun2socks
proxychains bird search "test" -n 1
```

### Option 3: Use Exa search as a fallback instead of bird

When bird is unavailable, use Exa to search Twitter content directly:

```bash
mcporter call 'exa.web_search_exa(query: "site:x.com search_term", numResults: 5)'
```

### Option 4: Check authentication

```bash
bird check
```

> If it returns "Missing credentials", you need to set the AUTH_TOKEN and CT0 environment variables.
