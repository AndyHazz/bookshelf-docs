---
description: Long-press a book for its tabbed menu - status, favourites, ratings, collections, covers, moving and deleting - and work with many books at once.
---

# Opening and managing books

## Opening a book

<div class="walk" markdown>

<div markdown>

- **Tap a book** to preview it in the top panel. **Tap it again**, or tap the top panel's cover, to open it.
- On a full screen shelf, one tap opens it. (You can change this under **Bookshelf > Settings > Behavior > Tap a book in full screen shelves**.)

When you're done reading, go back to KOReader's file browser in the usual way (the folder icon in the reader's top menu) and you land on your shelf, straight away.

</div>

!clip open-book | Tap once to preview, again to open, and back to the shelf.

</div>

## The book menu

<div class="walk" markdown>

<div markdown>

**Long-press any book**, on the shelf or in the top panel, for its menu. It opens on the **Edit** tab. Across the top are the cover, title and author. Along the bottom: **Open**, two buttons for text size, and **Close**.

The tabs:

<div class="shots" markdown>

!shot book-menu-description | Description

!shot book-menu-tags | Tags

!shot book-menu-cover | Cover

</div>

Description
:   The blurb.

My review
:   Your own review of the book, the same one KOReader's book status page keeps. With [Hardcover](../organise/hardcover.md) linked, this tab is **Reviews**, with **My review** and **Hardcover** to switch between. Hardcover's reviews load when you tap **Refresh**, and leave out spoilers unless you tick **Include spoilers** (it's offered only when there are some, and starts unticked each time).

Highlights
:   The book's highlights, notes and bookmarks, in book order, without opening it. Only for books that have some. Each row shows the same icon KOReader's own list uses, in the highlight's colour on a colour screen. Tap one for its chapter, page and date, the whole text and your note, and **View in book** to open the book right there. The list follows the menu's text size buttons.

Tags
:   The book's author, series, collections, genres and folder, as pills. Tap a pill to open that shelf. **Edit**, at the top, puts a cross on each tag you can take off and **+ Add** at the end of each section you can add to, which is where you add the book to collections or change its genres. **Done** finishes.

Edit
:   What you can do with the book (below).

Cover
:   Choose a different cover: one already stored, an image from your device (**Choose from device**), or an online search (**Search online…**). Tapping the book's own cover puts it back.

</div>

!clip book-menu | Long-press a book: favourite, finished, and into a collection.

!clip highlights | The Highlights tab, and one highlight in full.

</div>

### The Edit tab

!shot:side book-menu-edit | The Edit tab

**Reading status**
:   **Unopened**, **Reading**, **On hold** or **Finished**. Unopened clears progress and drops the book from Recent, without touching highlights or bookmarks.

**Your rating**, **Hardcover** and **Publish date**
:   Side by side under the reading status. **Your rating**: tap a star to rate. To clear it, tap your current rating again, or long-press the stars and confirm **Clear your rating?**. With Hardcover linked, its rating is next, the number in the heading; tap its stars for Hardcover's reviews.

    **Publish date** is the date `%published` and the **Published** sort use, with where it came from underneath: **from the file**, **from calibre**, **from the catalog**, **from Hardcover** or **set by you**. Many ebooks carry the date the ebook was made rather than when the book was first published, so check it before trusting it. Tap the date to pick another in a date picker; once you have set one, the picker's **Use the book's date (…)** goes back to the book's own. **Set date** shows when there is none: **Checking the file…** while Bookshelf reads it (it fills in by itself), or **None in the file**.

    On a small screen or with large text, the ratings stack and the publish date gets a row of its own below the actions.

**Actions**
:   A card for each thing you can do with the book:

| Card | What it does |
|------|--------------|
| **Favorite** | In or out of your favourites. The card is filled while it's a favourite. |
| **Remove from history** | Off the Recent shelf, nothing else changed. |
| **Show info** | KOReader's book information. |
| **Select** | Start a [selection](#many-books-at-once) with this book in it. |
| **Refresh metadata** | Re-read the cover and details from the file, after editing them elsewhere. |
| **Move…** | Move the file to another folder. Progress, highlights, bookmarks and covers go with it. |
| **Reset book data…** | Clear progress, bookmarks, highlights and so on, with a tick box for each. |
| **Delete** | Delete the file, after asking. |

Other plugins that add entries to KOReader's file menu, like **Open Incognito**, add cards here too.

!shot:side book-menu-arrange | Arranging the actions.

**Long-press any card** to arrange them. Only the cards show while you do: tap one to pick it, then use **‹** and **›** to move it, **Hide** to leave it out of the menu (it stays greyed while arranging, and **Show** brings it back), **Reset** for the original order with nothing hidden, and **Done** when it's right. The order is the same for every book.

**Hardcover**
:   With the Hardcover plugin installed: which Hardcover book this is linked to, and **Edit** (or **Link…**) to change it. See [Hardcover](../organise/hardcover.md).

## Folders, series and authors

!shot:side group-menu | Long-press a series stack

**Long-press a folder, series, author, genre or collection** for its menu: a page of cards, each with a line saying what it does.

- **Pin to the shelf menu**: make it a shelf of its own, next to this one. The quickest way to make a shelf.
- **Select *N***: select all its books, for the batch actions below (**Add *N* more** or **Remove *N*** once some are selected).
- **Extract page counts…** for just these books.
- **Book binding**, for a series on a spines shelf: **Same as shelf**, **Hardback** or **Paperback**, for that series on every shelf. **Same as shelf** uses the shelf's own **Book binding**.
- **Set … image…**: give it a picture of your own, shown in place of its covers. See [Folders](../organise/folders.md).
- **Find author image online**, for an author.
- **Move…**, **Rename…** and **Delete…**, for a real folder: buttons beside its book count. Moving or renaming takes every book's progress and covers with it. **Delete…** asks first, then removes the folder and everything in it.

## Many books at once

Select books, then act on them all:

1. Start a selection: **Select** in a book's Edit tab, **Select *N*** in a folder or series menu, or **Bookshelf > Settings > Library & search > Bulk selection mode**.
2. **Tap books** to add or remove them. The footer shows an **X** to stop, and a basket with the count.

    !shot bulk-footer | The footer while selecting

3. Tap the basket for **Edit selected (*N*)**, a page of changes to make to them all:
    - **Reading status**: **Unopened**, **Reading**, **On hold** or **Finished**.
    - **Rating**: one to five stars, or **Clear**.
    - **Favorite**: **Add** or **Remove**.
    - **Collections**: a page of your collections. Tap one to add the books to it, again to remove them from it, and again to leave it as it is.
    - **Also on Apply**: **Refresh metadata** and **Remove from history**.
    - **Right away**: move, reset or delete the books. These don't wait for Apply.
4. The line at the top lists what **Apply** will do. Nothing else changes until you tap it, or **Cancel** to drop it all.

!shot bulk-edit-selected | Edit selected

**Select all in this shelf** takes every book on the shelf, across all its pages: the way to select a shelf built from [filters](../organise/sources-filters.md).
