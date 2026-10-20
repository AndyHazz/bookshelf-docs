---
description: Link books to Hardcover for ratings, reviews, descriptions, genres and covers, using the Hardcover plugin.
---

# Hardcover

[Hardcover](https://hardcover.app) is a site for tracking what you read. If you use the [Hardcover plugin for KOReader](https://github.com/Billiam/hardcoverapp.koplugin), Bookshelf can link your books to it and show its ratings, reviews, descriptions, genres and covers.

Everything here appears only while that plugin is installed and on. Turn it off and your books go back to their own details; nothing is lost.

## Link a book

Long-press the book, open the **Edit** tab, and tap **Link…** in the **Hardcover** row:

- **Auto link** uses an ISBN or Hardcover ID inside the book, or searches by title and author if there isn't one.
- **Manual link…** searches Hardcover and lets you pick.
- **Select edition…** chooses the right edition, for the right cover and page count.
- **Use Hardcover image** and **Use Hardcover description** swap in Hardcover's for this book.
- **Clear link** unlinks it.

## Link everything

**Bookshelf > Hardcover enrichment > Auto-link all books** links every unlinked book in one go:

- **Exact match** uses ISBNs and Hardcover IDs only. Fast, and sure.
- **Best guess** searches by title and author. Slower, and finds more.

It works through about one book every two or three seconds, to stay inside Hardcover's limits, with a report at the end of what was linked and what wasn't.

## What you can use

Under **Bookshelf > Hardcover enrichment**:

| Setting | What it does |
|---------|--------------|
| **Show Hardcover ratings** | The top panel's rating shows Hardcover's public rating instead of yours. |
| **Use Hardcover rating if no user rating** | Books you haven't rated use their Hardcover rating, in star ratings on covers, the **Rating** sort and the **Ratings** shelf. |
| **Use Hardcover metadata** | Linked books use Hardcover's title, author, series and genres. |
| **Download covers from Hardcover** | Linking also fetches Hardcover's cover. |
| **Hardcover genres used** | How many of each book's Hardcover genres to use. |

Linked books get a **Reviews** tab in their [book menu](../use/book-menu.md) with spoiler-free Hardcover reviews, kept for reading offline.

## Keeping it fresh

**Manage Hardcover data** has **Refresh ratings only** (one quick request for everything), **Refresh linked book details** (slower, one book at a time), **Clear cache (keeps links)**, **Remove downloaded covers** and **Remove all Hardcover data**.

Bookshelf only contacts Hardcover when you ask it to. Normal use reads only what's already saved.
