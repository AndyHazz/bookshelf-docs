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

Each shelf sets its own: long-press its tab > **Shelf style**, then tap **Ornaments** to step through the levels.

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
- Switching an ornament off takes it off every shelf. Switch it back on and it returns to its old place.
- New ornaments go to the front of your first spines shelf's order, so you see them, and somewhere at random in the others. To keep every shelf as it is, set **Bookshelf > Theme > New ornaments go** to **Last, so your shelf stays put**.

### How big

- A standing piece is 80% of the height of the books. By default it's no wider than the books are tall, and a wider picture is scaled down to fit rather than left out.
- **Size** goes past that, up to the whole width of the shelf. A piece that wide gets a shelf to itself.
- When a shelf needs room for a book, the piece at its end gives way: it shrinks, or leaves that shelf if it would come out under a quarter of its size.
- Anything drawn to hang over the front of the plank, like a tail or a trailing vine, is kept within the plank's depth. The piece is made smaller if it has to be.
- **Anchor: top** hangs a piece from the shelf above instead, like a bat. It's sized to fit between that shelf and its own plank, and on a page's top shelf it hangs from the bottom of the top panel.
- **Mirror: alternate** flips every second time the piece comes round on a shelf. **Always** flips every one.

## Which ones

<div class="walk" markdown>

<div markdown>

**Theme > Ornaments** opens the **Ornament collection**: everything installed, with a tab for **All** and one for each pack.

- **Tap** an ornament to switch it off or on, for the theme on screen.
- **Long-press** one to switch it, or delete the file.
- **Select all** and **Select none** do a whole tab. **Apply** when done.

Which ornaments a shelf uses depends on its [theme](themes.md): Custom theme uses every one you've switched on, a pack uses its own, and Plain uses none.

</div>

!clip ornaments | The ornament collection, then adjusting one on the shelf.

</div>

!shot pack-ornament-collection | The Ornament collection, with three packs installed.

## Adjust one on the shelf

!shot:side ornament-adjust | Long-press an ornament on a spine shelf.

**Long-press an ornament** on the shelf. The shelf redraws behind the dialog as you go:

| Control | Does |
|---------|------|
| **Place** | Move it along this shelf's order. |
| **Size** | Up to the whole row. |
| **Padding** | Space either side. Below zero tucks it behind the books. |
| **Height** | Raise or lower it. |
| **Mirror** | **off**, **always**, or **alternate** each time it comes round. |
| **Anchor** | **bottom** stands it on its shelf; **top** hangs it from the shelf above. |
| **Tap** | What tapping it does: nothing, **Zoom** to show it full screen, or any action. |
| **Swap** | Choose a different ornament for this spot. |
| **Shuffle this shelf** | A new order for this shelf. |
| **Switch off** | Stop using it. |

**Size**, **Padding**, **Height**, **Mirror**, **Anchor** and **Tap** follow the ornament onto every shelf. **Place**, **Swap** and **Shuffle this shelf** change only the shelf you're on.

### Pin one in place

Ornaments are dealt afresh as you page through a shelf. To keep one exactly where it stands, long-press it and tap **Pin here**. It stays at that spot among the books, page after page, while the other ornaments carry on being dealt around it.

Long-press a pinned ornament for a smaller menu, titled **Ornament micro-module (pinned)**: **‹** and **›** nudge it one book along, **«** and **»** move it to the page before or after, **Settings** opens the controls above (its size, height, tap action and so on), and **Remove** unpins it. On a shelf of groups, such as series, **Pin here** is only offered where the ornament stands between two groups.

!clip ornament-pin | Pinning Baphomet from the Halloween pack, then nudging it along.

## Make your own

Drop PNG or SVG files into `koreader/settings/bookshelf/ornaments` on your device. New ones turn up within a few seconds while the shelf is open, at the front so you see them.

- **PNG**: the bottom edge of the picture is the plank. Transparent space above makes it stand smaller.
- **SVG**: the bottom of the viewBox is the plank. Bold, solid shapes work best. `template.svg` in that folder is the potted plant, with notes inside on how to draw one.

A **folder** of ornaments inside `ornaments` becomes a pack, with its own tab and its own card in the Theme library. Add a `theme` folder with a `wallpaper.png` and it becomes a full theme. The details are in the [README](https://github.com/AndyHazz/bookshelf.koplugin#spines).
