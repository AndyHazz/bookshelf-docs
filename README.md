# Bookshelf docs

The user guide for [Bookshelf](https://github.com/AndyHazz/bookshelf.koplugin), a home screen for KOReader. Published at https://andyhazz.github.io/bookshelf-docs/.

Built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/). Pushing to `main` publishes the site via GitHub Actions.

## Working on it

```sh
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/mkdocs serve        # http://127.0.0.1:8000/bookshelf-docs/
```

Pages are Markdown in `docs/`. A few shortcodes, handled by `hooks/clips.py`:

| Line | Becomes |
|------|---------|
| `!clip name \| alt text` | `docs/clips/name.mp4` in an e-reader frame, looping while on screen |
| `!still name \| caption` | `docs/stills/name.jpg` (or .png/.webp) in the same frame |
| `!plank oak plant cactus` | a shelf plank divider, with ornaments standing on it |
| `!timbers cherry ebony` | labelled plank swatches |
| `**Bookshelf > Settings**` | a breadcrumb of pills |

A clip or still that doesn't exist yet builds as a grey placeholder and a warning (the CI build is `--strict`, so it fails until the file is there).

The clips and stills are recordings of the real plugin, made on a scripted headless KOReader with a public domain library from Standard Ebooks.

## Licence

Text, images and videos are [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), except artwork from the paid theme packs, which is all rights reserved. See [LICENSE.md](LICENSE.md) for the details.
