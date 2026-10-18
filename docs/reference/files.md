---
description: Where Bookshelf keeps its settings and caches, what to back up, how to move to a new device, and how to remove it completely.
---

# Files, backup and removing

Bookshelf never changes your book files unless you ask it to (moving, renaming or deleting from a book's menu). Everything it keeps is in a few places.

## What's where

Paths are inside KOReader's folder: `koreader/` on a Kindle's USB drive, `.adds/koreader/` on a Kobo.

| Where | What | Back it up? |
|-------|------|-------------|
| `plugins/bookshelf.koplugin/` | The plugin itself. Replaced on every update. | No |
| `settings/bookshelf/settings.lua` | All your Bookshelf settings: shelves, filters, sorts, themes, colours, top panel lines, start menu. | **Yes** |
| `settings/bookshelf/micromodule_data.lua`, `hardcover_links.lua`, `hardcover.sqlite3` | Micro-module settings and data, and your Hardcover links and cached ratings. Only there once used. | **Yes** |
| `settings/bookshelf/ornaments/` | Ornaments and theme packs, and your adjustments to them (`ornaments.json`). | Yes, if you've added any |
| `settings/bookshelf/wallpapers/` | Your wallpapers. | Yes, if you've added any |
| `settings/bookshelf/micromodules/` | Micro-modules you've written or added. | Yes, if any |
| `settings/bookshelf/book_facts.sqlite3` | Page counts from [Extract page counts](../organise/page-counts.md). | Optional: it can be rebuilt |
| `cache/bookshelf/` | Caches, including scaled covers. | No: rebuilt as needed |

And outside it:

| Where | What |
|-------|------|
| `.bookshelf-images/` in your home folder | The [image library](../organise/folders.md#pictures-for-folders-and-stacks): author photos and your own pictures for stacks. Only there if you've used it. |
| `calibre.bookshelf.json` beside `metadata.calibre` | Calibre's author sort and custom columns, kept safe from wireless syncs. Only with [Calibre metadata](../organise/other-libraries.md#calibre) on. |
| `fonts/` (on a Kindle, the `fonts` folder at the top of the drive) | Copies of Bookshelf's three fonts, so KOReader's font menus can use them. |

### What belongs to KOReader

These are KOReader's own, and Bookshelf reads and writes them the same way KOReader does: reading status, progress, your rating and review (in each book's sidecar), favourites and collections, history (your Recent shelf) and reading statistics. They stay put whether or not Bookshelf is installed.

## Moving to a new device

Install Bookshelf on the new device, then copy `settings/bookshelf/` across before starting KOReader. Your shelves come with it.

Shelves that point at a **specific folder** remember that folder's full path. If your books live somewhere different on the new device, edit those shelves' sources.

## Removing Bookshelf

1. Open KOReader's menu, first tab, and set **Start with** back to **file browser** (or anything else).
2. Delete `plugins/bookshelf.koplugin/`.
3. To remove every trace, also delete `settings/bookshelf/`, `cache/bookshelf/`, and if you used them, `.bookshelf-images/` in your home folder and `calibre.bookshelf.json`.

Restart KOReader. Your books, progress, highlights and collections are untouched: they were always KOReader's.

!!! tip "Just pausing it"
    To turn Bookshelf off without deleting anything, untick it under **Tools > More tools > Plugin management** (the wrench tab), and restart.
