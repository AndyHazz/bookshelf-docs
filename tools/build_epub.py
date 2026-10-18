#!/usr/bin/env python3
"""build_epub.py <built-site-dir> <out.epub>

The user guide as an EPUB, from the built site (so the shortcodes are already
rendered): one chapter per page in nav order. A clip becomes its poster frame
with its title and the step list a screen reader gets; decoration (planks,
buttons, icons, light/dark duplicates) is dropped. Images stay in COLOUR
(plenty of readers have colour screens): they are made smaller, not grey.
Needs Calibre's ebook-convert, BeautifulSoup and Pillow.
"""
import io, re, subprocess, sys, tempfile
from pathlib import Path
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
from PIL import Image
from mkdocs.config import load_config

site, out = Path(sys.argv[1]), Path(sys.argv[2])
cfg = load_config(str(Path(__file__).resolve().parent.parent / "mkdocs.yml"))

def walk(nav):
    for item in nav:
        if isinstance(item, str): yield item
        elif isinstance(item, dict):
            for v in item.values():
                yield from (walk(v) if isinstance(v, list) else [v])

pages = list(walk(cfg["nav"]))
url_of = lambda md: "" if md == "index.md" else (md[:-3].removesuffix("/index") + "/").removeprefix("./")
anchor_of = lambda url: "p-" + (url.strip("/").replace("/", "-") or "home")

work = Path(tempfile.mkdtemp()); (work / "img").mkdir()
seen_img = {}

def image(src_abs):
    """copy a site image into the book as a modest JPEG; returns its book path"""
    if src_abs in seen_img: return seen_img[src_abs]
    p = site / src_abs.lstrip("/")
    if not p.exists(): return None
    im = Image.open(p).convert("RGB")
    # a screen shot was cropped at 2x: half its width is its true size on a
    # page; nothing needs more than 640 px on an e-reader
    w = min(im.width, 640, max(im.width // 2, 320)) if "/shots/" in src_abs else min(im.width, 640)
    if w < im.width: im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
    name = f"img/{len(seen_img):04d}.jpg"
    im.save(work / name, quality=70, optimize=True, progressive=False)
    seen_img[src_abs] = name
    return name

body = []
for md in pages:
    url = url_of(md)
    html_path = site / url / "index.html"
    if not html_path.exists(): continue
    soup = BeautifulSoup(html_path.read_text(encoding="utf-8"), "html.parser")
    art = soup.select_one("article.md-content__inner")
    if not art: continue
    for sel in [".headerlink", ".plank", ".timbers", ".clip-ctl", ".clip-zoom", "script", "style",
                "img[src*='#only-dark']", ".md-source-file", ".md-content__button", "a.md-button",
                ".twemoji", ".lg", "hr", ".bs-hero .tag", ".epub-download"]:
        for e in art.select(sel): e.decompose()
    # a clip: its poster frame, its title, and its steps as a visible list
    for fig in art.select("figure.clip"):
        v = fig.find("video")
        if not v: continue
        img = soup.new_tag("img", src=v.get("poster", ""), alt=v.get("aria-label", ""))
        v.replace_with(img)
        for sr in fig.select(".bs-sr"): sr["class"] = ["steps"]
    for e in art.select("[class]"):
        if e.name == "img": continue
    # images: resolve against the page, convert, point at the copy
    page_url = "/" + url
    for im in art.find_all("img"):
        src = im.get("src", "").split("#")[0]
        if not src or src.startswith("http"): im.decompose(); continue
        new = image(urlparse(urljoin(page_url, src)).path)
        if new: im["src"] = new
        else: im.decompose()
        for a in ("width", "height", "loading", "style"): im.attrs.pop(a, None)
    # links: to another page of the guide becomes a jump inside the book
    for a in art.find_all("a", href=True):
        h = a["href"]
        if h.startswith(("http", "mailto:")): continue
        target = urlparse(urljoin(page_url, h))
        frag = target.fragment
        a["href"] = "#" + (frag if frag else anchor_of(target.path.lstrip("/")))
    h1 = art.find("h1")
    if h1: h1["id"] = anchor_of(url)
    body.append(f'<section class="chapter">{art.decode_contents()}</section>')

css = """
body { font-family: serif; }
h1 { page-break-before: always; }
section.chapter:first-child h1 { page-break-before: auto; }
img { max-width: 100%; height: auto; }
figure { margin: 1em 0; text-align: center; }
figcaption { font-size: .9em; font-style: italic; }
.steps { font-size: .9em; text-align: left; }
.crumbs .sep { padding: 0 .2em; }
table { border-collapse: collapse; } td, th { border: 1px solid #999; padding: .2em .4em; vertical-align: top; }
"""
html = (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Bookshelf user guide</title>'
        f'<style>{css}</style></head><body>{"".join(body)}</body></html>')
(work / "guide.html").write_text(html, encoding="utf-8")
cover = image("/assets/social.png")
subprocess.run(["ebook-convert", str(work / "guide.html"), str(out),
                "--title", "Bookshelf user guide", "--authors", "AndyHazz",
                "--language", "en", "--cover", str(work / cover),
                "--level1-toc", "//h:h1", "--level2-toc", "//h:h2",
                "--chapter", "//h:h1", "--page-breaks-before", "//h:h1",
                "--no-default-epub-cover", "--epub-version", "3"],
               check=True, stdout=subprocess.DEVNULL)
print(f"{out}: {out.stat().st_size // 1024} kB, {len(body)} chapters, {len(seen_img)} images")
