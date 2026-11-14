---
description: Link books to Hardcover for ratings, reviews, descriptions, genres and covers, through a sync plugin or an API key of Bookshelf's own.
---

# Hardcover

[Hardcover](https://hardcover.app) is a free site for tracking what you read. Bookshelf can link your books to it and show its ratings, reviews, descriptions, genres and covers.

## Connect

Bookshelf reaches Hardcover in either of two ways:

- **A Hardcover sync plugin.** If you use the [Hardcover plugin for KOReader](https://github.com/Billiam/hardcoverapp.koplugin) or ShelfSync and are signed in there, Bookshelf uses that connection. Restart KOReader after installing one.
- **An API key of its own.** No sync plugin needed. Get a key at [hardcover.app/account/api](https://hardcover.app/account/api), then tap **Bookshelf > Hardcover enrichment > Hardcover API key**.

The **Hardcover API key** dialog says where the key in use comes from, and offers:

- **Enter key…** to paste or type it. A key is long, so **Read key from file** may be easier: save it in a text file at the path the dialog shows, and Bookshelf reads it, keeps it on the device and removes the file.
- **Copy the key from** your sync plugin, when that plugin already holds one. Only needed if you want Hardcover to keep working without the plugin; otherwise its key is used as it is.
- **Check key** asks Hardcover whether it accepts the key.
- **Remove Bookshelf's key**, once it has one.

The first line of **Hardcover enrichment** says how you're connected, such as **Connected through Bookshelf (API key)**, or **Not connected to Hardcover**. The rows that need Hardcover are greyed out until you are. A sync plugin that signs in without an API key can link books and fetch ratings, but Hardcover doesn't show other readers' reviews to that kind of sign-in; add an API key to see them.

If you stop using Hardcover, your books go back to their own details; nothing is lost.

## Link a book

Long-press the book and tap **Hardcover link** on the Edit tab. The Hardcover menu says what the book is linked to, if anything. A linked book also has a grey **Hardcover linked to: *book*** line under its cards, which opens the same menu. With no connection set up, the menu says what Hardcover is and how to connect, with **Hardcover API key…**.

Under **Link to Hardcover** (or **Change link**, once linked):

- **Auto link** uses an ISBN or Hardcover ID inside the book. Without one it reads **Auto link (best guess)** and searches by title and author.
- **Manual link…** searches Hardcover and lets you pick, with covers two to a row.
- **Select edition…** chooses the right edition, for the right cover and page count.
- **Clear link** unlinks it.

Once a book is linked, **Use Hardcover's** has two switches for that book: **Cover** and **Description**, each **On** or **Off**. **Cover** shows only when Hardcover's cover has been downloaded.

## Link everything

**Bookshelf > Hardcover enrichment > Auto-link all books** links every unlinked book in one go:

- **Exact match (ISBN / Hardcover id)** uses ISBNs and Hardcover IDs only. Fast, and sure.
- **Best guess (title & author)** searches by title and author. Slower, and finds more.

It runs in the background while you carry on using your device, about one book every two or three seconds to stay inside Hardcover's limits. Progress shows in the status line, with **Stop**. It pauses while a book is open and carries on when you're back on the shelf. A report at the end says what was linked and what wasn't.

## What you can use

Under **Bookshelf > Hardcover enrichment**:

| Setting | What it does |
|---------|--------------|
| **Show Hardcover ratings** | The top panel's rating shows Hardcover's public rating instead of yours. |
| **Use Hardcover rating if no user rating** | Books you haven't rated use their Hardcover rating, in star ratings on covers, the **Rating** sort and the **Ratings** shelf. |
| **Use Hardcover metadata** | Linked books use Hardcover's title, author, series and genres, and its first-published year for `%published` and the **Published** sort. A book linked before 6.3.2 gets the year when its Hardcover details are next refreshed. |
| **Download covers from Hardcover** | Linking also fetches Hardcover's cover. |
| **Hardcover genres used** | How many of each book's Hardcover genres to use. |

Linked books get a **Reviews** tab in their [book menu](../use/book-menu.md) with Hardcover reviews, kept for reading offline. Reviews marked as spoilers stay hidden; when a book has some, tick **Include spoilers** to show them for as long as the book menu is open. **Refresh** fetches the reviews again.

## Keeping it fresh

**Manage Hardcover data** has **Refresh ratings only** (one quick request for everything), **Refresh linked book details** (slower, one book at a time), **Clear cache (keeps links)**, **Remove downloaded covers** and **Remove all Hardcover data**.

Bookshelf only contacts Hardcover when you ask it to. Normal use reads only what's already saved.
