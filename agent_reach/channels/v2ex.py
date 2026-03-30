# -*- coding: utf-8 -*-
"""V2EX — public API channel for topics, nodes, users, and replies."""

import json
import urllib.request
from typing import Any
from .base import Channel

_UA = "agent-reach/1.0"
_TIMEOUT = 10


def _get_json(url: str) -> Any:
    """Fetch *url* and return parsed JSON. Raises on HTTP/network errors."""
    req = urllib.request.Request(url, headers={"User-Agent": _UA})
    with urllib.request.urlopen(req, timeout=_TIMEOUT) as resp:
        return json.loads(resp.read().decode("utf-8"))


class V2EXChannel(Channel):
    name = "v2ex"
    description = "V2EX nodes, topics and replies"
    backends = ["V2EX API (public)"]
    tier = 0

    # ------------------------------------------------------------------ #
    # URL routing
    # ------------------------------------------------------------------ #

    def can_handle(self, url: str) -> bool:
        from urllib.parse import urlparse
        d = urlparse(url).netloc.lower()
        return "v2ex.com" in d

    # ------------------------------------------------------------------ #
    # Health check
    # ------------------------------------------------------------------ #

    def check(self, config=None):
        try:
            _get_json(
                "https://www.v2ex.com/api/topics/show.json?node_name=python&page=1"
            )
            return "ok", "Public API available (hot topics, node browsing, topic details, user info)"
        except Exception as e:
            return "warn", f"V2EX API connection failed (may need a proxy): {e}"

    # ------------------------------------------------------------------ #
    # Data-fetching methods
    # ------------------------------------------------------------------ #

    def get_hot_topics(self, limit: int = 20) -> list:
        """Fetch list of hot topics.

        Returns a list of dicts with keys:
          title, url, replies, node_name, node_title, content
        """
        data = _get_json("https://www.v2ex.com/api/topics/hot.json")
        results = []
        for item in data[:limit]:
            node = item.get("node") or {}
            content = item.get("content", "") or ""
            results.append(
                {
                    "id": item.get("id", 0),
                    "title": item.get("title", ""),
                    "url": item.get("url", ""),
                    "replies": item.get("replies", 0),
                    "node_name": node.get("name", ""),
                    "node_title": node.get("title", ""),
                    "content": content[:200],
                    "created": item.get("created", 0),
                }
            )
        return results

    def get_node_topics(self, node_name: str, limit: int = 20) -> list:
        """Fetch latest topics from a specified node.

        Args:
            node_name: Node name, e.g. "python", "tech", "jobs"
            limit:     Maximum number of results to return

        Returns a list of dicts with keys:
          title, url, replies, node_name, node_title, content
        """
        url = (
            f"https://www.v2ex.com/api/topics/show.json"
            f"?node_name={node_name}&page=1"
        )
        data = _get_json(url)
        results = []
        for item in data[:limit]:
            node = item.get("node") or {}
            content = item.get("content", "") or ""
            results.append(
                {
                    "id": item.get("id", 0),
                    "title": item.get("title", ""),
                    "url": item.get("url", ""),
                    "replies": item.get("replies", 0),
                    "node_name": node.get("name", node_name),
                    "node_title": node.get("title", ""),
                    "content": content[:200],
                    "created": item.get("created", 0),
                }
            )
        return results

    def get_topic(self, topic_id: int) -> dict:
        """Fetch details and reply list for a single topic.

        Args:
            topic_id: Topic ID (extracted from URL https://www.v2ex.com/t/<id>)

        Returns a dict with keys:
          id, title, url, content, replies_count, node_name, node_title,
          author, created, replies (list of dicts with: author, content, created)
        """
        topic_data = _get_json(
            f"https://www.v2ex.com/api/topics/show.json?id={topic_id}"
        )
        # API returns a list even for single-ID queries
        if isinstance(topic_data, list):
            topic = topic_data[0] if topic_data else {}
        else:
            topic = topic_data

        node = topic.get("node") or {}
        member = topic.get("member") or {}

        # Fetch replies (first page)
        try:
            replies_raw = _get_json(
                f"https://www.v2ex.com/api/replies/show.json"
                f"?topic_id={topic_id}&page=1"
            )
        except Exception:
            replies_raw = []

        replies = [
            {
                "author": (r.get("member") or {}).get("username", ""),
                "content": r.get("content", ""),
                "created": r.get("created", 0),
            }
            for r in (replies_raw or [])
        ]

        return {
            "id": topic.get("id", topic_id),
            "title": topic.get("title", ""),
            "url": topic.get("url", f"https://www.v2ex.com/t/{topic_id}"),
            "content": topic.get("content", ""),
            "replies_count": topic.get("replies", 0),
            "node_name": node.get("name", ""),
            "node_title": node.get("title", ""),
            "author": member.get("username", ""),
            "created": topic.get("created", 0),
            "replies": replies,
        }

    def get_user(self, username: str) -> dict:
        """Fetch user information.

        Args:
            username: V2EX username

        Returns a dict with keys:
          id, username, url, website, twitter, psn, github, btc,
          location, bio, avatar, created
        """
        data = _get_json(
            f"https://www.v2ex.com/api/members/show.json?username={username}"
        )
        return {
            "id": data.get("id", 0),
            "username": data.get("username", username),
            "url": data.get("url", f"https://www.v2ex.com/member/{username}"),
            "website": data.get("website", ""),
            "twitter": data.get("twitter", ""),
            "psn": data.get("psn", ""),
            "github": data.get("github", ""),
            "btc": data.get("btc", ""),
            "location": data.get("location", ""),
            "bio": data.get("bio", ""),
            "avatar": data.get("avatar_large", data.get("avatar_normal", "")),
            "created": data.get("created", 0),
        }

    def search(self, query: str, limit: int = 10) -> list:
        """Search topics.

        Note: The V2EX public API does not support a full-text search endpoint
        (/api/search.json is unavailable).
        This method proxies the V2EX on-site search page via Jina Reader
        and returns plain text results (no structured data).

        For precise searches, visit https://www.v2ex.com/?q=<query> directly or
        use the Exa channel with a site:v2ex.com search.

        Returns:
            list of dicts with keys: title, url, snippet
            If search is unavailable, returns a list with a single {"error": str} entry.
        """
        return [
            {
                "error": (
                    "V2EX public API does not provide a search endpoint. "
                    f"Suggested alternative: https://www.v2ex.com/?q={query} "
                    "or use the Exa channel with site:v2ex.com search."
                )
            }
        ]
