---
description: Update Bookshelf from inside KOReader, read the changelog, and install a test build.
---

# Updating

Bookshelf updates itself over Wi-Fi. You don't need a computer.

## Check for updates

**Bookshelf > Updates > Check for updates** checks GitHub for a newer release. If there is one, you see its notes and **Update and restart**. If Wi-Fi is off, Bookshelf offers to turn it on.

Once a check has found an update, the **Updates** row itself says **Update available**, so you can see it without opening the menu.

## Also under Updates

**View changelog**
:   What changed in this and earlier releases, newest first. Notes you've opened once stay readable offline.

**Notify on wake when update available**
:   Off by default. When on, Bookshelf checks at most once an hour after the device wakes with Wi-Fi on, and shows a quiet notice if there's a new version. Nothing is fetched unless you turn this on or tap Check.

**Developer updates**
:   For trying a fix before it's released. Enter the **Development branch** name you've been given, tap **Install branch**, and Bookshelf installs it and restarts. **Reset to latest stable release** puts you back on the normal release.

## Updating by hand

Download the latest `bookshelf.koplugin.zip` from [Releases](https://github.com/AndyHazz/bookshelf.koplugin/releases/latest) and copy the folder over the old one, as in [Install Bookshelf](../get-started/install.md). Your settings are kept: they live in `koreader/settings/bookshelf`, not in the plugin folder.
