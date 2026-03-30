# -*- coding: utf-8 -*-
"""WeChat Official Account articles — read and search.

Read:   wechat-article-for-ai (Camoufox stealth browser)
Search: miku_ai (Sogou WeChat search)
"""

import shutil
import subprocess
from .base import Channel


class WeChatChannel(Channel):
    name = "wechat"
    description = "WeChat Official Account articles"
    backends = ["wechat-article-for-ai (Camoufox)", "miku_ai (Sogou Search)"]
    tier = 2

    def can_handle(self, url: str) -> bool:
        from urllib.parse import urlparse
        d = urlparse(url).netloc.lower()
        return "mp.weixin.qq.com" in d or "weixin.qq.com" in d

    def check(self, config=None):
        has_read = False
        has_search = False

        try:
            import camoufox  # noqa: F401
            has_read = True
        except ImportError:
            pass

        try:
            import miku_ai  # noqa: F401
            has_search = True
        except ImportError:
            pass

        if has_read and has_search:
            return "ok", "Fully available (search + read official account articles)"
        elif has_read:
            return "ok", "Can read official account articles (URL → Markdown). Install miku_ai to unlock search: pip install miku_ai"
        elif has_search:
            return "warn", (
                "Can search official account articles but cannot read full text. Install reading tool:\n"
                "  pip install camoufox[geoip] markdownify beautifulsoup4 httpx mcp"
            )
        else:
            return "off", (
                "WeChat Official Account tools need to be installed:\n"
                "  # Reading (URL → Markdown):\n"
                "  pip install camoufox[geoip] markdownify beautifulsoup4 httpx mcp\n"
                "  # Search (keyword → article list):\n"
                "  pip install miku_ai\n"
                "  See https://github.com/bzd6661/wechat-article-for-ai"
            )
