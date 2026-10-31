---
description: Every shelf source, every filter and every sort key, with how they combine.
---

# Sources, filters and sorting

A shelf is three choices: a **source** (where its books come from), **filters** (which of them to keep) and a **sort** (what order). All three are cards in the shelf editor: long-press a shelf's tab.

<div class="walk" markdown>

<div markdown>

## Sources

Tap the **Source / grouping** card in the shelf editor. The Source page has four sections.

**Books**

| Source | Shows |
|--------|-------|
| **Home (flattened)** | Every book under your home folder, ungrouped. Home starts like this. |
| **Home (folders)** | Your home folder as folders, with books spread across sections. |
| **A folder** | One folder and its subfolders. Tap **As folders ›** to keep its folders, or **Flattened ›** for every book in it with no folder tiles. **Browse device…** reaches folders outside home. |
| **Recently read** | Books you've opened, most recent first: your KOReader history. |
| **Latest added** | Files on the device, newest file date first. |
| **Favorites** | Your favourites. |

</div>

!clip source-filter | Change a shelf's source, then filter it.

</div>

!shot:side source-picker | Source

**Grouped: a stack for each**: a stack per series, author and so on. Tap a stack to open it.

**Just one**: a shelf of one series, author and so on, picked from a list.

| A stack for each | Just one |
|------------------|----------|
| **Series** | **A series ›**: one series, in order |
| **Authors** | **An author ›** |
| **Genres** | **A genre ›** |
| **Collections** | **A collection ›** |
| **Formats** | **A format ›**: EPUB, PDF, CBZ… |
| **Ratings** | **A rating ›**, including **Unrated** |
| **Languages** | **A language ›** |

**More**

- **Shelf of shelves**: a shelf holding other shelves. See [Shelves](shelves.md#shelves-inside-shelves).
- **OPDS catalog ›**: an [online catalogue](opds.md).
- **Kindle Virtual Library** or **Kobo library**: your store library, on devices with the right plugin. See [Other libraries](other-libraries.md).

Picking a source gives the shelf a sensible sort for it, which you can change.

!!! tip "Searching a long list"
    The **Just one** pickers have a **Search…** box. Start typing an author's name rather than paging through hundreds. Beside it, **A-Z | Most books** lists the choices alphabetically or biggest first, and the pickers keep that order until KOReader restarts.

!shot specific-author | **An author ›** opens Choose author

## Filters

!shot:side filters-dialog | Filters

Tap the **Filters** card in the shelf editor. Each filter is a row, reading **Any** until you pick something:

| Filter | Keeps |
|--------|-------|
| **Status** | **Unread**, **Reading**, **On hold**, **Finished** |
| **Genre** | books with any of, all of, or none of the genres you pick |
| **Language** | the languages you tick |
| **Format** | the formats you tick |
| **Rating** | **5 stars** to **1 star**, or **Unrated** |
| **Collection** | books in any of the collections you pick, and in none of the ones you leave out |
| **Series** | **Only standalone books**, **Only books in series**, or **Standalone and books in series** |
| **Folders** | books in the folders you pick, minus the ones you leave out, subfolders and all |

A book has to match every filter you set. Within one list, ticking several values keeps a book that matches **any** of them (except **All of these genres**, below). So Status: Unread with Language: English and French gives unread books in either language. The cross on a row clears that filter, and **Clear all filters** at the top clears them all.

Pages you tick have **Clear** at the top and **Apply** at the bottom. Each choice shows how many books it would leave, given your other filters, so you can see a filter's effect before you tick it. Longer lists have **A-Z | Most books** beside the search box.

<div class="shots" markdown>

!shot filter-genre | Genre filter, with book counts

!shot filter-status | Reading status filter

</div>

### Genre and Collection

**Genre** opens a page of three lists, each with **+ Add genres**:

- **Any of these genres**: a book needs at least one of them.
- **All of these genres**: a book needs every one. Science fiction and humour, say.
- **Leave out these genres**: a book with any of them is dropped.

**Collection** works the same way with two lists: **In any of these collections** and **Leave out these collections**.

An empty list is ignored, and the cross on a pick removes it.

### Folders

**Folders** has two lists: **Only books in these folders** (**+ Add a folder**) and **Leave out these folders** (**+ Add a folder to leave out**). Each opens Bookshelf's own list of folders, with a search box; **Browse device…** reaches a folder outside it. Leave the first list empty to keep every folder except those left out.

<div class="shots" markdown>

!shot filter-folders | Folder filter

!shot folder-picker | Picking a folder

</div>

## Sorting

<div class="walk flip" markdown>

!clip sort | Change a shelf's sort, then reverse it.

<div markdown>

Tap the **Sort** card in the shelf editor. A shelf can sort on up to three levels: by surname, then series, then number in series, for instance.

The levels sit at the top of the Sort page, each showing its key and its direction in words, such as **Added/opened** with **Oldest first | Newest first**.

- Tap **Add a sort** (or **Add a tie-breaker** for the next level), then tap a key below.
- Tap a level to select it, then tap a different key to change it.
- Tap the other direction to reverse it: **A-Z** or **Z-A**, **Unread first** or **Finished first**, **Favorites first** or **Favorites last**.
- The cross on a level removes it.

On a grouped shelf, the first level is **Order the groups by** (**Name**, **Surname**, **Book count**, **Most recently read**…), and the next is **Sort the books inside each**.

</div>

</div>

<div class="shots" markdown>

!shot sort-picker | Sort

!shot sort-groups | Order the groups by, on a grouped shelf

</div>

??? note "Every sort key"
    | Key | Order |
    |-----|-------|
    | **Title** | A to Z |
    | **Author** | author's first name, A to Z |
    | **Surname** | author's surname, A to Z |
    | **Filename** | A to Z |
    | **Series** | series name, A to Z |
    | **Series #** | number in series |
    | **Series + #** | series name, then number |
    | **Series or title** | the series name, or the title for standalone books |
    | **Added/opened** | whichever is more recent |
    | **Added** | date added |
    | **Opened** | last opened |
    | **Progress** | how much you've read |
    | **Rating** | your rating |
    | **Unread 1st**, **Reading 1st**, **Favorite 1st** | that group first |
    | **Pages** | needs [page counts](page-counts.md) |
    | **File size** | |
    | **Books** | on grouped shelves, the biggest groups first |

    On a shelf of one collection there's also **Collection order**, the order you arranged the collection in KOReader, and **Edit collection order ›** to rearrange it.

Two settings affect every sort, under **Bookshelf > Settings > Library & search**: **Ignore The, A, An when sorting** (on by default) and **Sort Chinese text by pinyin**. With [Calibre metadata](other-libraries.md#calibre) on, **Surname** uses Calibre's author sort and title sorting uses Calibre's title sort.

!!! note "Added means the file's date"
    **Added**, **Added/opened** and the **Latest added** source use each file's date on the device. Calibre gives a book a new date whenever it sends it again, so after a full resync everything counts as just added. For a reading pile that stays put, a [collection](collections.md) is more dependable.

!!! note "There's no 'date finished'"
    Bookshelf can filter by **Finished** but can't sort by when you finished, or show "read this year". A collection per year works well (add books as you finish them, and pin it as a shelf), and the **Reading goals** [module](../customise/micro-modules.md) counts books finished by month and year.
