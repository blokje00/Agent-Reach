# -*- coding: utf-8 -*-
"""Twitter/X — check if bird CLI (@steipete/bird) is available."""

import shutil
import subprocess
from .base import Channel


class TwitterChannel(Channel):
    name = "twitter"
    description = "Twitter/X tweets"
    backends = ["bird CLI"]
    tier = 1

    def can_handle(self, url: str) -> bool:
        from urllib.parse import urlparse
        d = urlparse(url).netloc.lower()
        return "x.com" in d or "twitter.com" in d

    def check(self, config=None):
        bird = shutil.which("bird") or shutil.which("birdx")
        if not bird:
            return "warn", (
                "bird CLI is not installed. Search is available via Exa as fallback. Install:\n"
                "  npm install -g @steipete/bird"
            )

        try:
            r = subprocess.run(
                [bird, "check"], capture_output=True,
                encoding="utf-8", errors="replace", timeout=10
            )
            output = (r.stdout or "") + (r.stderr or "")
            if r.returncode == 0:
                return "ok", "Fully available (read and search tweets, including long posts/X Articles)"
            # bird check returns 1 when auth is missing
            if "Missing credentials" in output or "missing" in output.lower():
                return "warn", (
                    "bird CLI is installed but authentication is not configured. Set environment variables:\n"
                    "  export AUTH_TOKEN=\"xxx\"\n"
                    "  export CT0=\"yyy\"\n"
                    "or run:\n"
                    "  agent-reach configure twitter-cookies \"auth_token=xxx; ct0=yyy\""
                )
            return "warn", (
                "bird CLI is installed but authentication check failed. Run:\n"
                "  agent-reach configure twitter-cookies \"auth_token=xxx; ct0=yyy\""
            )
        except Exception:
            return "warn", "bird CLI is installed but connection failed"
