---
description: Every Bookshelf menu, dialog and option, where to find it, what it does and what it starts as.
---

# Every menu option

This page lists every Bookshelf menu and dialog, organised by where you find it. Each option has its exact label in **bold** (labels on screen use American spelling, such as Color, Favorites and Behavior), what it does, and its default on a fresh install. (A few defaults are different if you upgraded from an older version; those say so.)

Most of Bookshelf's settings live in KOReader's top menu: tap the top edge of the screen (or swipe down from it) while the shelf is showing, then pick the **Bookshelf** tab, the open-book icon second from the left. That tab only appears in the file browser and on the shelf, not while a book is open.

Paths are written like **Bookshelf > Settings > Behavior**.

## Where is it?

| I want to... | Go to |
|---|---|
| Open Bookshelf when KOReader starts | KOReader file browser menu, first (filing-cabinet) tab > **Start with** > **bookshelf** |
| Change how many covers fit across and down | **Bookshelf > Adjust shelf/top panel size…**, or pinch and spread on the shelf |
| Change the order of the shelf tabs | Long-press a tab, then **Shelf order…** |
| Add or hide shelves | **Bookshelf > Edit shelves…** |
| Change a shelf's source, filters or sort | Long-press the shelf button to open the shelf editor |
| Switch a shelf between Covers, List and Spines | Shelf editor > **View mode** > **Show as**, or long-press the page number in the footer |
| Change the theme, wallpaper, plank or colours | **Bookshelf > Theme** |
| Change what the top panel shows | **Bookshelf > Settings > Edit top panel content** and **Status line** |
| Change the lines in List view | **Bookshelf > Settings > List view** |
| Change the text under covers | **Bookshelf > Settings > Cover display > Cover captions** |
| Make text bigger or smaller | **Bookshelf > Settings > Text size** |
| Turn off a Bookshelf gesture | **Bookshelf > Settings > Behavior > Bookshelf gestures** |
| Give covers and ornaments more contrast | **Bookshelf > Settings > Image contrast** |
| Hide the footer | **Bookshelf > Settings > Behavior > Footer bar** |
| Put modules on the home screen | **Bookshelf > Settings > Modules** |
| Edit the start menu | Long-press any entry in the start menu |
| Update the plugin | **Bookshelf > Updates > Check for updates** |
| Show page counts or percent read on covers | **Bookshelf > Settings > Cover display > Page badge** |
| Fit more rows on a list shelf | Shelf editor > **View mode** > **Rows**, or pinch the list |
| Put a clock in the start menu | Long-press any start menu entry > plus > **Bookshelf module…** > **Clock** |
| Fetch author photos | **Bookshelf > Settings > Library & search > Find author images online…** |
| Give a folder or series a picture | Long-press it > **Set folder image…** (or series, author…) |
| Fill in page counts | **Bookshelf > Settings > Library & search > Extract page counts…** |
| Make every book face out | Shelf editor > **View mode** > **Face out** > **All books** (Spines only) |
| Back up or remove Bookshelf | See [Files, backup and removing](files.md) |
| Start again with the default shelves | **Bookshelf > Settings > Advanced > Reset shelf menu to defaults** |

## The Bookshelf tab

The rows of KOReader's **Bookshelf** tab, top to bottom.

!shot:side bookshelf-tab | The Bookshelf tab

**Open Bookshelf** / **Close Bookshelf**
:   Opens the shelf over KOReader's file browser, or closes it again. The label changes to Close while the shelf is on screen.

**Adjust shelf/top panel size…**
:   Opens a live overlay for the cover grid. The shelf shows as covers while it is open, whatever its style, so you can see the grid you are changing. Greyed out unless the shelf is on screen.

    !shot:side adjust-size | Adjust shelf/top panel size

    - **Columns** (minus and plus): covers across, from 2 to 6. Fewer columns means bigger covers. Default: 4.
    - **Rows** (minus and plus): rows of covers. Default: enough to leave the top panel about 30% of the screen.
    - **Cancel** puts the old values back; **Accept** keeps the new ones.

    The top panel takes whatever height is left. List and Spines shelves use the same space with their own row counts. This setting is shared by every shelf.

