"""Bake the GitHub badge's numbers (latest release, stars, forks) into the site.

Material fetches them from api.github.com in every visitor's browser, which
GitHub limits to 60 requests an hour per connection, unauthenticated; past
that, the badge falls back to a plain logo. Fetched once per build here
(authenticated in CI via GITHUB_TOKEN) and pre-filled into the session cache
Material reads first (overrides/main.html). A failed fetch leaves it empty,
and Material fetches as before.

Kept in .cache/repo_facts.json for an hour: `mkdocs serve` rebuilds on every
file change, and fetching on each one ran into GitHub's 60-an-hour limit and
held every rebuild up on the request. Within the hour the kept facts are
used; past it they are fetched again, and kept facts of any age stand in when
a fetch fails. CI starts with no cache, so it always fetches.
"""
import json
import logging
import os
import re
import time
import urllib.request

TTL = 3600

log = logging.getLogger("mkdocs.hooks.repo_facts")


def _get(url):
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json",
                                               "User-Agent": "bookshelf-docs-build"})
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=10) as r:
        return json.load(r)


def _cache_path(config):
    root = os.path.dirname(os.path.abspath(config.config_file_path or "mkdocs.yml"))
    return os.path.join(root, ".cache", "repo_facts.json")


def _read_cache(path):
    try:
        with open(path) as f:
            kept = json.load(f)
        return kept.get("facts") or {}, float(kept.get("at") or 0)
    except Exception:
        return {}, 0


def _write_cache(path, facts):
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as f:
            json.dump({"at": time.time(), "facts": facts}, f)
    except Exception as e:
        log.info("repo facts not kept (%s)", e)


def on_config(config):
    m = re.match(r"https://github\.com/([^/]+)/([^/]+?)/?$", config.get("repo_url") or "")
    if not m:
        return config
    path = _cache_path(config)
    kept, at = _read_cache(path)
    complete = lambda f: {"stars", "forks", "version"} <= f.keys()
    if complete(kept) and time.time() - at < TTL:
        config.extra["repo_facts"] = kept
        return config
    api = f"https://api.github.com/repos/{m[1]}/{m[2]}"
    facts = {}
    try:
        repo = _get(api)
        facts.update(stars=repo["stargazers_count"], forks=repo["forks_count"])
        facts["version"] = _get(f"{api}/releases/latest")["tag_name"]
    except Exception as e:  # offline, rate limited: the kept facts, else Material fetches live
        log.info("repo facts not fetched (%s)%s", e, "; using the kept ones" if complete(kept) else "")
    if complete(facts):
        _write_cache(path, facts)
    elif complete(kept):
        facts = kept
    config.extra["repo_facts"] = facts if complete(facts) else {}
    return config
