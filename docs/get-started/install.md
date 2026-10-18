---
description: Download Bookshelf, copy it into KOReader's plugins folder, and restart.
---

# Install Bookshelf

Bookshelf is a **plugin**: an add-on that KOReader loads when it starts, the way a browser loads an extension. Installing it means copying one folder onto your e-reader.

You'll need KOReader on your device first. If it isn't there yet, start with [Install KOReader](koreader.md).

## 1. Download

Get **`bookshelf.koplugin.zip`** from the [latest release](https://github.com/AndyHazz/bookshelf.koplugin/releases/latest) on GitHub. It's under **Assets** at the bottom of the release notes.

!!! tip "Use the release zip, not the green Code button"
    The release zip has the right folder name inside it. GitHub's **Code > Download ZIP** gives you a folder with the wrong name, which KOReader won't load.

## 2. Copy it to your device

Connect your e-reader to your computer with a USB cable, unzip the download, and copy the **`bookshelf.koplugin`** folder into KOReader's `plugins` folder. Where that is depends on your device:

=== "Kindle"

    `koreader/plugins/`, in the `koreader` folder at the top of the Kindle's drive, next to `documents`.

=== "Kobo"

    `.adds/koreader/plugins/`. The `.adds` folder is hidden: on a Mac press ++cmd+shift+period++ in Finder, on Windows tick **View > Hidden items**.

=== "PocketBook"

    `applications/koreader/plugins/`

=== "Android"

    `koreader/plugins/` in your device's internal storage.

=== "Linux and Mac"

    Linux: `~/.config/koreader/plugins/`. macOS: `~/Library/Application Support/koreader/plugins/`.

When you're done, the folder should look like this, with `main.lua` one level down and not two:

```text
koreader/
└── plugins/
    └── bookshelf.koplugin/
        ├── _meta.lua
        ├── main.lua
        └── ...
```

Then eject the device safely.

## 3. Restart KOReader

Plugins load when KOReader starts, so if it was already running, close it and open it again:

1. Tap the top edge of the screen to open KOReader's menu.
2. Tap the last tab, the one with three lines, and choose **Exit**.
3. Open KOReader again, the same way you did before.

KOReader opens on its usual file browser. Tap the top of the screen: the menu now has a **Bookshelf** tab, with an open-book icon, second from the left. Its first row, **Open Bookshelf**, puts your shelf on screen.

!shot bookshelf-tab-menu | The Bookshelf tab, with the shelf open

## 4. Make it your home screen

To have Bookshelf open every time KOReader starts, set **Start with** to Bookshelf. It takes ten seconds: see [Open on startup](startup.md).

## If it doesn't appear

??? failure "No Bookshelf tab in the menu"
    - Check the folder is called exactly `bookshelf.koplugin` and that `main.lua` is directly inside it.
    - Check your KOReader version under **Help > Version**. Older than v2025.08 shows a single line asking you to update KOReader, rather than the full plugin.

??? failure "A notice about Cover browser"
    Bookshelf needs KOReader's **Cover browser** plugin, which supplies covers and book details. It's on in a normal KOReader, but some other plugins ask you to turn it off. Turn it back on in KOReader's menu: the wrench tab, then **More tools > Plugin management**, then restart.

??? failure "The shelf is empty"
    Bookshelf shows the books in KOReader's **home folder**. See [Your home folder](home-folder.md).

## Updating later

You don't need to repeat these steps for new versions. Bookshelf can update itself from inside KOReader: see [Updating](../reference/updating.md).

[Next: your home folder :octicons-arrow-right-24:](home-folder.md){ .md-button .md-button--primary }
