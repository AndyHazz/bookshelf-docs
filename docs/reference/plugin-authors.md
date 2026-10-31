---
description: Extend Bookshelf from another plugin or a user patch - shelf sources, tokens, cover placeholders, OPDS actions and modules.
---

# For plugin authors

Bookshelf has a few small, stable ways for other plugins (and KOReader user patches) to add to it. All go through `ui.bookshelf`.

## Shelf sources

Put your own books on a shelf: a server's catalogue, a store's library, anything that isn't files Bookshelf walks. The reader adds a shelf, picks your source under **Source / grouping**, and it behaves like any other shelf.

```lua
local function register(ui)
    local bs = ui and ui.bookshelf
    if not (bs and bs.registerSource and (bs.SOURCE_API or 0) >= 1) then
        return false
    end
    return bs:registerSource("komga", MySpec)
end
```

Bookshelf's own Kindle and Kobo library shelves use the same interface. The full guide is [SOURCE_API.md](https://github.com/AndyHazz/bookshelf.koplugin/blob/master/SOURCE_API.md).

## Tokens

`registerTokens(id, defs)` adds tokens of your own to every template: the top panel, cover captions and list lines. The spec is at `Tokens.register` in `lib/bookshelf_tokens.lua`.

## Cover placeholders

`registerPlaceholder(id, fn)` draws the card for books without a cover, in place of Bookshelf's lettering. The contract, and how a user patch registers before the plugin has loaded, are at the top of `lib/bookshelf_placeholders.lua`.

## OPDS book actions

`registerRecordActions(id, fn)` adds buttons to an online catalogue book's download view. The contract is at the top of `lib/bookshelf_record_actions.lua`.

## Modules { #micro-modules }

A [module](../customise/micro-modules.md) is one small Lua file with a `render(ctx)` function. Drop it into `koreader/settings/bookshelf/micromodules/` to have it survive updates; a broken one is skipped rather than breaking the menu. The contract is in [micromodules/README.md](https://github.com/AndyHazz/bookshelf.koplugin/blob/master/micromodules/README.md), and the modules that ship with Bookshelf are good examples.

To let readers install and update your modules from the device, ship them as a **module pack**: a small KOReader plugin with a `bookshelf_modules/` folder beside its `main.lua`. KOReader's plugin stores install and update it like any plugin, and Bookshelf finds the modules inside. Its modules get a chip of their own in the module library, under the plugin's name; a spec's `pack` or `category` field puts a module in a named pack or one of Bookshelf's groups instead. Both are in the README, under *Publishing a module pack* and *Picker chips*.

A few helpers in the module kit (`lib/bookshelf_module_kit.lua`) are there for packs:

- **`self_sized = true`** in a module's spec, for one that sizes itself: pixel art that only looks right at whole steps, an image, a widget built for another host. Bookshelf renders it once at its cell's size, instead of trying it at several scales until it fits.
- **`Kit.plugin(MODULE_DIR)`** finds your own plugin's running instance, by its folder, so a module can show the plugin's state (a pet, a game, a reading log). It's `nil` when the plugin isn't running.
- **`Kit.setOnHomeShelf(key, on)`** puts your module first on the reader's home shelf (the first shelf that holds books), or takes it off; **`Kit.onHomeShelf(key)`** says whether it's there. Call it only from something the reader chose, such as a tick in your settings, and check the function exists first so an older Bookshelf reads as not installed.

The README has the details and examples.

## Other book formats

Book formats another plugin registers with KOReader show on shelves like any other book. Bookshelf doesn't fetch covers for them itself, since that can mean a network request per book; a cover the file browser has already made still shows.
