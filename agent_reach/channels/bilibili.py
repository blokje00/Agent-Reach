# -*- coding: utf-8 -*-
"""Bilibili — video via yt-dlp, search via /x/web-interface API."""

import json
import os
import shutil
import subprocess
import urllib.request
from .base import Channel

_UA = "agent-reach/1.0"
_TIMEOUT = 10
_SEARCH_API = "https://api.bilibili.com/x/web-interface/search/all/v2?keyword=test&page=1"


def _search_api_ok() -> bool:
    """Return True if Bilibili search API responds with code 0."""
    req = urllib.request.Request(_SEARCH_API, headers={"User-Agent": _UA})
    try:
        with urllib.request.urlopen(req, timeout=_TIMEOUT) as resp:
            data = json.loads(resp.read())
            return data.get("code") == 0
    except Exception:
        return False


def _bilisearch_ok() -> bool:
    """Return True if yt-dlp bilisearch works without 412."""
    try:
        result = subprocess.run(
            ["yt-dlp", "--flat-playlist", "--no-download", "-j",
             "bilisearch1:test"],
            capture_output=True, text=True, timeout=_TIMEOUT,
        )
        return result.returncode == 0
    except Exception:
        return False


class BilibiliChannel(Channel):
    name = "bilibili"
    description = "Bilibili videos and subtitles"
    backends = ["yt-dlp", "Bilibili Search API"]
    tier = 1

    def can_handle(self, url: str) -> bool:
        from urllib.parse import urlparse
        d = urlparse(url).netloc.lower()
        return "bilibili.com" in d or "b23.tv" in d

    def check(self, config=None):
        if not shutil.which("yt-dlp"):
            return "off", "yt-dlp is not installed. Install: pip install yt-dlp"

        proxy = (config.get("bilibili_proxy") if config else None) or os.environ.get("BILIBILI_PROXY")

        # Probe search API connectivity
        api_ok = _search_api_ok()
        # Probe yt-dlp bilisearch for 412 errors
        ytdlp_search_ok = _bilisearch_ok()

        parts = []

        # Video read status
        if proxy:
            parts.append("Video reading: yt-dlp (proxy configured)")
        else:
            parts.append("Video reading: yt-dlp (local env; server may need proxy)")

        # Search status
        if api_ok:
            parts.append("Search: Bilibili API available (/x/web-interface/search/all/v2)")
        else:
            parts.append("Search: Bilibili API unreachable, search may be limited")

        if not ytdlp_search_ok:
            parts.append("Note: yt-dlp bilisearch unavailable (possible HTTP 412 anti-crawl), search will use Bilibili API")

        status = "ok" if api_ok else "warn"
        return status, ". ".join(parts)
