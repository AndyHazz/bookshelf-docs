---
description: Where to find the official, up-to-date guides for installing KOReader on Kindle, Kobo, PocketBook, Android and more.
---

# Install KOReader

Bookshelf is a plugin for [KOReader](https://koreader.rocks/), a free reading app that runs on most e-readers. If KOReader is already on your device, skip to [Install Bookshelf](install.md).

[KOReader's own wiki](https://github.com/koreader/koreader/wiki) keeps a guide for each kind of device, written by the people who make KOReader and kept up to date as firmware changes.

!!! info "Which KOReader version?"
    Bookshelf needs **KOReader v2025.08 or newer**, and works best on **v2026.03 or newer**. Get the latest from [KOReader's releases page](https://github.com/koreader/koreader/releases/latest). Already installed? Check yours in KOReader's menu under **Help > Version**.

## Pick your device

=== "Kindle"

    A Kindle has to be **jailbroken** before it can run KOReader. That sounds alarming, but it's a well-trodden path with a friendly guide. In short:

    - Your Kindle keeps working as before: the store, your Kindle books and the normal home screen are all still there. KOReader is an extra app you open when you want it.
    - Set aside an hour or so, and follow each step exactly.
    - Bookshelf itself is easy to remove later: it's one folder.

    1. **Find your jailbreak.** The method depends on your Kindle model and firmware version. The [Kindle Modding wizard](https://kindlemodding.org/jailbreak-wizard.html) asks a few questions and sends you to the right guide.
    2. **Follow that guide** on [kindlemodding.org](https://kindlemodding.org/jailbreaking/), including its steps for [stopping automatic updates](https://kindlemodding.org/jailbreaking/prevent-auto-update/).
    3. **Install KOReader** with [KOReader's Kindle guide](https://github.com/koreader/koreader/wiki/Installation-on-Kindle-devices). It tells you which package to download for your model.
    4. **Open KOReader** the way that guide describes: from the **KUAL** launcher, or from the KOReader item in your Kindle library, depending on how you installed it. Exiting KOReader takes you back to the normal Kindle home screen.

    !!! warning "Before you start"
        - Check the wizard **before** updating your Kindle or registering it. A firmware update can close the door on a jailbreak, or remove one you already have.
        - Follow each guide's advice on Wi-Fi and airplane mode exactly. Some steps need Wi-Fi off, others need it on.
        - Jailbreaking is done at your own risk. It is a community effort, separate from KOReader and from Bookshelf.

=== "Kobo"

    No jailbreak needed. The easiest route is NiLuJe's **one-click install package**, which installs KOReader along with a launcher so it shows up in your Kobo's own menu.

    - [KOReader's Kobo guide](https://github.com/koreader/koreader/wiki/Installation-on-Kobo-devices) explains every method and recommends the one-click package for most people.
    - [The one-click packages](https://www.mobileread.com/forums/showthread.php?t=314220) (MobileRead), with helper scripts for Windows, macOS and Linux.
    - [NickelMenu](https://github.com/pgaskin/NickelMenu) is the launcher that adds KOReader to the Kobo menu. It keeps working after Kobo firmware updates.

=== "PocketBook"

    - [KOReader's PocketBook guide](https://github.com/koreader/koreader/wiki/Installation-on-PocketBook-devices): unzip the PocketBook package and copy its folders onto the device. KOReader then appears under your apps.

    Android-based PocketBooks follow the Android route instead.

=== "Android"

    KOReader isn't on Google Play. Install it from F-Droid or straight from KOReader's releases.

    - [KOReader on F-Droid](https://f-droid.org/packages/org.koreader.launcher.fdroid/), which keeps it updated for you.
    - [KOReader's Android guide](https://github.com/koreader/koreader/wiki/Installation-on-Android-devices), if you'd rather install the APK yourself.

=== "reMarkable"

    - [KOReader's reMarkable guide](https://github.com/koreader/koreader/wiki/Installation-on-reMarkable) covers the reMarkable 1, 2 and Paper Pro. It recommends installing with a desktop helper app.

=== "Linux and others"

    - [Desktop Linux](https://github.com/koreader/koreader/wiki/Installation-on-desktop-Linux): `.deb`, AppImage or [Flathub](https://flathub.org/apps/rocks.koreader.KOReader).
    - [macOS](https://github.com/koreader/koreader/wiki/Installation-on-MacOS) and [Chromebook](https://github.com/koreader/koreader/wiki/Installation-on-Chromebook-devices) have guides too.
    - Every supported device is listed in the sidebar of [KOReader's wiki](https://github.com/koreader/koreader/wiki).

## Learning KOReader itself

You don't need to know KOReader well to use Bookshelf, but a little helps. [KOReader's user guide](https://koreader.rocks/user_guide/) covers reading features, and the [Getting started page](https://github.com/koreader/koreader/wiki/Getting-Started) on its wiki is a good first read.

The one thing worth knowing now: **tap the top edge of the screen** to open KOReader's menu. Bookshelf's settings live there, under its own tab.

[Next: install Bookshelf :octicons-arrow-right-24:](install.md){ .md-button .md-button--primary }
