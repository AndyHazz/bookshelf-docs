---
description: Show a shelf as a grid of covers, a list, or spines on a plank. Captions, folder tiles, face-out books, Auto per level, rows and columns.
---

# Covers, lists and spines

Every shelf can be drawn three ways, and each shelf remembers its own.

<div class="clips" markdown>

!still style-covers | **Covers**: a grid of cover art, with a caption under each.

!still style-list | **List**: titles, authors and progress, row by row.

!still style-spines | **Spines**: books edge-on on a wooden plank.

</div>

## The quick way

<div class="walk" markdown>

<div markdown>

**Long-press the page counter** in the footer. Each long-press moves the shelf on screen to the next style: Covers, then List, then Spines, then back to Covers.

It changes only the shelf you're looking at. Home can be a grid of covers while Recent is a list.

!!! note "A fresh install starts on spines"
    On a new install the Home shelf shows spines. If you'd rather a grid of covers, long-press the page counter once. The videos on this site mostly show Home as covers.

</div>

!clip shelf-styles | Long-press the page counter to step through the styles.

</div>

## The full set of options

<div class="walk flip" markdown>

!clip shelf-editor-style | Long-press a shelf's tab, then Shelf style.

<div markdown>

**Long-press a shelf's tab** to open its editor, then tap **Shelf style**. The dialog has:

- **Theme**: the [theme](../customise/themes.md) this shelf wears.
- **Show as**: **Auto**, **Covers**, **List** or **Spines**.
- The settings for the style you picked, below. They change with it.

Everything applies as you tap, and the shelf redraws behind the dialog. **Close** when you're happy.

The editor's button names the style the shelf is pinned to: **Shelf style: List**, say. A shelf left on the default Covers names its folder tiles instead, so the Genres shelf reads **Shelf style: Ribbon**.

</div>

</div>

## Covers

The grid most people settle on. Each cover can carry small badges: a heart for favourites, the number in its series, a bookmark while you're reading, a mark once finished, and a progress bar. Choose which under **Bookshelf > Settings > Cover display** (see [Layout](../customise/layout.md#on-every-cover)).

<img class="shelfrow" src="../../assets/ui/cover-row-2-light.webp#only-light" alt="Covers with series numbers, favourite hearts and finished marks" style="max-width:620px;margin:1.2rem auto 1.6rem"><img class="shelfrow" src="../../assets/ui/cover-row-2-dark.webp#only-dark" alt="Covers with series numbers, favourite hearts and finished marks" style="max-width:620px;margin:1.2rem auto 1.6rem">

**How big.** The number of columns sets the size: **pinch** the shelf for more, smaller covers, **spread** for fewer, bigger ones. Or use **Bookshelf > Adjust shelf/top panel size…** for exact numbers.

!shot:side shelf-style-covers | Shelf style on a Covers shelf

In **Shelf style**:

| Setting | What it does |
|---------|--------------|
| **Folder tiles** | How folders, series and authors look: **Divider card**, **Ribbon**, **Book stack**, **Collage**, **Text** or **None**. **Default setting** follows the library-wide choice in **Bookshelf > Settings > Cover display > Default folder style**. |
| **Cover captions** | The line under each cover: **Title**, **Author**, **Series**, **None** or **Custom…**, built from [tokens](../reference/tokens.md). |

!clip folder-style | Default folder style: from Divider card to Ribbon.

## List

<div class="walk flip" markdown>

!clip list-view | The Recent shelf as a list, and its options.

<div markdown>

!shot style-row-list | The Recent shelf as a list

!shot shelf-style-list | Shelf style on a List shelf

Each row shows a cover thumbnail beside up to six lines of text: by default the title with rating and favourite, the author, the start of the blurb, and a progress bar with pages.

| Setting | What it does |
|---------|--------------|
| **List columns** | 1 to 3 columns side by side, or Auto. |
| **List rows** | 1 to 12 rows a page, or Auto to fit the screen. |

Pinching a list fits one more or one fewer row. To change what the lines say, see **Bookshelf > Settings > List view**, which works like the [top panel](../customise/top-panel.md) line editor. All list shelves share one layout.

</div>

</div>

## Spines

Books stand edge-on on a plank, like a real bookcase, so lots fit at once. Some people love it; if it's not for you, the other two styles do everything it does. Each book is drawn from what Bookshelf knows about it:

- **Width** from the page count, so a doorstop is fatter than a novella. Until a book has a page count it gets an average width: see [Page counts](../organise/page-counts.md).
- **Height** from the cover's shape.
- **Colour** from the cover art, darkened so the title stays readable.

<img class="shelfrow" src="../../assets/ui/shelf-row-1-light.webp#only-light" alt="A row of book spines on an oak plank, with a potted cactus at the end"><img class="shelfrow" src="../../assets/ui/shelf-row-1-dark.webp#only-dark" alt="A row of book spines on an oak plank, with a potted cactus at the end">

Tap a spine and the book lifts off the shelf into the top panel. Tap it again to open it, or tap empty space to put it back.

!shot:side shelf-style-spines | Shelf style on a Spines shelf

| Setting | What it does |
|---------|--------------|
| **Book binding** | **Hardback** or **Paperback**: thin flush covers, softer shading and lighter page edges. A series can have its own from its long-press menu. |
| **Series boxes** | Each series stands as an open slipcase holding its books, with the first cover as a sticker and a read count. Tap one to open the series. |
| **Spine rows** | How many shelves fit on the screen. **Auto** fits the space. |
| **Spine thickness** | Fatter or thinner spines across the board, 60% to 200%. |
| **Face out** | Which books turn to show their cover. See below. |
| **Author on spine** | Print the author under the title. |
| **Ornaments** | How often [ornaments](../customise/ornaments.md) stand in the gaps: **None**, **Rarely**, **Often** or **Always**. |

The plank and ornaments come from the shelf's [theme](../customise/themes.md), and [theme packs](../customise/packs.md) bring more.

### Face out

<div class="walk" markdown>

<div markdown>

Like a bookshop dressing a shelf, some books can turn to show their cover. **Face out** lets you tick as many reasons as you like:

- **Unread**, **Reading**, **On hold**, **Finished**
- **Unread standalone**: unread books that aren't in a series
- **Favorites**
- **First in series** or **First unread in series**
- **Recently added**, with **How many** (1, 3, 5, 10 or 20)
- **In a collection**, then choose which one: a To read pile, say
- **All books**, or **None**

The Home shelf ships with Favorites, Reading and the five newest. A new shelf starts with Favorites.

!shot face-out-dialog | Shelf style > Face out

</div>

!clip face-out | Shelf style > Face out > All books.

</div>

## Auto: a style per level

<div class="walk flip" markdown>

!clip auto-levels | Genres as a list, each genre opening as its own shelf.

<div markdown>

**Auto** picks a style for each level of a shelf:

- **Level 1** is the shelf itself.
- **Level 2** is anything you open from it: a series, an author, a folder.

!shot shelf-style-auto | Shelf style on an Auto shelf

Tap either to step through Covers, List and Spines. So a Genres shelf can **list** its genres and open each genre as a **grid of covers**. When both levels are lists, each gets its own rows and columns.

</div>

</div>

## Search results

Search results have their own style, separate from any shelf. **Long-press the Search results pill** in the shelf menu and choose **Covers**, **List**, **Spines** or **Auto**.

!shot search-results-style | Show search results as
