---
description: Change the card above the shelf - its size, which sections show, and every line's text, font and style.
---

# The top panel

The top panel is the card above the shelf. It shows the book you're reading, or the book you've just tapped: cover, title, author, blurb, tags and progress, with a status line across the top.

It can show a grid of [micro-modules](micro-modules.md) instead: a clock, a quote, one of your shelves, with up to four pages of them. Turn on **Settings > Micro modules > In the top panel**, then tap the grid button at the end of the shelf menu.

## Its size

<div class="walk" markdown>

<div markdown>

The shelf takes the rows and columns it needs, and the top panel fills what's left. So you size the top panel by sizing the shelf:

- **Pinch** or **spread** the shelf.
- **Swipe** on the top panel (below).
- **Bookshelf > Adjust shelf/top panel size…** sets **Columns** and **Rows** exactly, with the shelf changing behind as you go. **Accept** keeps it.

To hide it, **swipe up** on the shelf for full screen. A thin status line stays at the top; tap it, or swipe down, for the panel again.

</div>

!clip top-panel-layout | Resize the top panel, hide it and bring it back.

</div>

<div class="walk" markdown>

<div markdown>

**Swipe down** on the top panel for a bigger panel, with one shelf row fewer: a larger cover and more of the blurb. **Swipe up** on the panel to give the row back.

Start the swipe on the panel itself rather than at the very top of the screen. A swipe down from the top edge opens KOReader's menu instead.

</div>

!clip panel-resize | Swipe down on the top panel for a bigger panel, up to give the row back.

</div>

!shot adjust-size | Bookshelf > Adjust shelf/top panel size…

## What it shows

!shot:side edit-top-panel-menu | Settings > Edit top panel content.

**Bookshelf > Settings > Edit top panel content** lists its sections:

| Section | Shows |
|---------|-------|
| **Rating (interactive)** | Five stars you can tap to rate the book. Off at first. |
| **Title** | |
| **Author** | In handwriting, at first. |
| **Metadata** | A free line. Off at first, since the series is already a tag. |
| **Description** | The blurb. Tap it on the panel to read it all. |
| **Tags (interactive)** | Pills for the series and genres. Tap one to open that shelf. |
| **Progress** | Percentage, a bar, and the time left. |

If you upgraded from an older version and never changed the panel, it keeps the older layout instead: Metadata on, Tags off and a plain author line. **Reset top panel content to defaults** (below) switches to the layout above.

**Tap** a section to edit it. **Long-press** it to hide or show it. The **Status line** across the very top has its own row above, and works the same way.

!shot:wide status-line | The status line: time, storage, battery, light and Wi-Fi.

## Edit a line

<div class="walk flip" markdown>

!clip top-panel-content | Edit the Author line: a new font and size.

<div markdown>

Tapping a section opens the **line editor**. The panel behind updates as you type.

- The **text box** holds the line. Words starting with `%` are [tokens](../reference/tokens.md), replaced with the book's details: `%title`, `%authors`, `%book_pct`.
- **Regular** steps through Bold, Italic and Bold italic.
- **Size** and **Font…**, each font shown in its own typeface.
- **Aa** for capitals, and the alignment button.
- On **Progress**: **Bar style** (Bordered, Solid, Rounded, Metro, Wave, Pacman), **+ Bar** and **Bar height**.
- **Tokens…** and **Icons…** insert a token or a glyph.
- **Save**, or **Cancel** to leave it as it was.

</div>

</div>

<div class="shots" markdown>

!shot line-editor-author | The line editor on Author.

!shot line-editor-progress | On Progress, with its bar row.

</div>

<div class="shots" markdown>

!shot token-picker | Tokens…

!shot icons-library | Icons…

</div>

### Some ideas

| Line | Try |
|------|-----|
| Metadata | `%series_name #%series_num`, shown only for books in a series: `[if:series]%series_name #%series_num[/if]` |
| Progress | `%book_pct  %bar  %book_time_left` |
| Status line | `%time_12h %spacer %batt_icon%batt` |

The [tokens page](../reference/tokens.md) has every token and how conditions work.

## The Tags section

!shot:side tags-menu | The Tags section's settings.

Tags isn't a line of text, so it opens its own settings: **Show tags line**, which kinds of pill to show (**Author**, **Series**, **Collections**, **Genres**, **Folder**), **Font size**, **Alignment** and **Maximum tag rows**. Extra pills fold into a **+N** pill.

## Text size and starting over

- **Bookshelf > Settings > Text size > Top panel** scales the whole panel.
- **Bookshelf > Settings > Advanced > Reset top panel content to defaults** puts back the look a fresh install has.

## The same line while reading

**Bookshelf > Settings > Advanced > While reading > Show status line** draws the top panel's status line across the top of the reader too, so it's the same on the shelf and in a book.
