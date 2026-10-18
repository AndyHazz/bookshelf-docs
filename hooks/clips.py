"""Clip shortcodes for the Bookshelf docs.

In any page:

    !clip shelf-styles | Long-press the page counter to change the style

becomes an e-reader-framed, muted, looping video (docs/clips/<name>.mp4 with
docs/clips/<name>.jpg as its poster). `!still <name> | caption` does the same
for a PNG/JPG in docs/stills/. A missing file builds as a labelled gap and a
warning, so pages can be written before their clip is recorded.

    !shot shelf-editor | The shelf editor
    !shot:side face-out-dialog | Face out

shows a cropped screenshot of the real UI (docs/shots/<name>.webp, sized from
its <name>.size sidecar: "width height scale", scale 2 = shown at half size).
`:side` floats it beside the text on wide screens; `:wide` lets it run to the
full column; `:device` puts a full-screen shot in the e-reader frame.
"""
import html
import logging
import re
from pathlib import Path

log = logging.getLogger("mkdocs.hooks.clips")
LINE = re.compile(r"^(?P<indent>[ \t]*)!(?P<kind>clip|still|shot)(?::(?P<variant>side|wide|device))?\s+(?P<name>[\w.-]+)\s*(?:\|\s*(?P<cap>.*))?$", re.M)


def on_page_markdown(markdown, page, config, files):
    docs = Path(config["docs_dir"])
    depth = page.url.count("/") if page.url else 0
    up = "../" * depth

    def sub(m):
        kind, name, cap = m["kind"], m["name"], (m["cap"] or "").strip()
        ind = m["indent"]
        # `| alt: text` gives an image its alt text with no visible caption
        alt_only = ""
        if cap.lower().startswith("alt:"):
            alt_only, cap = cap[4:].strip(), ""
        cap_html = f"<figcaption>{_inline(cap)}</figcaption>" if cap else ""
        if kind == "shot":
            img = docs / "shots" / f"{name}.webp"
            alt = html.escape(alt_only or _plain(cap) or name.replace("-", " "))
            cls = "shot" + (f" shot-{m['variant']}" if m["variant"] else "")
            if not img.exists():
                log.warning("shot %s: no %s (page %s)", name, img.name, page.file.src_path)
                return f'{ind}<figure class="{cls} missing"><p>shot: {html.escape(name)}</p>{cap_html}</figure>'
            size = docs / "shots" / f"{name}.size"
            dims = ""
            if size.exists():
                w, h, sc = size.read_text().split()
                dims = f' width="{round(int(w) / float(sc))}" height="{round(int(h) / float(sc))}"'
            if m["variant"] == "device":
                # a full-screen shot, in the same e-reader frame as the clips
                return (f'{ind}<figure class="clip still"><div class="bezel">'
                        f'<img src="{up}shots/{name}.webp" alt="{alt}" loading="lazy"></div>{cap_html}</figure>')
            return (f'{ind}<figure class="{cls}"><img src="{up}shots/{name}.webp" alt="{alt}"{dims} loading="lazy">'
                    f'{cap_html}</figure>')
        if kind == "clip":
            mp4 = docs / "clips" / f"{name}.mp4"
            if not mp4.exists():
                log.warning("clip %s: no %s (page %s)", name, mp4.name, page.file.src_path)
                return f'{ind}<figure class="clip missing"><div class="bezel"><p>clip: {html.escape(name)}</p></div>{cap_html}</figure>'
            ratio = ""
            meta = docs / "clips" / f"{name}.ratio"
            if meta.exists():
                ratio = f' style="--clip-ratio: {meta.read_text().strip()}"'
            alt = html.escape(alt_only or _plain(cap) or name.replace("-", " "))
            # The caption names what the clip is about, so a reader can tell
            # several clips apart at a glance (the burned-in captions explain
            # each step as it plays). The clips are silent, so the burned-in
            # captions (docs/clips/<name>.captions, one per line, written by
            # the rig's docs_clip.sh) also go in as text for screen readers:
            # the text alternative a video-only clip needs (WCAG 1.2.1).
            steps = ""
            capfile = docs / "clips" / f"{name}.captions"
            if capfile.exists():
                lines = [l.strip() for l in capfile.read_text(encoding="utf-8").splitlines() if l.strip()]
                if lines:
                    items = "".join(f"<li>{html.escape(l, quote=False)}</li>" for l in lines)
                    steps = f'<div class="bs-sr"><p>What the clip shows, step by step:</p><ol>{items}</ol></div>'
            # The caption is a bold title under the clip, so a reader can tell
            # several clips apart at a glance before any of them plays.
            title = f'<figcaption class="clip-title">{_inline(cap)}</figcaption>' if cap else ""
            return (f'{ind}<figure class="clip"{ratio}><div class="bezel">'
                    f'<video src="{up}clips/{name}.mp4" poster="{up}clips/{name}.jpg" muted loop playsinline preload="none" '
                    f'aria-label="{alt}"></video>{steps}</div>{title}</figure>')
        for ext in ("png", "jpg", "webp"):
            img = docs / "stills" / f"{name}.{ext}"
            if img.exists():
                alt = html.escape(alt_only or _plain(cap) or name.replace("-", " "))
                return (f'{ind}<figure class="clip still"><div class="bezel">'
                        f'<img src="{up}stills/{name}.{ext}" alt="{alt}" loading="lazy"></div>{cap_html}</figure>')
        log.warning("still %s: no image (page %s)", name, page.file.src_path)
        return f'{ind}<figure class="clip missing"><div class="bezel"><p>still: {html.escape(name)}</p></div>{cap_html}</figure>'

    markdown = LINE.sub(sub, markdown)

    def plank(m):
        timber, extras = m["timber"], (m["extra"] or "").split()
        base = f"{up}assets/ui/planks/{timber}"
        orns = ""
        for i, orn in enumerate(extras):
            side = "left" if i == 0 and len(extras) > 1 else "right"
            orns += f'<img class="orn orn-{side}" src="{up}assets/ui/{orn}.svg" alt="" aria-hidden="true">'
        # as the plugin draws it: the middle runs the full width and the
        # ends are laid over it (their inner edges fade into the middle)
        cls = "plank has-orn" if orns else "plank"
        return (f'{m["indent"]}<div class="{cls}" aria-hidden="true" style="background-image:url({base}-middle.png)">{orns}'
                f'<img class="pl-l" src="{base}-left.png" alt="">'
                f'<img class="pl-r" src="{base}-right.png" alt=""></div>')

    markdown = PLANK.sub(plank, markdown)

    def timbers(m):
        cells = ""
        for timber in m["names"].split():
            base = f"{up}assets/ui/planks/{timber}"
            cells += (f'<div class="timber"><div class="plank" style="background-image:url({base}-middle.png)">'
                      f'<img class="pl-l" src="{base}-left.png" alt=""><img class="pl-r" src="{base}-right.png" alt="">'
                      f'</div><span class="tag">{html.escape(timber.capitalize())}</span></div>')
        return f'{m["indent"]}<div class="timbers">{cells}</div>'

    markdown = TIMBERS.sub(timbers, markdown)

    return crumbs(markdown)


