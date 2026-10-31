---
description: Ornaments are pictures that stand on the shelf between your books. Turn them on, place them, size them and make your own.
---

# Ornaments

Ornaments stand on the spines shelf among your books: a potted plant, a cactus, a framed print, a bat hanging from the shelf above. Bookshelf comes with two, and [theme packs](packs.md) bring many more.

!plank oak plant cactus

## Where they stand

Ornaments only appear on shelves shown as **Spines**. They have two kinds of spot:

- **The ends of a shelf.** A piece stands at the left or right end of a plank, and the books move along to make room. Empty planks below your last book count too, so a short shelf can still have something on the bare wood.
- **Between groups.** Where a series, an author's books or another group meets its neighbour, the gap can widen to hold a piece. If that gap falls at the start of a shelf, the piece stands before the first book. A shelf that doesn't group its books has no such gaps, so its pieces only stand at the ends.

<!-- TODO: a spines page with one piece at a shelf end and one in a gap between two series. -->

### How often

Each shelf sets its own: long-press its tab, then **View mode** > **Ornaments**, on a shelf shown as **Spines**.

| Level | Shelf ends | Gaps between groups |
|-------|------------|---------------------|
| **None** | none | none |
| **Rarely** | one shelf in four | none |
| **Often** | every other shelf | one in four |
| **Always** | every shelf | every other one |

A shelf you haven't changed uses **Often**. Home ships with **Always**.

The count runs on through the whole shelf, page after page, rather than starting again on each page. Which shelf in each run gets the piece, and which end it stands at, is mixed up so the pages don't all look alike (it never picks the same end three times running). The mix belongs to the shelf, so a page looks the same every time you come back to it. A series, author or folder you open from the shelf gets a mix of its own.

Adding or removing books can move the spots along, since they're counted by shelves and gaps.

### Which piece goes where

Each shelf deals its ornaments in an order of its own, going round again when it gets to the end: the first spot on the shelf takes the first ornament, the next spot the next one, and so on. The order is shuffled the first time a shelf uses it and then kept, so a shelf opens on the same pieces every time.

- **Place**, **Swap** and **Shuffle this shelf** (long-press an ornament) change the order on that shelf only.
- **Hide** takes an ornament off every shelf that wears the same theme. **Show** it again and it returns to its old place.
- New ornaments go to the front of your first spines shelf's order, so you see them, and somewhere at random in the others. To keep every shelf as it is, set **Bookshelf > Theme > New ornaments go** to **Last, so your shelf stays put**.

### How big

- A standing piece is 80% of the height of the books. By default it's no wider than the books are tall, and a wider picture is scaled down to fit rather than left out.
- **Size** goes past that, up to the whole width of the shelf. A piece that wide gets a shelf to itself.
- When a shelf needs room for a book, the piece at its end gives way: it shrinks, or leaves that shelf if it would come out under a quarter of its size.
- Anything drawn to hang over the front of the plank, like a tail or a trailing vine, is kept within the plank's depth. The piece is made smaller if it has to be.
- **Anchor** set to **Top** hangs a piece from the shelf above instead, like a bat. It's sized to fit between that shelf and its own plank, and on a page's top shelf it hangs from the bottom of the top panel.
- **Mirror** set to **Alternate** flips every second time the piece comes round on a shelf. **Always** flips every one.

## Which ones

<div class="walk" markdown>

<div markdown>

**Theme > Ornaments** opens the **Ornament collection**: everything installed, with a tab for **All** and one for each pack. The line under the pieces says whose set the checkboxes are: the theme of the shelf you opened it from, as in "On Plain shelves: 12 of 443. Check a piece to add it, uncheck to take it off."

- **Tap** an ornament to check or uncheck it, for that theme.
- **Long-press** one to **Hide** or **Show** it, or **Delete…** the file.
- **Select all** and **Select none** do a whole tab. Changes are kept as you go; close it when you're done.
- **Add ornaments…**, on the All tab, says which folder to copy your own into.

Each [theme](themes.md) keeps its own set, so the checkboxes change with the shelf you opened the collection from: a pack's shelf shows the pack's set, and Plain's starts empty.

</div>

!clip ornaments | The ornament collection, then adjusting one on the shelf.

</div>

!shot pack-ornament-collection | The Ornament collection, with three packs installed.

## Adjust one on the shelf

!shot:side ornament-adjust | Long-press an ornament on a spine shelf.

**Long-press an ornament** on the shelf. Its menu shows the piece and its name at the top, then a strip of actions:

| Action | Does |
|--------|------|
| **Swap** | Choose a different ornament for this spot, from any pack. |
| **Hide** | Take it off every shelf with this theme. **Show** brings it back. |
| **Pin to a spot** | Fix it where it stands (below). |
| **Reset** | Put the piece back the way its pack made it. |
| **Shuffle this shelf** | A new order for this shelf, after asking. Its swaps and moves are lost. |

Under them, the controls. The shelf redraws behind the menu as you go:

| Control | Does |
|---------|------|
| **Size** | Up to the whole row. |
| **Height** | Raise or lower it. |
| **Padding** | Space either side. Below zero tucks it behind the books. |
| **Place** | Move it along this shelf's order: it shows where it is, as in "3 of 12". |
| **Mirror** | **Off**, **Always**, or **Alternate** each time it comes round. |
| **Anchor** | **Bottom** stands it on its shelf; **Top** hangs it from the shelf above. |
| **On tap** | What tapping it does: **None**, **Zoom** to show it full screen, or any action. |

**Size**, **Height** and **Padding** step with **−** and **+**, and with **−10** and **+10** either side for bigger steps. Tap a value to put it back.

**Size**, **Padding**, **Height**, **Mirror**, **Anchor** and **On tap** follow the ornament onto every shelf. **Place**, **Swap** and **Shuffle this shelf** change only the shelf you're on.

### Pin one in place

Ornaments are dealt afresh as you page through a shelf. To keep one exactly where it stands, long-press it and tap **Pin to a spot**. It stays at that spot among the books, page after page, while the other ornaments carry on being dealt around it.

Long-press a pinned ornament for a smaller menu, titled **Pinned ornament**: **Adjust ornament** opens the controls above (its size, height, tap action and so on), **Unpin** puts it back among the others, and under **Move it**, **Page**, **Left**, **Right** and **Page** move it a book or a page at a time. You can also swipe it along the shelf. **Pin to a spot** needs **Settings > Modules > On the shelf** switched on. On a shelf of groups, such as series, it is only offered where the ornament stands between two groups.

!clip ornament-pin | Pinning Baphomet from the Halloween pack, then nudging it along.

## Make your own

Drop PNG or SVG files into `koreader/settings/bookshelf/ornaments` on your device. New ones turn up within a few seconds while the shelf is open, at the front so you see them.

- **PNG**: the bottom edge of the picture is the plank. Transparent space above makes it stand smaller.
- **SVG**: the bottom of the viewBox is the plank. Bold, solid shapes work best. `template.svg` in that folder is the potted plant, with notes inside on how to draw one.

A **folder** of ornaments inside `ornaments` becomes a pack, with its own tab and its own card in the Theme library. Add a `theme` folder with a `wallpaper.png` and it becomes a full theme. The details are in the [README](https://github.com/AndyHazz/bookshelf.koplugin#spines).
