# Export and accessibility standards

## Raster and video
- **PNG**: favor for crisp text, logos, charts, and flat color.
- **JPEG/JPG**: favor for photographic artwork when smaller file size matters; export at visually high quality.
- **WebP**: only if explicitly supported by the destination uploader; never assume it is accepted.
- **MP4 (H.264 video, AAC audio)**: common interoperability baseline for short-form video, but check current platform limits, codec, duration and file size.
- Use **sRGB** for general web/raster work unless the platform specifically calls for something else; do not use CMYK for ordinary web image exports.
- **Pixel width × height**, not DPI/PPI metadata, determines on-screen raster dimensions. The source image's “US standard” label does not change this.
- Do not infer platform maximum file size from this skill. Confirm the specific uploader limit when relevant.

## Source-to-export workflow
1. Retain high-resolution artwork and editable layers if possible.
2. Crop/recompose deliberately to the target aspect ratio; do not nonuniformly stretch faces, text or logos.
3. Export exact target pixel dimensions; inspect image clarity after compression.
4. Preview at mobile scale; inspect text readability, contrast and overlays.
5. For a campaign, export a distinct file per placement.

## Readability and accessibility
- Prefer short headlines and strong visual hierarchy, avoiding extremely small or thin text.
- Aim for at least **4.5:1 contrast** for ordinary text and **3:1** for large text where practical; evaluate text over busy image areas carefully.
- Provide useful alt text/captions in the post or handoff when the platform supports them.
- Avoid communicating meaning through color alone.
- Include captions/subtitles for spoken content; avoid flashing elements likely to distract or harm.
- Review sensitive cropping: faces, logos, charts, and embedded legal text should not be cut off.

## Naming and handoff
Use `campaign_platform_placement_WIDTHxHEIGHT_v01.ext` (example: `launch_instagram_story_1080x1920_v01.png`). Include account surface where it matters (e.g. `linkedin_personal-cover`, `linkedin_company-cover`).

Handoff summary: platform, placement, dimensions, format, file size, whether actual export dimensions were inspected, crop/safe-zone review, source of any current specification, and any unresolved publishing constraint.
