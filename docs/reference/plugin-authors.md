---
description: Extend Bookshelf from another plugin or a user patch - shelf sources, tokens, cover placeholders, OPDS actions and micro-modules.
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

## Micro-modules

A [micro-module](../customise/micro-modules.md) is one small Lua file with a `render(ctx)` function. Drop it into `koreader/settings/bookshelf/micromodules/` to have it survive updates; a broken one is skipped rather than breaking the menu. The contract is in [micromodules/README.md](https://github.com/AndyHazz/bookshelf.koplugin/blob/master/micromodules/README.md), and the modules that ship with Bookshelf are good examples.

## Other book formats

Book formats another plugin registers with KOReader show on shelves like any other book. Bookshelf doesn't fetch covers for them itself, since that can mean a network request per book; a cover the file browser has already made still shows.
