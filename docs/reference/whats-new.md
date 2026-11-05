---
description: What's new in recent versions of Bookshelf, with links to where each feature is explained.
---

# What's new

<span class="tag">These pages describe Bookshelf 6.3.3</span>

Full release notes for every version are on [GitHub Releases](https://github.com/AndyHazz/bookshelf.koplugin/releases), and in the app under **Bookshelf > Updates > View changelog**.

## 6.3.2

**Wallpaper scaling**
:   A picture that isn't the shape of your screen can be stretched (as before), cropped to fill, or fitted with a margin: **Scaling** at the foot of the wallpaper browser. The browser now shows each picture in your screen's shape, as it will look, and in portrait the picture on screen is the one used. [More](../customise/wallpaper-colours.md#wallpaper)

**Sort by publication year**
:   **Published** under **Book** on a shelf's Sort page, newest first: the same year as `%published`. Books whose year hasn't been read yet go last, then move into place once it has. [More](../organise/sources-filters.md#sorting)

**See and correct a book's date**
:   The book menu's Edit tab shows the publish date beside your rating and Hardcover's, with where it came from, and a date picker to correct it. With **Use Hardcover metadata** on, linked books use Hardcover's first-published year. Long-press your stars to clear your rating. [More](../use/book-menu.md#the-edit-tab)

**Fixes**
:   Books added by **Scan all library metadata** show in their series straight away, and changing a book's rating or status no longer clears its stored page count and date. **Random book**'s **All books** includes your Kindle library when you have a Kindle Virtual Library shelf.

## 6.3.1

**Faster and steadier**
:   A shelf of shelves with filters opens large folders much faster, and **Extract page counts** no longer misses books on devices short of memory. Dialogs from other plugins opened from KOReader's menu over the shelf draw in full, and the book menu's header has a light grey band.

## 6.3

**A publication year token**
:   `%published` gives a book's publication year, from Calibre, the OPDS catalogue (kept when you download a book) or the book file itself. Add it after the author with `%authors_short [if:published](%published)[/if]`, which shows nothing for a book with no date. [More](tokens.md)

**Delete a folder**
:   Long-press a folder: **Delete…** sits beside its book count with **Move…** and **Rename…**, and asks before it removes the folder and everything in it. [More](../organise/folders.md#moving-renaming-and-deleting)

## 6.2

**Image contrast**
:   **Covers and ornaments contrast boost** deepens the darks and lifts the lights of covers, spines and ornaments, for screens with few greys. **Wallpaper contrast** and **Wallpaper brightness** adjust the wallpaper on its own. All start at 0%. [More](../customise/layout.md#image-contrast)

**Turn pages behind menus**
:   Swipe left or right on the shelf behind a Bookshelf menu or slider page to turn its page, so you can see a change on more books without closing it. A tap outside a slider page keeps its value. [More](../use/navigation.md#pages)

**Footer bar**
:   **Settings > Behavior > Footer bar**: **Show**, **Hide** (the shelf uses its space) or **Invisible buttons** (the buttons still work where they were). [More](../reference/menus.md#behavior)

**Fewer flashes**
:   Closing KOReader's menu over the shelf, closing the Theme library, and moving between shelves with different themes no longer flash the whole screen.

**Calibre and OPDS**
:   **Read calibre metadata.calibre** is no longer marked beta. `%calibre{pubdate}` gives a book's publication year in an OPDS catalogue without it. [More](../reference/tokens.md)

## 6.1

**A new look for the menus**
:   The book menu, the shelf editor, the pickers and the ornament menu share one style and Bookshelf's UI font: grey cards, a close X on the title, and menus inside a menu that open as pages of it, with **Back** and a path along the top. [More](../organise/shelves.md#the-shelf-editor)

**Tap a shelf to edit it**
:   Tap the button of the shelf you're on to open its editor. Long-press still works on any shelf. [More](../organise/shelves.md#the-shelf-editor)

**A shorter shelf editor**
:   **View mode** sits beside **Source**, **Sort** beside **Filters**. **Modules** says how many the shelf has, and on a spines shelf opens a page of them. [More](../reference/menus.md#the-shelf-editor)

**Shelf order**
:   **Shelf order…** in the shelf editor lists every shelf at that level to move up or down. Tap a shelf to open its editor. [More](../organise/shelves.md#change-the-order-of-the-tabs)

**More from filters**
:   **Genre** has three lists, tagged **OR**, **AND** and **NOT**: any of these, all of these, and genres to leave out. Picks show as tags you tap to remove. **Collection** can leave one out too, and **Folders** are picked from Bookshelf's own folder list. Author, series and filter lists sort **A-Z** or by **Most books**. [More](../organise/sources-filters.md#genre-and-collection)

**Sort the Theme library**
:   **A-Z**, **Newest** or **Last used**. [More](../customise/themes.md#choose-a-theme)

**Arrange the book menu**
:   Long-press an action on the **Edit** tab to move it or hide it. Hardcover reviews can **Include spoilers**. [More](../use/book-menu.md#the-edit-tab)

**Search results keep their look**
:   Search results have their own **Show as**, which also applies to an author or series opened from them. [More](../use/shelf-styles.md#search-results)

**Sliders for sizes**
:   Text sizes and other scales are a slider in a slim panel, with the value in its title. [More](../customise/layout.md#text-sizes)

**The ornament menu**
:   Redesigned, with **Pin to a spot**, **Hide** and **Show**, and **Swap** offering any piece from any pack. The ornament library opens much faster with a big collection. [More](../customise/ornaments.md#adjust-one-on-the-shelf)

**Keys**
:   On a device with page or arrow keys, every Bookshelf menu shows a focus ring and takes the keys, and the cursor on a shelf reaches its modules and ornaments to open their menus. [More](../use/navigation.md#with-buttons)

**QR codes**
:   **About** has one for this guide, and **Add theme pack…** and **Add ornaments…** one for the shop, to open on your phone.

**Faster covers after a restart**
:   The cover cache keeps the covers you use, and ornaments no longer push them out. Devices with little memory use a smaller cache.

**Home's default**
:   Home shows every book flattened, newest added or opened first, if you have never edited your shelves. [More](../organise/shelves.md)

**What a theme pack leaves out**
:   A theme pack's missing parts (wallpaper, plank, colours) come from **Plain**, not your Custom theme. [More](../customise/themes.md)

## 6.0.3

**Turn off modules among your books**
:   **Micro modules > On the shelf** hides every module standing among a shelf's books, and the books take their space back. Turn it on again and they return where they were. [More](../customise/micro-modules.md#on-a-shelf-among-your-books)

## 6.0

**A layout editor for micro-modules**
:   Modules sit on a grid, full screen (six columns) or in the top panel (two rows), across up to four pages; swipe or tap the dots to turn them. Long-press one to resize it, move it, send it to another page or add more, with everything else faded while you work. Each module lays itself out for its space, and portrait and landscape keep their own layouts. [More](../customise/micro-modules.md#add-move-and-change-them)

**Modules among a shelf's books**
:   **Add a module to this shelf…** in the shelf editor stands any module between your books, on covers or spines. [More](../customise/micro-modules.md#on-a-shelf-among-your-books)

**Shelf and Ornament modules**
:   **Shelf** shows one of your shelves inside a module, in its own style. A tap puts a book in the top panel as a shelf does, and the module opens books even from the micro-modules button while reading. **Ornament** shows a piece from your ornament packs. [More](../customise/micro-modules.md#the-shelf-module)

**Groups in the module library**
:   Chips sort the library into **Shelf & books**, **Reading**, **Time & device**, **Fun & info** and **Actions**, plus one per module pack and **My modules**. Module packs install and update like any KOReader plugin. [More](plugin-authors.md#micro-modules)

**A Highlights tab in the book menu**
:   A book's highlights, notes and bookmarks without opening it, with **View in book** to jump to one. [More](../use/book-menu.md#the-book-menu)

**Pin an ornament**
:   **Pin here** keeps a shelf ornament where it stands, page after page. [More](../customise/ornaments.md#pin-one-in-place)

**Copy and move shelves**
:   **Copy** and **Move to…** in the shelf editor copy a shelf, or move it in and out of a shelf of shelves. [More](../organise/shelves.md#shelves-inside-shelves)

**Coloured panels**
:   **Panel color** in **Theme > Colors** gives the top panel and footer a colour of their own in place of white or black, with text to suit, or your own pick under **Panel text**. Both are kept separately for the light and dark looks. [More](../customise/wallpaper-colours.md#wallpaper)

**Colours for each module**
:   The palette icon in a module's menu gives that card its own background, border and text, and modules can offer colours of their own. [More](../customise/micro-modules.md#add-move-and-change-them)

**Each book in one group**
:   **Library & search > Show each book in one group only** files a book with several authors, genres or collections under just one of them. [More](../organise/groups.md)

**Author photos shaped like covers**
:   Author photos are cropped to a book cover's shape, so author stacks line up with the books around them. [More](../organise/groups.md#author-photos)

**Warmer module cards**
:   Module cards are warm paper by default on colour screens, and the same grey as before on black-and-white screens.

## 5.5.5

**Star ratings on covers**
:   **Cover display > Favorite icon or star rating > Stars (rating)** puts your rating in the corner of every rated book. [More](menus.md#cover-display)

**Hardcover ratings as a stand-in**
:   **Hardcover enrichment > Use Hardcover rating if no user rating** fills in books you haven't rated, on covers, in the Rating sort and on the Ratings shelf. [More](../organise/hardcover.md#what-you-can-use)

**Refresh the library from a gesture**
:   **Bookshelf: refresh the library** is a Gesture manager action, for any gesture or a quick menu. [More](gestures.md#gesture-manager-actions)

## 5.5.4

**Paperback binding**
:   Spine shelves can draw their books as paperbacks: thin flush covers and lighter page edges. Per shelf under **Shelf style > Book binding**, or per series from its long-press menu. [More](../use/shelf-styles.md#spines)

**E-ink refresh rate for shelf pages**
:   Shelf page turns can flash clean as often as KOReader's own full refresh rate, to clear ghosting. **Advanced > Performance tweaks > Use E-ink refresh rate for shelf pages**. [More](menus.md#advanced)

**Faster micro-modules**
:   The full-screen micro-modules view opens much faster, and **Shelf size** and **Reading goal** fill in their numbers in the background.

**About** links this guide.

## 5.5

**Series boxes**
:   On a spine shelf, each series can stand as an open slipcase holding its books, with a read count. **Shelf style > Series boxes**. [More](../organise/groups.md#series-boxes)

**Author photos**
:   **Find author images online…** fetches a photo for every author on your shelves, from Open Library or Wikipedia. [More](../organise/groups.md#author-photos)

**Page badge**
:   Pages, percent read, or both, in the corner of every cover, with printed page counts where a book has them. [More](../organise/page-counts.md#showing-the-count)

**New sorts**
:   **Added/opened** (whichever is more recent) and **Favorite 1st**. [More](../organise/sources-filters.md#sorting)

**Recently read** micro-module
:   The covers of the books you opened last, a tap from opening. [More](../customise/micro-modules.md#the-modules)

**Random book** can open directly
:   Its settings now have **On tap: Open book directly**. (5.5.2)

**Online catalogues**
:   Comics and manga servers that stream page by page get KOReader's **Page stream** buttons. [More](../organise/opds.md#comics-and-manga)

**Other plugins' formats**
:   Book formats another plugin registers with KOReader show on your shelves. [More](plugin-authors.md#other-book-formats)

**Stack count badges on a shelf of shelves**
:   Tiles inside a shelf of shelves show how many books they hold. (5.5.3)

And a long list of fixes: see the release notes.

## 5.4

**Themes**
:   Themes became layers: a **Default theme** for every shelf, and any shelf can wear its own. The Theme library shows each as a card. [More](../customise/themes.md)

**Shelf of shelves**
:   A shelf that holds other shelves. [More](../organise/shelves.md#shelves-inside-shelves)

**Auto, per level**
:   A shelf can show its top level one way and what you open another. [More](../use/shelf-styles.md#auto-a-style-per-level)
