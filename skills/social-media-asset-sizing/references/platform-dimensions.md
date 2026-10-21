# Platform dimensions — reference presets

**Status:** Working presets extracted or normalized from the user-supplied graphic on 2026-10-19. **Not a live certification of every platform's latest specifications.** Dimensions are **width × height in pixels**. A listed ratio is computed from dimensions, not blindly copied from the graphic. Some entries are deliberately labeled `CHECK` where the graphic is outdated, ambiguous, or internally inconsistent. Confirm official requirements before publication.

| Platform | Placement | W×H px | Actual ratio | Status / practical note |
|---|---|---:|---|---|
| Instagram | Square feed post | 1080×1080 | 1:1 | Common preset |
| Instagram | Portrait feed post | 1080×1350 | 4:5 | Common preset; feed/grid cropping can differ |
| Instagram | Story / Reel | 1080×1920 | 9:16 | Keep text out of interface overlays |
| Instagram | Profile avatar | 320×320 | 1:1 | Circle mask; use higher-resolution source if possible |
| YouTube | Channel banner | 2560×1440 | 16:9 | Only center safe area reliably visible on all devices; see safe-zones |
| YouTube | Video thumbnail | 1280×720 | 16:9 | Conventional landscape preset |
| YouTube | Short | 1080×1920 | 9:16 | Video canvas; thumbnails/preview handling may differ |
| Facebook | Square feed post | 1200×1200 | 1:1 | Graphic reference; other supported ratios vary |
| Facebook | Portrait feed post | 1200×1500 | 4:5 | Graphic reference; placement-dependent |
| Facebook | Cover image | 820×312 | ~2.63:1 | CHECK: graphic's '16:9' label is mathematically wrong; cover displays/crops vary by device |
| Facebook | Story | 1080×1920 | 9:16 | UI overlays vary |
| X | Square post | 1024×1024 | 1:1 | Graphic preset, not exclusive |
| X | Portrait post | 1024×1280 | 4:5 | Graphic preset; display crops vary |
| X | Header | 1500×500 | 3:1 | Protect left/bottom areas from avatar overlays |
| X | Avatar | 400×400 | 1:1 | Circular display mask |
| TikTok | Vertical video | 1080×1920 | 9:16 | Common preset; avoid caption/action overlays |
| TikTok | Cover artwork | 1080×1080 | 1:1 | CHECK: source graphic calls it 'cover image'; not a universal video-cover requirement |
| TikTok | Avatar | 200×200 | 1:1 | Working graphic reference |
| LinkedIn | Square feed post | 1200×1200 | 1:1 | General artwork preset |
| LinkedIn | Portrait feed post | 1200×1500 | 4:5 | Graphic reference; preview crop varies |
| LinkedIn | Personal profile background | 1584×396 | 4:1 | Graphic banner; **not** a LinkedIn company Page banner |
| LinkedIn | Personal avatar | 400×400 | 1:1 | Circle display mask |
| LinkedIn | Company Page logo | 400×400 | 1:1 | Official recommended company Page logo (checked 2026-10-19) |
| LinkedIn | Company Page cover | 4200×700 | 6:1 | Official recommended company Page cover (checked 2026-10-19) |
| Pinterest | Vertical Pin | 1000×1500 | 2:3 | Source graphic correct |
| Pinterest | Square Pin | 1000×1000 | 1:1 | Source graphic |
| Pinterest | Board cover | 800×450 | 16:9 | Graphic reference; board-cover behavior should be checked |
| Pinterest | Avatar | 165×165 | 1:1 | Graphic reference; may describe display size rather than ideal upload |
| Snapchat | Story / Spotlight | 1080×1920 | 9:16 | Source graphic |
| Snapchat | Square snap artwork | 1080×1080 | 1:1 | CHECK: not a universal placement requirement |
| Snapchat | Avatar | 320×320 | 1:1 | CHECK: platform account/avatar model differs by surface |
| Reddit | Square post | 1080×1080 | 1:1 | Graphic preset |
| Reddit | Portrait post | 1080×1350 | 4:5 | Graphic preset |
| Reddit | Community banner | 2560×1024 | 2.5:1 | CHECK: graphic incorrectly labels this '16:9'; rendering depends on community UI |
| Reddit | Avatar | 256×256 | 1:1 | Graphic reference |
| Twitch | Channel banner | 1920×1080 | 16:9 | Source graphic; channel background/display behavior varies |
| Twitch | Panel | 320×160 | 2:1 | Source graphic |
| Twitch | Offline screen | 1920×1080 | 16:9 | Source graphic |
| Discord | Server banner | 960×540 | 16:9 | Feature/plan restrictions may apply |
| Discord | Server icon | 1024×1024 | 1:1 | Circle rendering/crop can apply |
| Discord | User avatar | 128×128 | 1:1 | CHECK: likely display/reference size, not necessarily recommended master upload |
| Spotify | Playlist cover | 3000×3000 | 1:1 | Source graphic; CHECK current upload limits |
| Spotify | Profile avatar | 320×320 | 1:1 | Graphic reference |
| Spotify | Banner | 2480×1365 | ~1.82:1 | CHECK: source labels 16:9 but 2480÷1365≈1.817; placement ambiguous |

## Corrections and ambiguity in the original image
- Instagram portrait **1080×1350 is 4:5**, not a US-specific standard.
- Pinterest vertical Pin **1000×1500 is 2:3**.
- Facebook cover **820×312 is ≈2.63:1**, not 16:9.
- Reddit banner **2560×1024 is 2.5:1**, not 16:9.
- Spotify banner **2480×1365 is ≈1.82:1**, not 16:9.
- LinkedIn **1584×396** applies to a **personal** profile background. Company Page specifications are distinct.
- Twitch panel **320×160 is 2:1** (the figure uses pixel dimensions rather than ratio there).
- Some avatar dimensions may be display sizes rather than recommended source artwork; prefer crisp larger masters and verify uploader constraints.

## When a placement is missing
Do **not** invent an authoritative size. Ask for the exact placement or search its current official documentation. If only a general design direction is needed, explicitly label the selected pixels as a **design preset**, not a platform rule.