**Edit shelves…**
:   The list of your shelves. See [Edit shelves](#edit-shelves).

**Theme (*name*)**
:   Themes, wallpaper, plank, ornaments and colours. Named after the theme the shelf on screen wears. See [Theme](#theme).

**Hardcover enrichment**
:   Only there while KOReader's Hardcover plugin is installed and enabled. See [Hardcover enrichment](#hardcover-enrichment).

**Settings**
:   Everything else. See [Settings](#settings).

**Updates**
:   Reads **Update available: v*X*** once a check has found a newer release. See [Updates](#updates).

**About**
:   A popup with the version, a link to this guide with a QR code for it (to open on your phone), and a link to the project page. If it finds another copy of Bookshelf installed, such as an old folder left beside the current one, it lists where: KOReader loads every copy it finds, so the extra one should be removed.

    !shot about-popup | About

### Start with

This is KOReader's own setting, not a Bookshelf one. In KOReader's **file browser**, open the top menu, go to the first (filing-cabinet) tab, then the last row, **Start with**, and choose **bookshelf**. The row then reads **Start with: bookshelf** and the shelf opens at once. Choosing any other Start with option while the shelf is showing closes it. See also [Open on startup](../get-started/startup.md).

## Edit shelves

**Bookshelf > Edit shelves…**

!shot:side edit-shelves | Bookshelf > Edit shelves…

**Flexible shelf widths**
:   Sizes each shelf button to fit its label, so icon-only shelves stay narrow. Off gives every button the same width. Default: on (off if you upgraded from a version before this setting).

**Uppercase labels**
:   Shows shelf names and the breadcrumb in capitals. Off shows them exactly as typed. Default: on.

One row per shelf
:   Each of your top-level shelves, with a tick when it is shown. **Tap** a row to open that shelf's [shelf editor](#the-shelf-editor). **Long-press** it to show or hide the shelf. This is the only place to hide a shelf. Shelves inside a shelf of shelves are not listed. A grey line at the foot says the same: **Tap a shelf to edit it. Long-press to show or hide it.**

**+ Add new shelf**
:   Makes a shelf called "New shelf" and opens its editor on the [Source](#source) page. If you back out without picking a source, the new shelf is removed.

A fresh install starts with four shelves: **Home** (every book under your home folder in one list, shown as Spines and sorted by **Added/opened**), **Recent** (books you have opened, shown as List), **Series** and **Genres**. If you upgraded and have never edited any shelf, Home moves to the same flattened, Added/opened Home; once any shelf has been edited, Home stays as you had it. Latest, Authors, Favorites and the rest can be added from the Source page.

## Theme

**Bookshelf > Theme (*name*)**. Long-press the row for a short explanation of themes. For a guided tour, see [Themes](../customise/themes.md).

!shot:side theme-menu | Bookshelf > Theme

**This shelf: *theme***
:   Opens the Theme library for the shelf on screen. Reads **Default theme** while the shelf follows the default, or **Same as *shelf*** for a shelf inside a shelf of shelves that follows its parent.

**Other shelves: all default** / **Other shelves: *N* with own themes**
:   A row for each other shown shelf, reading *shelf*: *theme*. Tap one to switch to that shelf and open its Theme library.

**Default theme: *theme***
:   The theme every shelf without its own wears. Default: Custom theme.

**Light or dark: *choice***
:   **Auto (follow night mode)**, **Light** or **Dark**. Sets the shelf's light or dark colours separately from KOReader's night mode. Part of the theme. Default: Auto (follow night mode).

**Wallpaper: *name***
:   The wallpaper submenu (below). Long-press it to see which folders pictures load from.

**Plank: *name***
:   Opens the plank browser. Long-press to reset the plank colour. Default: Oak.

**Ornaments: *N* of *M* on**
:   Opens the ornament browser. Long-press to see the ornaments folder.

**Colors**
:   The colour list (below).

**New ornaments go: *first/last***
:   Where newly added ornaments join each shelf's ornament order: **First, so you see them** or **Last, so your shelf stays put**. This belongs to your ornament collection, not to a theme. Default: first.

### Wallpaper

**Bookshelf > Theme > Wallpaper**

!shot:side theme-wallpaper-menu | Bookshelf > Theme > Wallpaper

**Wallpaper: *name***
:   Opens the wallpaper browser. Default: None. (A "Leafy wallpaper" is copied into your wallpapers folder but not chosen.)

**Full screen wallpaper: *name***
:   A different picture for full screen shelves, or **Same as wallpaper**. Default: Same as wallpaper.

**Invert wallpaper when dark**
:   Shows the wallpaper as its negative when the shelf is dark. A pack's own dark wallpaper is never inverted. Default: off.

**Color behind wallpaper: *value***
:   The colour that shows round the picture. Long-press to reset. Default: white.

**Panel colors and shading: *level***
:   How strongly the top panel and footer are shaded over the wallpaper: **Transparent**, **Low**, **Moderate**, **Heavy** or **Solid**. Below the levels, **Panel color** and **Panel text**, the same rows as in Colors. Default: Heavy.

**Blur wallpaper behind panels**
:   Blurs the picture behind the top panel and footer before shading it. Greyed out at Transparent and Solid. Default: off.

**Panel behind Covers shelves**
:   On Covers shelves, draws one panel behind the top panel, covers and footer instead of a plate under each title. Default: off.

**Wallpaper contrast: *N%*** and **Wallpaper brightness: *N%***
:   The wallpaper quieter or bolder, darker or lighter, from -100% to 100%. The same rows as in [Image contrast](#image-contrast); not part of any theme. Default: 0%.

**Extra wallpaper folder: *folder***
:   Another folder to load wallpapers from. Long-press to stop using it. Not part of any theme. Default: None.

### Colors

**Bookshelf > Theme > Colors**. Each row shows its current value. Tap a row to open the colour picker; long-press it to reset just that colour. The defaults below are for a light shelf on a greyscale screen, as % black.

!shot:side colors-menu-1 | Bookshelf > Theme > Colors

??? note "The full Colors list"

    **Reset to default colors**
    :   Clears every colour in this list, light and dark, for the theme on screen.

    **Colors for: Light** / **Colors for: Dark**
    :   Switches which set the rows below edit. It does not change the shelf or night mode. Starts on the set the shelf is using.

    **Text ink**
    :   The shelf's own text. Default: 100% (black on a light shelf, white on a dark one).

    **Progress bar** / **Progress bar track**
    :   The filled and unfilled parts of the bar on covers. Defaults: 75% and 0% (white).

    **Bookmark color** / **Finished bookmark color**
    :   The in-progress bookmark and the finished mark. Defaults: 75% and 0%.

    **Favorite heart color** (or **Favorite star color**)
    :   Follows the favourite icon chosen in Cover display. Default: light pink for the heart, gold for the star (about 20% on a greyscale screen).

    **Badge foreground** / **Badge background**
    :   Text and fill of the series number and page badges. Defaults: 100% and 0%.

    **Panel color** / **Panel text**
    :   The colour of the top panel and footer, blended over the wallpaper as strongly as the shading says, and the text and icons on them. Default: white by day, black on a dark shelf; with a panel colour set, **Panel text** is **Auto**, black or white, whichever reads on it.

    **Module background** / **Module border**
    :   The card behind each module and the line round it. A module can have its own, from **Style** in the [layout editor](#layout-editor). Defaults: about 7% (a very light grey); the border follows the text colour.

    **Border color**
    :   Cover frames, badge borders and folder card edges. Default: 100%.

    **Selection outline color**
    :   The ring round the selected or currently reading book. Default: 100%.

    **Cover shadow color**
    :   The drop shadow behind covers and folder cards. Default: mid grey, darker in night mode.

    **Folder overlay background** / **Folder text color**
    :   The card fill behind folder and stack tiles, and their label text. Defaults: 20% and 100%.

    **Shelf menu background**
    :   The bar behind the shelf buttons. Its picker has an extra **Transparent** choice. Default: white by day, black at night.

    **Selected shelf background** / **Selected shelf text**
    :   The selected shelf button. Defaults: inverted (100%) and paper white (0%).

!shot:side colour-picker | The colour picker on a colour screen

The colour picker
:   On a colour screen: 25 colour chips and a `#` field for a hex colour. On a greyscale screen: 15 greys from white to black, as they look on screen. Tap a chip to try it on the shelf behind. The footer has **Cancel** (puts the old colour back), **Default** and **Apply**.

### Theme library

Opened from **This shelf**, a shelf under **Other shelves**, **Default theme**, or the **Theme** card in the shelf editor (where it is a page of the editor). Titled **Theme: *shelf*** or **Default theme**.

!shot:side pack-theme-library | Theme library

- Four cards a page: **Default theme** (for a shelf), **Custom theme**, **Plain**, then every theme pack. The built-in ones have a `*` before their name. Each card sums up what the theme brings and says **Edited** if you have changed it. Whatever a theme does not bring is Plain's: no wallpaper, the built-in plank and the default colours.
- The strip under the title: **A-Z**, **Newest** (the packs most recently copied onto the device first) or **Last used**, then **Add theme pack…** (where to copy a pack folder, with the shop's QR code and link) and **Reset edited theme** (asks, then throws away your changes to the marked theme; greyed if there are none).
- **Tap** a card to use it. The shelf behind redraws and the library stays open.
- **Long-press** an edited pack or Plain to reset it, after asking. One you have not changed says so.
- The X in the title closes it (from the shelf editor, the back arrow goes back a page).

### Wallpaper, plank and ornament browsers

!shot:side pack-wallpaper-browser | Wallpaper browser

Wallpaper browser
:   Tabs **All**, **Yours**, then one per pack with a wallpaper. Tap a picture to use it straight away. The strip has **Same as wallpaper** (full screen browser only) and **No wallpaper**; the X in the title closes it.

!shot:side pack-plank-browser | Plank browser

Plank browser
:   Tabs **All**, **Built-in**, then one per pack with planks. Entries are **Plain color**, **Oak**, then pack planks. **Plain color** asks for a colour, then brings you back. The X in the title closes it.

!shot:side pack-ornament-collection | Ornament collection

Ornament collection
:   Tabs **All**, then one per pack (marked **(off)** when the pack is off). A line under the grid says whose set the ticks are, for example "On Plain shelves: 12 of 443. Check a piece to add it, uncheck to take it off." Tap an ornament to add it to the theme on screen or take it off. Long-press for **Hide** / **Show** and **Delete…**, which removes the file. The strip has **Add ornaments…** (where to put files, with the shop's QR code and link; on the All tab), **Select all** and **Select none**; the X in the title closes it. Opened from an ornament's **Swap**, it is titled **Swap for** and has no ticks: tap the piece to swap in, from any pack. See [Ornaments](../customise/ornaments.md).

## Hardcover enrichment

**Bookshelf > Hardcover enrichment**. Only present while the Hardcover plugin is installed and enabled. See [Hardcover](../organise/hardcover.md).

**Cached Hardcover ratings: *rated/linked · last fetch***
:   A greyed status row.

**Auto-link all books**
:   Links every unlinked book. Choose **Exact match (ISBN / Hardcover id)** or **Best guess (title & author)**. Tap the progress to cancel. Ends with a report.

**Show Hardcover ratings**
:   The top panel's rating row shows the cached Hardcover rating instead of yours, and the rating row is turned on. Default: off.

**Use Hardcover rating if no user rating**
:   Books you haven't rated yourself use their Hardcover rating instead: in star ratings on covers, the **Rating** sort and the **Ratings** shelf. Linked books only, from ratings already fetched. Default: off.

**Use Hardcover metadata**
:   Linked books show Hardcover's title, author, series and genres in place of their own. Default: off.

**Download covers from Hardcover**
:   Linking a book also downloads its Hardcover cover and uses it. Default: off.

**Hardcover genres used: *N***
:   How many of a linked book's genres to use, 0 to 20. Needs Use Hardcover metadata. Default: 5.

**Manage Hardcover data**
:   **Refresh ratings only**; **Refresh linked book details** (one request per book, cancellable); **Clear cache (keeps links)**; **Remove downloaded covers** (puts the originals back, keeps links); **Remove all Hardcover data** (unlinks everything and cannot be undone).

## Settings

!shot:side settings-menu | Bookshelf > Settings

**Bookshelf > Settings**. Rows that change the top panel are greyed out unless the shelf is on screen. In order: Status line, Edit top panel content, Cover display, List view, Text size, Bookshelf UI font, Image contrast, Modules, Start menu, Behavior, Library & search, Advanced.

### Status line

!shot status-line | The status line

**Status line: *preview***
:   The strip of device and reading details at the very top of the top panel, also shown on full screen shelves. The row shows a live preview. **Tap** to open the [line editor](#the-line-editor); **long-press** to turn it on or off. Default: on, showing the time, free storage, battery, frontlight and Wi-Fi.

### Edit top panel content

!shot:side edit-top-panel-menu | Edit top panel content

**Bookshelf > Settings > Edit top panel content**. One row per section of the top panel, each with a live preview. **Tap** a row to open its line editor; **long-press** to turn the section on or off. See [The top panel](../customise/top-panel.md).

| Section | What it shows by default | On by default |
|---|---|---|
| **Rating (interactive)** | Five stars you can tap. Tapping the row just turns it on or off. | No |
| **Title** | The title, large | Yes |
| **Author** | The author, or "A and B", or "A, B, et al." | Yes |
| **Metadata** | The series and number | No |
| **Description** | Your rating, then the book's blurb | Yes |
| **Tags (interactive)** | Tappable pills for series and genres | Yes, one row |
| **Progress** | Percent read, a progress bar and time left | Yes |

If you upgraded from an older version and never edited the top panel, you have the older layout instead (Metadata on, Tags off); **Advanced > Reset top panel content to defaults** switches to the one above.

**Tags (interactive)** has its own submenu instead of a line editor:

!shot:side tags-menu | Edit top panel content > Tags (interactive)

**Show tags line**
:   Turns the pills on or off.

**Author**, **Series**, **Collections**, **Genres**, **Folder**
:   Which kinds of pill to show. Default: Series and Genres (all five if you upgraded from an older version).

**Font size: *N***
:   8 to 48. Default: 14.

**Alignment: *choice***
:   **Left**, **Center** or **Right**. Default: Left.

**Maximum tag rows: *N***
:   1 to 5. Extra pills fold into a "+N" button. Default: 1 (2 if you upgraded from an older version).

### The line editor

!shot:side line-editor-progress | The line editor for Progress

Used by the status line, each top panel section, each List view line and custom cover captions. You type a template in the box, and the top panel or list updates behind it as you type. The [Tokens](tokens.md) page explains templates in full.

??? note "Line editor buttons"

    **Regular** / **Bold** / **Italic** / **Bold italic**
    :   One button that steps through the four weights. (Cover captions have a plain **Bold** toggle instead.)

    **Size: *N***
    :   Font size, 8 to 48, with -5, -1, +1 and +5 buttons, **Default** and **Close**.

    **Font…**
    :   Pick a font, each shown in its own typeface. Reads **Font ✓** once one is chosen. The picker's footer has **Cancel**, **Default** and **Done**.

    **Aa** / **AA**
    :   Uppercase on or off. Not shown for Description.

    Alignment button
    :   Steps through left, centre and right. Greyed out when the line contains `%spacer` or `%bar`.

    **Bar style** / **Bar: *style***
    :   Progress section and List view lines only. Steps through Bordered, Solid, Rounded, Metro, Wave and Pacman. Greyed out until the line has a `%bar`.

    **+ Bar** / **- Bar**
    :   Adds or removes the progress bar.

    **Bar height** / **Height: *N*%**
    :   30% to 200% of the text height. Default: 100%.

    **Cancel**
    :   Puts the line back as it was and closes.

    !shot:side token-picker | Insert token

    **Tokens…**
    :   Opens **Insert token**: a searchable list of tokens with a live preview of each, sorted into **All**, **Book**, **Authors**, **Progress**, **Time**, **Device**, **Logic** and **Style**.

    !shot:side icons-library | Icons library

    **Icons…**
    :   Opens the **Icons library**: a searchable grid of glyphs, with tabs **All**, **Dynamic**, **Device**, **Reading**, **Time**, **Symbols**, **Arrows**, **Blocks**, **Separators** and **SVG icon folder**.

    **Default**
    :   Resets the text and styling to the built-in default.

    **Save**
    :   Keeps your changes and closes.

### Cover display

**Bookshelf > Settings > Cover display**. Changes show on the shelf behind the menu.

!shot:side cover-display-menu | Cover display, page 1

**Cover captions: *choice***
:   The line under each cover: **Title**, **Author**, **Series**, **Custom…** or **None**. Custom opens a small line editor (Bold, Aa/AA, Tokens…, Icons…, Default, Save). A shelf can override this in its [View mode](#view-mode). Default: Title.

**Show author below series**
:   Prints the author under each series stack. Default: off.

**True cover aspect ratio**
:   Draws each cover at its real shape instead of a uniform rectangle. Default: off.

**Tallest cover shape: *N***
:   How tall a cover may be for its width before it is trimmed: **1.4**, **1.5**, **1.55 (default)**, **1.65** or **1.8**. Needs True cover aspect ratio.

**Square cover corners**
:   Square instead of rounded corners. Default: off.

**No cover drop shadow**
:   Flat covers with no shadow. Default: off.

**Default folder style: *style***
:   How folders and stacks look across the library: **Divider card**, **Ribbon**, **Book stack**, **Collage**, **Text** or **None**. Each shelf can override this. Default: Divider card.

**Show progress bars**
:   A thin bar on books you are reading. Default: on.

**Show reading bookmarks**
:   A bookmark on books you are partway through. Default: on.

**Page badge: *choice***
:   The pill in the bottom corner: **Off**, **Pages**, **Percent read** (books you are reading or have on hold) or **Percent read and pages**. Also in this submenu: **Number only** (drops the "p"), **Count: your reading settings** (default) or **Count: printed pages first**, and **Extract page counts…**. Default: Off.

!shot:side cover-display-menu-2 | Cover display, page 2

**Completed book badge: *choice***
:   **None**, **Bookmark style** or **Small tick box**. Default: Bookmark style.

**Fade finished books**
:   Draws finished covers faded. Default: off.

**On-hold display: *choice***
:   **None**, **Pause badge**, **Faded cover** or **Both**. Default: Both.

**Show series #: *choice***
:   The "#3" badge: **Always**, **Within series folder** or **Never**. Default: Within series folder (Always if you upgraded from an older version).

**Show favorites icon**
:   A mark in the cover's corner: on your favourites, or your star rating (see the next row). Default: on.

**Favorite icon or star rating: *choice***
:   **Heart (favorite)** or **Star (favorite)** on favourites, or **Stars (rating)**: every rated book shows its rating as a row of stars, closing up to fit on narrow covers. Default: Heart (favorite).

**Stack count badge: *choice***
:   A book count on stack tiles: **Off**, **Folders only**, **Groups only** or **All stacks**. Default: Groups only.

**Stack count format: *choice***
:   **Total**, or **Finished / Total**. Default: Total.

**Cover opening effect**
:   A short cover animation when you open a book. Default: on.

### List view

**Bookshelf > Settings > List view**. The lines that make up every row on List shelves. All List shelves share one layout. Two grey lines at the top say where the rest is: **Rows, columns and view are set per shelf:** **long-press a shelf, then open View mode.**

!shot:side list-view-menu | Bookshelf > Settings > List view

**Line 1: *preview*** ... **Line *N*: *preview***
:   Tap to open the line editor. Long-press for **Move up**, **Move down**, **Delete** and **Cancel**. Default: four lines (title with rating and favourite mark; author; description; a progress bar with percent read and page count).

**Add a line**
:   Adds a line at the end, up to six.

### Text size

!shot:side text-size-menu | Bookshelf > Settings > Text size

**Bookshelf > Settings > Text size**. Each row reads its size, such as **Shelf menu: 118%**, and opens a slim page at the bottom of the screen, so you can watch the change behind it. The page's title shows the value (**Shelf menu font scale: 118%**). Under it is a slider: tap or drag the track, or use the grey cards beside it (**−5** and **+5**, or **−1** and **+1** for the shelf menu and list text, with **−10** and **+10** outside them). A tick under the track marks the default. Footer: **Cancel** (puts back the size it opened with), **Default** (100%) and **Done**. A tap outside the page is **Done**; the X and Back are **Cancel**. Swipe left or right on the shelf behind to see the change on other pages. Every size starts at 100% and can go as low as 50%.

| Row | What it scales | Maximum |
|---|---|---|
| **Cover captions** | Text under covers | 300% |
| **Cover badges** | Series number and page badges | 200% |
| **Stack & folder labels** | Labels on stack and folder tiles | 300% |
| **Shelf menu** | Shelf button labels | 300% |
| **List text** | List view rows | 300% |
| **Top panel** | All top panel text | 200% |
| **Modules** | Module text | 200% |
| **Start menu** | Start menu entries | 200% |
| **Modal tabs** | Tab labels in the book menu | 200% |

### Bookshelf UI font

!shot:side ui-font-picker | The font picker

**Bookshelf UI font: *font***
:   The font for Bookshelf's own menus and labels. In the picker, **Default** follows KOReader's UI font; **Cancel** puts back the font it opened with and **Done** keeps the one picked. Default: Roboto Condensed (Follow KOReader if you upgraded from an older version).

### Image contrast

**Bookshelf > Settings > Image contrast**. Each row opens a slim slider page like the [text sizes](#text-size) (steps of 5 and 20), so you see the change on the shelf behind it. Swipe left or right on the shelf to judge it on other pages. All three start at 0%, which leaves the pictures as they are.

**Covers and ornaments contrast boost: *N%***
:   Deepens the shadows and lifts the light parts of covers, spines and ornaments, around each picture's own middle grey, which can help on a screen with few greys. 0% to 100%. Default: 0%.

**Wallpaper contrast: *N%***
:   The wallpaper quieter (down to -100%, one flat grey) or bolder (up to 100%). Default: 0%.

**Wallpaper brightness: *N%***
:   The wallpaper darker (down to -100%, black) or lighter (up to 100%, white). Default: 0%.

The two wallpaper rows are also under **Theme > Wallpaper**. None of the three is part of a theme.

### Modules

**Bookshelf > Settings > Modules**. Where modules can appear. Turn all four off to switch modules off entirely; the row then reads **Modules: Off**. See [Modules](../customise/micro-modules.md).

!shot:side micro-modules-menu | Bookshelf > Settings > Modules

**In the start menu**
:   Module cards in the start menu. Default: on.

**In the top panel**
:   Adds a grid button to the shelf menu that swaps the top panel for a grid of modules. Default: off (on if you upgraded from an older version).

**Full-screen button**
:   A footer button that opens all your modules full screen. Default: on (off if you upgraded from an older version).

**On the shelf**
:   Modules standing among a shelf's books. Off, shelves show only their books and ornaments, and the editor's **Modules** card and an ornament's **Pin to a spot** are not offered; the modules come back as they were when you turn it on. Default: on.

### Start menu

**Bookshelf > Settings > Start menu**

!shot:side start-menu-settings | Bookshelf > Settings > Start menu

**Start menu: *Left/Right/Off***
:   Which footer corner the start menu button sits in, or **Off** to hide it. Default: Left.

**Minimum start menu width: *default/N dp***
:   120 to 600 dp, on a slider page like the [text sizes](#text-size) (steps of 5 and 20), with the start menu open as a preview. Default: 180.

The buttons that open the start menu while reading are under **Advanced > While reading**.

### Behavior

**Bookshelf > Settings > Behavior**

!shot:side behavior-menu | Bookshelf > Settings > Behavior

**Top panel starts with: *choice***
:   **Currently reading** or **Modules**. Only shown while **Modules > In the top panel** is on. Default: Currently reading.

**Tap a book in full screen shelves: *choice***
:   **Show the book's details**, **Open with a single tap** or **Open with a double tap**. Default: Open with a single tap.

**Bookshelf gestures**
:   Switches for each of Bookshelf's own gestures, with **All gestures** at the top. A gesture you switch off does nothing, so a KOReader gesture can use it instead. All on by default. The full list is on the [Gestures](gestures.md) page.

**Double tap to open books**
:   Opening a book from the top panel, or from a cover on a full screen shelf, takes two taps; the first selects it. Default: off.

**Footer bar: *choice***
:   **Show**; **Hide**, where the shelf uses the bar's space (swipe to turn pages, and open the menu from KOReader's menu or a gesture); or **Invisible buttons**, where the bar isn't drawn but its buttons still work where they were, and moving into it with the keys shows it. Both hidden choices show the bar while you select books. Default: Show.

**Page turn animation: *speed***
:   A wipe when you turn shelf pages (e-ink only): **Off**, **Fast**, **Normal** or **Slow**. Default: Fast.

**Start menu animation: *speed***
:   The same for the start menu opening and closing. Default: Fast.

**Closing book notification**
:   Shows "Closing book…" while a book closes. Default: on.

### Library & search

**Bookshelf > Settings > Library & search**

!shot:side library-search-menu | Library & search, page 1

**Scan all library metadata**
:   Reads covers and details for every book under your home folder.

**Extract page counts…**
:   Opens the page count dialog. Under **Use page counts from, in this order**: **Publisher page numbers (fast)**, **Hardcover editions (fast)**, **Your reading settings (slow)**, **Calibre page column (fast)** and **Page counts in file names (fastest)**, all ticked by default. Under **Which books**: **Only books without a page count** (default) or **Every book, replacing earlier counts**. Buttons: **Delete scanned page counts…**, **Cancel**, **Start**. See [Page counts](../organise/page-counts.md).

    !shot page-count-dialog | Extract page counts

**Manage collections…**
:   Tap a collection for **Rename**, **Pin to shelf menu** and **Delete** (Favorites can only be pinned). Footer: **+ New collection**, **Close**.

    !shot manage-collections | Manage collections

**Bulk selection mode**
:   Closes the menu and starts [bulk selection](#bulk-selection).

**Author name formatting: *choice***
:   **Auto**, **First Last** or **Last, First**. Different spellings of the same author are merged either way. Default: First Last (Auto if you upgraded from an older version).

**Spine text direction: *choice***
:   **Top to bottom** or **Bottom to top**. Default: Top to bottom.

**Hide single-book series and genres**
:   Leaves series and genres with only one book out of those stacks. Default: off.

**Image library: *folder***
:   Where custom images for folders, series, authors and so on are kept. Default: `.bookshelf-images` in your home folder.

**Find author images online…**
:   Looks up a photo for every author without one (Open Library, then Wikipedia). Progress and a **Stop** button show in the status line.

**Include folder names in search results**
:   Default: off.

**Include genres and tags in search results**
:   Default: on.

**Show each book in one group only**
:   On Authors, Genres and Collections shelves, a book with several of them appears under its first one only (for collections, the one highest in KOReader's collection list). Search and filters still find it under all of them. Default: off.

**Ignore The, A, An when sorting**
:   Sorts titles by the word after a leading article. Default: on.

**Sort Chinese text by pinyin**
:   Default: off.

### Advanced

**Bookshelf > Settings > Advanced**

!shot:side advanced-menu | Bookshelf > Settings > Advanced

**Performance tweaks**
:   A submenu:

    !shot:side performance-tweaks-menu | Advanced > Performance tweaks

    - **Disable spine mode shadows**: flat spines with no shadows. Default: off.
    - **Plank designs: *plank***: off draws a plain plank colour instead of the plank picture. Default: on.
    - **Instant book close (beta)**: shows the shelf at once when you leave a book and finishes closing it later. Default: on.
    - **Use E-ink refresh rate for shelf pages**: shelf page turns flash clean as often as KOReader's own **Full refresh rate** (**Screen > E-ink settings**), to clear ghosting. A page that flashes skips its animation. E-ink only. Default: off.
    - **Pre-warm shelf cache**: gets each shelf ready in the background after launch. Default: on.
    - **"Latest" walk depth**: how many folders deep the Latest source looks, 1 to 99. Default: 3.
    - **Cover cache: *N* MB**: memory for scaled covers, 8 to 128 MB. Default: set from your device's memory.
    - **Clear cover cache**: empties the cover cache, and samples every spine's colour from its cover again.
    - **Color panel dithering**: colour e-ink only; keeps covers saturated. Default: on.

**While reading**
:   What Bookshelf draws inside the reader:

    !shot:side while-reading-menu | Advanced > While reading

    - **Show status line**: Bookshelf's status line across the top of the book. Default: off.
    - **Show menu button**: a start menu button in the reader. Default: off.
    - **Show modules button**: a full-screen modules button in the corner opposite the menu button. Takes effect the next time you open a book. Default: off.
    - **Launcher button position and size…**: edge and side offsets, size (50% to 150%), **Side: left/right** and **Edge: bottom/top**. Greyed out unless a button is on.

**Reset shelf menu to defaults**
:   After asking, puts back the fresh-install shelves and returns to Home.

**Reset top panel content to defaults**
:   After asking, puts back the fresh-install top panel layout and fonts.

**Read calibre metadata.calibre**
:   Reads Calibre's `metadata.calibre` file from your home folder or the folder above it. Default: off. See [Calibre, Kindle and Kobo libraries](../organise/other-libraries.md).

## The shelf editor

**Tap the button of the shelf you're on**, **long-press any shelf button**, or tap a shelf in **Edit shelves…**. Titled **Editing shelf: *name***. Every change applies and saves straight away, with the shelf redrawing behind; there is no Save button. For a walkthrough, see [Shelves](../organise/shelves.md) and [Sources, filters and sorting](../organise/sources-filters.md).

The front page is a set of cards, each showing its current value, two to a row: **Source** and **View mode**, **Filters** and **Sort**, **Theme** and **Modules** (one to a row on a narrow screen). A card opens a page inside the editor: its title is a breadcrumb such as *Home › Filters › Genre*, **Back** at its left goes back a page (the chevron alone when the title leaves no room), and the X at its right closes the editor. On a device with keys, the arrow keys move a focus ring through the cards and buttons.

!shot:side shelf-editor | The shelf editor

The strip under the title
:   **Edit shelf name** opens the **Shelf name** box with **Cancel**, **Insert icon…** (the way to give a shelf an icon) and **OK**. **Shelf order…** opens the [Shelf order](#shelf-order) page. At the right, **Copy** makes a copy right after this shelf, called "*name* (copy)", with the shelves inside it if it is a shelf of shelves, and opens its editor. **Move to…** opens a page with the **Shelf menu** and, under **Into a shelf of shelves**, each shelf of shelves this one can go into; where it is now is marked. With no shelf of shelves yet, it says how to make one.

**Source / grouping: *source***
:   Opens the [Source](#source) page. Changing the source resets the sort to that source's default. Giving a shelf of shelves another source deletes the shelves inside it, after asking.

**Filters: *None/N active***
:   Opens [Filters](#filters). On an online catalogue shelf this card is **Catalog settings** instead. On a shelf of shelves it is **Add shelf tile: *On/Off***, which shows or hides the tile for adding a shelf (default: On).

**View mode: *mode***
:   Opens [View mode](#view-mode). Reads **Covers**, **List**, **Spines**, **Auto**, or **Spines, face out** when some books stand face out.

**Sort: *levels***
:   Opens [Sort](#sort). Lists the levels in order, with the direction in brackets when it is not the usual one, such as **Sort: Added (Oldest first)**. Catalogue shelves show **Server order** instead; a shelf of shelves shows **Shelves stand in the order you arrange them**.

**Theme: *theme***
:   Opens the [Theme library](#theme-library) as a page of the editor. Default: **Default theme** (inside a shelf of shelves, **Same as *shelf***).

**Modules: *N* on this shelf** (or **Add to this shelf…**)
:   With none yet, opens the module library as a page; picking a module closes the editor and opens the shelf in the [layout editor](#layout-editor) with the new module selected. With some, a covers shelf opens the layout editor, and a spines shelf a **Modules** page listing them (tap one for its menu) with **Add module…**. Only on the shelf on screen. Greyed with the reason on a List shelf (**Not in List view**) or with **Settings > Modules > On the shelf** off (**Off in Settings**). See [On a shelf, among your books](../customise/micro-modules.md#on-a-shelf-among-your-books).

Footer
:   **Delete** removes the shelf after asking (any shelf can be deleted; deleting a shelf of shelves deletes the shelves inside it). **New shelf** adds a shelf right after this one (or inside the same shelf of shelves) and opens it on the Source page. **Close** closes the editor, as do a tap outside it and Back.

A shelf that has just been made and has no source yet shows **Choose a source to keep this new shelf.** above its cards.

### Shelf order

**Shelf editor > Shelf order…**. Every shelf at this shelf's level (the shelf menu, or the shelf of shelves it is in), drawn as on the shelf menu, with this one in black. Each has up and down arrows, so any of them can be moved from here; tap another shelf to open its own editor. Moves save at once.

### Source

**Shelf editor > Source / grouping**. The source in use is in black.

!shot:side source-picker | Source

| Section | Choice | What the shelf shows | Default sort |
|---|---|---|---|
| **Books** | **Home (flattened)** | Every book under your home folder, ungrouped | Surname, Series, Series # |
| | **Home (folders)** | Your home folder, grouped by folder | Filename |
| | **A folder**: **As folders ›** or **Flattened ›** | One folder as a tree, or every book in it and its subfolders | Filename, or Surname, Series, Series # |
| | **Recently read** | Books you have opened, latest first | Opened |
| | **Latest added** | Files on disk, newest first | Added |
| | **Favorites** | KOReader's Favorites collection | Opened |
| **Grouped: a stack for each** | **Series**, **Authors**, **Genres**, **Collections**, **Formats**, **Ratings**, **Languages** | A stack per series, author and so on | Groups by Opened (Series), Surname (Authors), Rating (Ratings) or Books (the rest) |
| **Just one** | **A series ›**, **An author ›**, **A genre ›**, **A collection ›**, **A format ›**, **A rating ›**, **A language ›** | The books of one of them; once picked, the chip names it (**A series: *name*** ›) | A series: Series #. An author or a rating: Series, Series #, Title. A genre or a language: Surname, Series, Series #. A collection: Collection order, then Opened. A format: Opened |
| **More** | **Shelf of shelves** | A shelf that holds other shelves | None |
| | **OPDS catalog ›** | An online catalogue | Server order |
| | **Kindle Virtual Library** | The Kindle's own library (Kindle, with its plugin) | Title |
| | **Kobo library** | Kobo store books (Kobo, with its plugin) | Title |

Sources from other plugins are listed under More.

The "Just one" pickers
:   A page of the editor with a searchable grid of cards, titled **Choose *kind***. Where the choices have book counts, a switch beside the search box sorts them **A-Z** or **Most books** first; the order you pick is kept for the next picker. The back arrow goes back to the Source page. **A rating** offers one to five stars or **Unrated**.

Folder picker
:   **Choose folder within home folder** lists every folder in your home folder that holds a book. **Browse device…** on the strip opens KOReader's own folder chooser so you can pick any folder.

Catalogue picker
:   **Choose OPDS catalog** lists your catalogues (shared with KOReader's own OPDS list). **Add catalog…** on the strip opens a form with **Catalog name**, **Catalog URL**, **Username (optional)**, **Password (optional)**, **Use server filenames** and **Sync catalog** (both off). Long-press a catalogue for **Edit** or **Delete**.

### Filters

**Shelf editor > Filters**. One card per filter, each showing **Any** or what is picked, with a cross to clear it. A line at the top says what the page is for ("Books matching the filters you choose below will show in this shelf."), with **Clear all filters** under it once any are set. A book must match every filter; each filter's page says how its own choices combine. The number beside a choice is how many books it would show with your other filters. No filters by default.

!shot:side filters-dialog | Filters

**Status**, **Language**, **Format**, **Rating**
:   A page of choices to tick, any of which a book can match: **Unread**, **Reading**, **On hold**, **Finished** for Status; **5 stars** to **1 star**, or **Unrated**, for Rating; the values in your library for the others, searchable, with the **A-Z** / **Most books** switch. **Clear** on the strip unticks them all; **Apply** in the footer (or the back chevron) keeps them and goes back.

**Genre**
:   Three lists, tagged **OR**, **AND** and **NOT**: **Any of these genres**, **All of these genres** and **Leave out these genres**, each with **+ Add genres**, which opens the same tick page for that list. Picks show as tags; tap one to remove it. A book needs one genre from the first list, every genre in the second and none from the third. An empty list is ignored.

**Collection**
:   Two lists, tagged **OR** and **NOT**: **In any of these collections** and **Leave out these collections**, each with **+ Add collections**. Picks show as tags; tap one to remove it.

**Series**
:   **Standalone and books in series**, **Only standalone books** or **Only books in series**.

**Folders**
:   **Only books in these folders** (**OR**, with **+ Add a folder**) and **Leave out these folders** (**NOT**, with **+ Add a folder to leave out**). Both pick from Bookshelf's own folder list, with **Browse device…** for any other folder. Each folder has a cross to remove it. Both cover sub-folders. Leave the first list empty to include every folder except those left out.

### Sort

**Shelf editor > Sort**. Up to three levels, side by side in the strip, each with its direction in words below it (**A-Z** / **Z-A**, **Oldest first** / **Newest first**, **Unread first** / **Finished first**, **Favorites first** / **Favorites last** and so on) and a cross to remove it. After the last level comes **Add a sort** or **Add a tie-breaker**. Tap a level to choose its key from the chips below; the shelf behind changes as you go.

!shot:side sort-picker | Sort

On a grouped shelf, the first level is **Order the groups by** and cannot be removed, and the next is **Sort the books inside each**.

??? note "Every sort key"

    | Chip | Sorts by | Usual direction |
    |---|---|---|
    | **Title** | Title | A-Z |
    | **Author** | Author's first name | A-Z |
    | **Surname** | Author's surname | A-Z |
    | **Filename** | File name | A-Z |
    | **Series** | Series name | A-Z |
    | **Series #** | Number in the series | 1, 2, 3 |
    | **Series + #** | Series name, then number | A-Z |
    | **Series or title** | Series name for series books, title for the rest | A-Z |
    | **Added/opened** | Whichever is later | Newest first |
    | **Added** | Date added | Newest first |
    | **Opened** | Last opened | Newest first |
    | **Progress** | Percent read | Most read first |
    | **Rating** | Your rating | Highest first |
    | **Unread 1st** | Unread, then reading, then finished | Unread first |
    | **Reading 1st** | Reading, then unread, then finished | Reading first |
    | **Favorite 1st** | Favourites first | Favorites first |
    | **Pages** | Page count | Shortest first |
    | **File size** | File size | Smallest first |
    | **Books** | Number of books in a stack | Most first |

    The chips sit under the headings **Book**, **Series**, **Reading**, **Status** and **Size**. The first level of a grouped shelf offers **Name** (**Full name** for authors), **Surname**, **Book count**, **Most recently read**, **Most recently added** and **Added/opened**. A shelf of one collection adds a **Collection** heading with **Collection order** (**Your order** / **Reversed**) and **Edit collection order ›**.

### View mode

**Shelf editor > View mode**. **Show as** comes first, then the settings of the style it shows, on the same page.

!shot:side shelf-style-auto | View mode: Auto

**Show as**
:   **Auto**, **Covers**, **List** or **Spines**. Default: Covers for a new shelf. Catalogue shelves have no Spines; a shelf of shelves has no Auto.

    Auto adds **Top level** (the shelf itself) and **Inside folders and stacks** (anything you open from it), each **Covers**, **List** or **Spines** (default Covers, then List). Below them, under **Settings**, a card for each level, such as **Top level: Covers ›**, opens that style's settings for it.

!shot:side shelf-style-list | View mode: List

**Columns** / **Rows** (List)
:   1 to 3 columns and 1 to 12 rows, with minus and plus; below 1 is **Auto**. Default: Auto. Under Auto with both levels on List, each level has its own.

!shot:side shelf-style-spines | View mode: Spines

**Face out: *summary*** (Spines)
:   Opens the **Face out** page: which books stand face out. Tick any of **Unread**, **Reading**, **On hold**, **Finished** (under **Reading status**); **First in series**, **First unread in series**, **Unread standalone** (under **Series**); **Favorites**, **Recently added** (with **How many of the newest**: 1, 3, 5, 10 or 20; default 5) and **In a collection** (which asks for the collection) under **Other**. Under **Whole shelf**: **All books** or **None**. A line at the top says what the page is for. Default: Favorites (Home ships with Favorites, Reading and the newest 5).

    !shot face-out-dialog | Face out

**Rows** (Spines)
:   1 to 6, or Auto. Default: Auto.

**Thickness** (Spines)
:   60% to 200%, in steps of 10%. Default: 100%.

**Book binding** (Spines)
:   **Hardback**, the classic look, or **Paperback**, with thin flush covers, softer shading and lighter page edges. A series can have its own from its long-press menu. Default: Hardback.

**Series boxes** (Spines)
:   **On** stands each series in an open slipcase. Default: Off.

**Author on spine** (Spines)
:   **On** or **Off**. Default: On.

**Ornaments** (Spines)
:   **None**, **Rarely**, **Often** or **Always**. Default: Often (Home ships with Always).

!shot:side shelf-style-covers | View mode: Covers

**Folder tiles** (Covers)
:   **Default setting**, **Divider card**, **Ribbon**, **Book stack**, **Collage**, **Text** or **None**. Default: Default setting (follows Cover display); the shipped Series shelf uses Collage and Genres uses Ribbon. Not on catalogue shelves.

**Cover captions: *choice*** (Covers)
:   Opens a page: **Default**, **None**, **Title**, **Author**, **Series**, or **A line of your own ›**, which opens the line editor. Default: Default.

### Catalog settings

**Shelf editor > Catalog settings**, for online catalogue (OPDS) shelves, in place of Filters. See [Online catalogues](../organise/opds.md).

**Starts at**
:   Where the shelf opens in the catalogue: **The top of the catalog**, or a subcatalog. Set it by long-pressing a subcatalog tile on the shelf and choosing **Start the shelf here**. **Back to the top** goes back.

**Saves downloads to**
:   **KOReader's download folder** (default) or **A folder of your own ›**.

**Refresh this catalog**
:   **Only when I swipe down** (default), **If it's over 5 minutes old**, **If it's over an hour old**, **If it's over a day old**, **If it's over a week old** or **Every time I open it**.

## On the shelf

### The book menu

**Long-press a book** (cover or spine) or **long-press the top panel**. It opens on the Edit tab. See [Opening and managing books](../use/book-menu.md).

!shot:side book-menu-edit | The book menu, Edit tab

Description
:   The blurb. If both the book and Hardcover have one, switch between **Embedded** and **Hardcover**.

**My review** / **Reviews**
:   Your own review (**Write a review** or **Edit**), plus Hardcover reviews for linked books, with **Refresh** and, when Hardcover has spoiler reviews for the book, **Include spoilers**.

Highlights
:   Only for a book with highlights, notes or bookmarks. Tap one to read it, with **View in book**.

Tags
:   Pills under **Author(s)**, **Series**, **Collections**, **Genres** and **Folder**; tap one to go there. One **Edit** button puts a cross on each tag you can remove and a **+ Add** after each group; **Done** ends it. Long-press a genre for **Rename**, **Pin to shelf menu** and **Delete**.

Edit
:   **Reading status** (**Unopened**, **Reading**, **On hold**, **Finished**), **Ratings** (your stars, and Hardcover's for a linked book), then **Actions**, a grid of cards: **Favorite**, **Remove from history**, **Show info**, **Select**, **Refresh metadata**, **Move…**, **Reset book data…**, **Delete**, and any other plugin's actions. Long-press a card to arrange them: pick a card, then **‹** and **›** move it, **Hide** / **Show** takes it off or puts it back, **Reset** puts back the usual order with nothing hidden, and **Done** ends it. With the Hardcover plugin on, a **Hardcover** row reads the link (or **Not linked**) with **Edit** or **Link…**, which opens a page: **Linked to *book*.**, **Use Hardcover's** **Cover** and **Description** (each **On** / **Off**), then **Link to Hardcover** or **Change link**: **Auto link**, **Manual link…**, **Select edition…** and **Clear link**.

Cover
:   Covers to choose from, with **Choose from device** and **Search online…** on the strip.

Footer
:   **Open**, zoom out and zoom in (long-press either to reset the size), **Close**.

### Group menu

**Long-press a stack or folder** (series, author, genre, collection, format, rating, language, folder, or a series box). A page of option cards, each with a line saying what it does. For a folder, **Move…**, **Rename…** and **Delete…** sit beside the book count at the top.

!shot:side group-menu | Group menu for a series

- **Shelf menu**: **Pin to the shelf menu** adds it as a shelf of its own, next to the one you are on.
- **Books**: **Select *N***, **Add *N* more** or **Remove *N*** for [bulk selection](#bulk-selection), and **Extract page counts…** for just these books.
- **Spines** (series only): **Book binding**, **Same as shelf**, **Hardback** or **Paperback**, for this series' books on every shelf. Default: Same as shelf.
- **Image**: **Set folder image…** and **Clear folder image** for a folder; **Set *kind* image…** and **Clear *kind* image** for a series, author, genre or collection. Authors also get **Find author image online**.

### Bulk selection

Start it from a book's **Select**, a group's **Select *N***, or **Settings > Library & search > Bulk selection mode**. Tap covers to select them. The footer shows an **X** to leave and a bucket with the count. Tap the bucket for the **Edit selected (*N*)** page:

!shot:side bulk-edit-selected | Edit selected

- At the top, what Apply will do, one change a line ("Pick what to change, then Apply." until you pick something), and **Select all in this shelf**.
- **Reading status**: **Unopened**, **Reading**, **On hold** or **Finished**.
- **Rating**: one to five stars, or **Clear**.
- **Collections**: **Favorite** **Add** or **Remove**, and a **Collections** row that opens a page of your collections: tap one to add the books to it, again to remove them from it, and again to leave it as it is.
- **Also on Apply**: **Refresh metadata** and **Remove from history**.
- **Right away**: **Move to folder…**, **Reset book data…** and **Delete…**, which act at once (Reset and Delete ask first).
- Footer: **Cancel**, **Apply**. Nothing above Right away changes until you apply. Tap a picked choice again to unpick it.

### Footer

!shot shelf-footer | The footer

**Settings > Behavior > Footer bar** can hide it, or keep its buttons but not draw them.

Chevrons
:   First, previous, next and last page. Long-press previous or next to skip ten pages.

Page counter
:   Tap for **Enter text, letter or page number** (on a Spines shelf, **Enter text, letter or book number**): **Search…**, **Go to letter**, **Cancel**, **Go to page** (or **Go to book**). Long-press to switch the shelf to the next view mode (Covers, List, Spines).

    !shot goto-dialog | Tap the page counter

Start menu button
:   Opens the start menu. Its corner is set in **Settings > Start menu**.

Modules button
:   Opens your modules full screen. Shown when **Settings > Modules > Full-screen button** is on. In the full-screen view, the pencil opens the layout editor.

### Top panel and shelf menu

!shot top-panel | The top panel

Top panel
:   Tap the cover to open the book. Tap the description to read all of it, the stars to rate, a tag pill to go there. Long-press for the book menu. Swipes are on the [Gestures](gestures.md) page.

Shelf menu
:   The book icon at the left shows the book you are reading. Tap a shelf to switch, long-press to edit it. The magnifier opens **Search library**. Long-press the **Search results** pill for the **Search results** page: **Show as** **Auto**, **Covers** (default), **List** or **Spines**. Under Auto, **Results** and **Inside folders and stacks** each pick **Covers**, **List** or **Spines** (default List for both). A shelf opened from the results keeps this view.

    !shot shelf-menu-row | The shelf menu

Modules grid button
:   Only with **Settings > Modules > In the top panel** on. Tap to swap the top panel for the module grid. Long-press for a page with **Reset to default** (puts back the modules the top panel starts with) and **Remove from the top panel** (**Settings > Modules > In the top panel** brings them back).

Add-shelf tile
:   On a shelf of shelves, while **Add shelf tile** is on. Tap it for the **Add shelf** page: **New shelf** (starts a shelf inside this one, on the Source page), then under **Move a shelf here**, each shelf that could move in, with where it is now (**In the shelf menu** or **In *name***).

### Start menu

**Long-press an entry** to edit it. See [The start menu](../use/start-menu.md).

!shot:side start-menu-edit | Editing a start menu entry

- **Rename**, **Icon…** (**Choose icon…**, **Remove icon**)
- **Module settings…** for modules
- Up and down arrows to move it
- **Move to folder…** / **Move out of folder**
- **Show in: *choice***: **Library and reader** (default), **Library only** or **Reader only**. Menu shortcuts also have **Auto**.
- Delete icon, and add icon, which opens **Add to menu**: **Plugin…**, **System action…**, **Menu action…**, **Bookshelf action…** (**Close bookshelf**, **Bookshelf menu**), **Bookshelf module…**, **New folder…** and **Divider**.

!shot start-menu-add | Add to menu

### Modules { #layout-editor }

**Long-press a module**, or the space between modules, in the top panel grid or the full-screen view (or tap the pencil in the full-screen view) for the layout editor. Everything but the grid fades, so the empty cells show as dashed outlines.

!shot:side module-longpress | The layout editor

- The toolbar for the selected module, titled with its name, with an X: a d-pad at the left moves it a cell; beside it, **Width** and **Height** with minus and plus, and **Page** with chevrons to send it to the page before or after; then **Settings** (the module's own), **Style** and **Remove**.
- **Style** sets this module's own card colours (**Card background**, **Card border**, **Card border color**, **Card text**, and any of the module's own), in a menu titled ***name* · style for Light** (or **Dark**), with **Reset**.
- The footer: **Add**, the page numbers (with a module selected, a number sends it to that page), **New page** (with a module selected) and **Done**. With nothing selected, it says **Tap a module to select it**.
- Gestures: tap a module to select it, swipe it to move it, pinch or spread on it to resize it, long-press an empty cell to add a module there, swipe sideways on an empty cell to turn the page.

**Add** opens **Modules**, with chips for **All**, **Shelf & books**, **Reading**, **Time & device**, **Fun & info**, **Actions**, each module pack, and **My modules**.

On a **covers shelf**, long-pressing a module among the books opens the same editor over the shelf, without **Height** (a module there is one row tall), page numbers or **New page**. On a **spines shelf** it opens a smaller menu: **Settings**, **Style** and **Remove** on its strip, then **Move it** (**Page**, **Left**, **Right**, **Page**; or swipe it on the shelf, a book at a time) and **Width**. A [pinned ornament](../customise/ornaments.md#pin-one-in-place) (the **Pinned ornament** module) has **Adjust ornament**, which opens the ornament's own menu, and **Unpin**, which puts it back among the others, in place of Settings, Style, Remove and Width.

The modules and their settings are listed on the [Modules](../customise/micro-modules.md) page.

### Ornament menu

**Long-press an ornament** on a Spines shelf. The shelf redraws behind it. Its picture and name are at the top, with an X to close.

!shot:side ornament-adjust | The ornament menu

- The strip: **Swap** (opens the ornament collection to pick a piece from any pack to take this one's place), **Hide** / **Show** (takes it out of the shelf's set, keeping its place), **Pin to a spot** (fixes it where it stands, as a [Pinned ornament](../customise/ornaments.md#pin-one-in-place) module), **Reset** (back to what its pack says), and at the right **Shuffle this shelf** (a new order for this shelf's ornaments, after asking). A pinned ornament has no Swap, Hide or Shuffle.
- **Size**, **Height** and **Padding**: a value with minus and plus (up and down chevrons for Height). A hold, or the **−10** and **+10** cards outside them, takes a bigger step; tap the value to reset it.
- **Place**: *N* of *M* in this shelf's order, with chevrons to move it earlier or later.
- **Mirror**: **Off**, **Always** or **Alternate**. **Anchor**: **Bottom** or **Top**.
- **On tap**: **None ›** until you give it a job (**Give this ornament a job!**). It opens **Tap action**: **No action**, **Zoom**, or any action the start menu can run.

## Updates

**Bookshelf > Updates**. See [Updating](updating.md).

!shot:side updates-menu | Bookshelf > Updates

**Check for updates (v*X*)**
:   Checks GitHub for a new release, offering to turn Wi-Fi on first. If there is one, you see the notes with **Update and restart**. Once a check has found one, the row names both versions.

**View changelog**
:   Release notes, with **‹ Older**, **Newer ›**, **Refresh** and **Close**. Kept for reading offline.

**Notify on wake when update available**
:   When the device wakes with Wi-Fi on, checks at most once an hour. Default: off.

**Developer updates**
:   For testing fixes before release:

    - **Development branch**: type a branch name, or leave it empty for stable.
    - **Install branch: *name***: downloads and installs that branch.
    - **Reset to latest stable release**: clears the branch and installs the latest release.
    - **Installed: v*X* (release)**: what you have now.
    - **Pack editor…**: for people making ornament packs.
