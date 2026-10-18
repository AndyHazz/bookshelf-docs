"""Bake the GitHub badge's numbers (latest release, stars, forks) into the site.

Material fetches them from api.github.com in every visitor's browser, which
GitHub limits to 60 requests an hour per connection, unauthenticated; past
that, the badge falls back to a plain logo. Fetched once per build here
(authenticated in CI via GITHUB_TOKEN) and pre-filled into the session cache
Material reads first (overrides/main.html). A failed fetch leaves it empty,
and Material fetches as before.
"""
import json
import logging
import os
import re
import urllib.request

log = logging.getLogger("mkdocs.hooks.repo_facts")


def _get(url):
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json",
                                               "User-Agent": "bookshelf-docs-build"})
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=10) as r:
        return json.load(r)


def on_config(config):
    m = re.match(r"https://github\.com/([^/]+)/([^/]+?)/?$", config.get("repo_url") or "")
    if not m:
        return config
    api = f"https://api.github.com/repos/{m[1]}/{m[2]}"
    facts = {}
    try:
        repo = _get(api)
        facts.update(stars=repo["stargazers_count"], forks=repo["forks_count"])
        facts["version"] = _get(f"{api}/releases/latest")["tag_name"]
    except Exception as e:  # offline, rate limited: Material fetches it live instead
        log.info("repo facts not fetched (%s)", e)
    config.extra["repo_facts"] = facts if {"stars", "forks", "version"} <= facts.keys() else {}
    return config