# `!plank oak` or `!plank walnut cactus plant`: a shelf divider drawn from the
# real plank images, with the starter ornaments standing on it.
PLANK = re.compile(r"^(?P<indent>[ \t]*)!plank\s+(?P<timber>[\w-]+)(?P<extra>(?:\s+[\w-]+)*)\s*$", re.M)

# `!timbers cherry ebony maple`: labelled plank swatches in a grid
TIMBERS = re.compile(r"^(?P<indent>[ \t]*)!timbers\s+(?P<names>[\w -]+?)\s*$", re.M)

# **Bookshelf > Settings > Behavior** reads as the plugin's own breadcrumb:
# a row of pills. Fenced code is left alone.
PATH = re.compile(r"\*\*([^*\n<>`]+?(?: &gt; | > )[^*\n<`]+?)\*\*")
FENCE = re.compile(r"^(```|~~~)")


def crumbs(markdown):
    out, in_fence = [], False
    for line in markdown.split("\n"):
        if FENCE.match(line.strip()):
            in_fence = not in_fence
        if not in_fence and "**" in line and ">" in line:
            line = PATH.sub(_crumb, line)
        out.append(line)
    return "\n".join(out)


def _crumb(m):
    parts = [p.strip() for p in re.split(r" > | &gt; ", m[1]) if p.strip()]
    # The arrow is drawn; a screen reader hears " > " between the steps, as
    # the menu path is written elsewhere. No title: it only repeated the
    # visible text, as a tooltip that covered the next line.
    pills = '<span class="sep" aria-hidden="true">›</span><span class="bs-sr"> &gt; </span>'.join(
        f'<span class="pill">{html.escape(p, quote=False)}</span>' for p in parts)
    return f'<span class="crumbs">{pills}</span>'


def _inline(text):
    """**bold** and *italic* in a caption (it is raw HTML, so Markdown never sees it)."""
    out = html.escape(text, quote=False)
    out = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", out)
    return re.sub(r"\*(.+?)\*", r"<em>\1</em>", out)


def _plain(text):
    return re.sub(r"\*+", "", text)
