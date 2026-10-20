---
description: Fixes for the common problems - Bookshelf not showing, an empty shelf, missing covers, odd page counts and slow screens.
---

# Troubleshooting

??? failure "There's no Bookshelf tab in the menu"
    - The Bookshelf tab only appears while the shelf or KOReader's file browser is on screen, not while a book is open. Close the book first.
    - Check the plugin folder is called exactly `bookshelf.koplugin`, with `main.lua` directly inside it. See [Install Bookshelf](../get-started/install.md).
    - Check KOReader is v2025.08 or newer: **Help > Version**. On anything older, Bookshelf shows a single line asking you to update.
    - Check it isn't switched off: **Tools > More tools > Plugin management** (the wrench tab).

??? failure "A notice says Bookshelf needs Cover browser"
    Bookshelf gets covers and book details from KOReader's **Cover browser** plugin. Turn it back on under **Tools > More tools > Plugin management**, then restart KOReader.

??? failure "KOReader doesn't open on the shelf"
    Set **Start with** to **bookshelf**: it's in the first tab of the menu, while on the shelf or the file browser. See [Open on startup](../get-started/startup.md).

??? failure "The shelf is empty"
    Bookshelf shows the books in KOReader's home folder. Tap **Set home folder** on the empty shelf, or see [Your home folder](../get-started/home-folder.md).

    If one shelf is empty but others aren't, check that shelf's **Filters**: long-press its tab. **Clear all filters** starts again.

??? failure "New books don't appear"
    Bookshelf notices new books on its own while the shelf is open. To check straight away, **swipe down** on the shelf. Books added outside your home folder won't appear.

??? failure "Covers are missing or wrong"
    - Long-press the book, **Edit** tab, **Refresh metadata**.
    - For the whole library: **Bookshelf > Settings > Library & search > Scan all library metadata**.
    - To choose a cover yourself: the book menu's **Cover** tab.
    - If covers or spine colours look stale after changing many books, **Bookshelf > Settings > Advanced > Performance tweaks > Clear cover cache**.

??? failure "All my spines are the same width"
    Spine width comes from the page count, and a book you've never opened has none. Run [Extract page counts](../organise/page-counts.md).

??? failure "The same author shows up twice"
    **Bookshelf > Settings > Library & search > Author name formatting** merges "Osman, Richard" and "Richard Osman". See [Series, authors and genres](../organise/groups.md#authors).

??? failure "An online catalogue won't download"
    Downloads need a home folder you've set yourself. See [Your home folder](../get-started/home-folder.md).

??? failure "One of my KOReader gestures stopped working on the shelf"
    Bookshelf may be using that gesture. Switch Bookshelf's off under **Bookshelf > Settings > Behavior > Bookshelf gestures**, and yours works again.

??? failure "Odd behaviour after installing a new version by hand"
    If you copied a new version in under a different folder name, the old one may still be there, and KOReader loads every copy it finds. **Bookshelf > About** lists any other copy of Bookshelf it finds. Delete the extra folder and restart.

??? failure "Screen refreshes look choppy"
    Try slower or no animations under **Bookshelf > Settings > Behavior**: **Page turn animation** and **Start menu animation**. On a colour screen, check **Color panel dithering** under **Advanced > Performance tweaks**.

??? failure "Leaving a book behaves oddly"
    Bookshelf shows the shelf the moment you leave a book and closes the book a moment later. If another plugin doesn't get on with that, turn off **Bookshelf > Settings > Advanced > Performance tweaks > Instant book close (beta)**.

## Still stuck?

Search the [issues on GitHub](https://github.com/AndyHazz/bookshelf.koplugin/issues), or open a new one. It helps to include your device, KOReader version (**Help > Version**), Bookshelf version (**Bookshelf > About**) and, if you can, a screenshot.
