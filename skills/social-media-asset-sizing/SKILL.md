---
name: social-media-asset-sizing
description: "Select, adapt, export, and quality-check social-media image and video dimensions across Instagram, YouTube, Facebook, X, TikTok, LinkedIn, Pinterest, Snapchat, Reddit, Twitch, Discord, and Spotify. Use for posts, stories, reels, shorts, thumbnails, covers, banners, avatars, and cross-platform creative variants."
---

# Social Media Asset Sizing

## Purpose
Help produce platform-specific social assets with correct pixel dimensions, coherent composition, accessible text, and documented validation. This skill provides design and sizing guidance; it does not itself create images, edit media, or publish posts. Use available media-generation/editing or file tools when required.

## Workflow
1. **Identify destination.** Determine platform, asset type (feed post, story, short, thumbnail, banner, avatar, etc.), account surface (personal/company/channel), and output format. If omitted, infer from the user's explicit context; otherwise ask only the critical missing question. Do not treat a company's banner as the same asset as a personal profile cover.
2. **Find a candidate preset.** Read `references/platform-dimensions.md`. Its values are starting presets, *not* promises of current upload limits or display behavior. Select by platform **and** asset type, not by aspect ratio alone.
3. **Verify when current correctness matters.** For a final deliverable, publication, advertisements, or platform-specific upload constraints, consult official platform documentation if browsing is available. Record source and date. If not checked, label platform acceptance as **unverified**. When live official guidance conflicts with a reference, prefer the official guidance and explain the adjustment. Never claim a platform rule is verified solely because it appears in the supplied image.
4. **Compose for cropping.** Use `references/safe-zones.md`; protect logos, faces, calls to action and text. Check circle-masked avatars and changing banner crops. For multi-platform work, recompose each canvas, not just stretch it.
5. **Prepare export.** Follow `references/export-standards.md`. Pixel dimensions (not DPI or a supposed “US standard”) determine raster canvas size. Keep source layers editable where available; export deliverables separately.
6. **Validate.** Follow `references/quality-checklist.md`. If a local image and Python/Pillow are available, run `python scripts/validate_assets.py path/to/file.png --width 1080 --height 1920` to verify pixel dimensions and format. Review actual text placement manually; a dimension check is not a crop or accessibility audit.
7. **Report accurately.** Provide destination, asset type, final W×H px, reduced aspect ratio, file format, safe-zone considerations, and verification status. Disclose any unperformed checks. Never say an image or platform upload was tested when it wasn't.

## Default decisions
- **Vertical short-form content:** use a 1080×1920 (9:16) candidate, adjusting UI-safe regions for the destination.
- **Square general feed artwork:** use 1080×1080 (1:1) as a portable baseline, but prefer platform-specific presets when known.
- **Portrait feed art:** avoid one-size-fits-all assumptions: Instagram 1080×1350 (4:5) remains a useful composition preset; other platforms may crop or display differently.
- **Landscape video thumbnails:** use 1280×720 (16:9) as a YouTube candidate.
- **Headers, banners, and profile images:** always select by the exact destination. Aspect ratios and visible areas vary substantially.

## Rule hierarchy
1. User-approved dimensions or publishing brief, unless technically incompatible with a stated target.
2. Current official platform upload and rendering requirements.
3. Verified project-specific brand/template requirements.
4. Presets in this skill.
5. Conservative default compositions.

When rules conflict, identify the conflict and propose the smallest safe adjustment; do not silently override a mandatory requirement. If the user requests an unusual custom dimension, honor it and note that platform suitability is unverified unless confirmed.

## Multi-platform adaptation
- Start from the highest-resolution suitable master with separate text, subject, logo, and background layers.
- Produce individual canvases for each selected placement.
- Preserve message, brand and focal point; change line breaks, positioning and crop as needed.
- Do not enlarge low-resolution sources and represent the result as genuinely higher detail.
- Name exports using `campaign_platform_asset_widthxheight_v01.ext`.

## Files to consult
- `references/platform-dimensions.md` — platform matrix, caveats, corrections to the supplied graphic
- `references/safe-zones.md` — margins, masks, UI overlays and preview behavior
- `references/export-standards.md` — format, color, compression, filenames and accessibility
- `references/quality-checklist.md` — QA and handoff status
- `references/sources.md` — provenance and update guidance
- `scripts/validate_assets.py` — optional local raster validation

## Important interpretation
The source infographic calls its sizes “US standard.” Social-platform pixel sizes are **not region-specific US measurement standards**. It also mixes upload canvas sizes with displayed sizes and contains some inconsistent ratios. The corrected, annotated matrix must not be treated as a complete or independently verified platform policy.
