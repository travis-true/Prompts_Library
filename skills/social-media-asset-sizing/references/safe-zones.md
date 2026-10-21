# Safe zones and crop behavior

## Principle
A pixel-perfect canvas can still fail when the platform adds captions, buttons, masks or responsive crops. Do not equate full upload area with reliably visible content.

## General conservative design guidance (not platform guarantees)
- On ordinary feed artwork, keep vital text/marks at least **5% of canvas width/height** inside the edge; increase margin for busy frames.
- On vertical stories and short-form video, keep essential words and calls to action in a central area; reserve **roughly 15% top and 20% bottom** as a conservative *starting guide*, and avoid right-side controls. These are **not official universal safe-zone measurements**. Preview on the destination platform.
- For circular avatars, use a square source and keep important elements within its **central inscribed circle**. Keep a little additional inset within the circle for comfortable breathing room.
- Banners are device- and account-specific; preview mobile/desktop variations and avoid putting essential type at the edge.

## YouTube channel banner
- Canvas: **2560×1440 px**.
- Widely used cross-device central safe area: approximately **1546×423 px**. Center it at x≈507–2053 and y≈509–931. This is a **content guide**, not a separate upload size. Exact pixel interpretations can vary slightly among sources; keep additional breathing room.
- Extend atmospheric/background design across the entire canvas, with channel name/logo/tagline inside the center safe area.

## X header
- Canvas preset: **1500×500 px**. Leave tolerance around the bottom-left profile photo overlap and other responsive crops; do not assume a universal numerical safe region.

## LinkedIn
- **Personal** background: **1584×396 px**; profile photo and controls may overlap. Keep primary message centered/right while previewing both mobile and desktop.
- **Company Page** cover is a different asset. Official LinkedIn documentation explicitly warns that cover photos can be cropped and recommends avoiding important content near edges, especially lower-right; verify current UI before release.

## Composition checks
1. Can the main subject and headline survive center crop, square crop, and portrait crop?
2. Are all important words legible at typical phone display size?
3. Does an avatar or native app UI block anything important?
4. Does a circular mask cut through faces, words, or logos?
5. Is the alternative/mobile crop acceptable?

Record a manual preview as **completed** only if someone actually inspected it.
