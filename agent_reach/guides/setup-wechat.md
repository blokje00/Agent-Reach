# WeChat Official Account Setup Guide

## Feature Overview
Read WeChat Official Account articles. Requires Playwright to handle WeChat's anti-bot mechanisms.

## Steps the Agent Can Complete Automatically

1. Check if Playwright is installed:
```bash
python -c "import playwright; print('ok')"
```

2. Install Playwright + browser:
```bash
pip install playwright
playwright install chromium
```

3. Test after installation:
```bash
curl -s "https://r.jina.ai/https://mp.weixin.qq.com/s/a_test_link" -H "Accept: text/markdown"
```

## Steps Requiring Manual User Action

Tell the user:

> WeChat Official Account setup is simple — it just requires installing a browser component (~150 MB).
>
> I'll handle the installation for you; you don't need to do anything. The process takes about 1–2 minutes.
>
> After installation you can read WeChat Official Account articles directly, no login required.

## Agent Workflow

1. Install Playwright: `pip install playwright`
2. Install Chromium: `playwright install chromium`
3. Test: read a WeChat article
4. Report back: "✅ WeChat Official Accounts configured! Send me any official account article link and I can read it."
5. If installation fails (insufficient disk space, etc.): "❌ Browser component installation failed. This may be due to insufficient disk space (~150 MB required)."
