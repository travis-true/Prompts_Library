# Design Style Lab

Compare 25 visual styles across seven workplace layouts (175 examples), apply your content and brand settings, select an output direction, review accessibility findings, and download production briefs.

**[Open the public Design Style Lab](https://trueprompt-design-style-lab.travistrue1.chatgpt.site)**

## Included features

- Live headline, body and action-label editing.
- Web, PowerPoint, Word / PDF and social-graphic directions.
- Brand colors and system fonts with conflict guidance.
- Three-style comparisons, shareable selection links and device-local drafts.
- Separate optional motion settings with reduced-motion overrides.
- Computed contrast and readability checks with explicit manual-review limits.
- Card, page, dashboard, slide, job aid, form and dense-table examples.
- [Apply Design Style skill](../../skills/apply-design-style/SKILL.md), bundled with all 25 profiles.

## Run locally

No dependencies or build step are required. Serve `dist/` with any static web server. For example, from this directory:

```sh
python -m http.server 8080 --directory dist
```

Open http://localhost:8080. Clipboard features may require a secure context or localhost. Drafts stay in that browser's local storage; selection links omit entered content.

## Files and maintenance

`dist/index.html`, `app.js` and the CSS files are the editable website source. `data.js`, `profiles/`, `style-library.json` and `profile-standard.json` contain the shared design profiles. `dist/skill/` contains a portable skill copy; keep it aligned with the canonical skill above. No Site credentials or hosting identity are included.

The live Site uses separate Sites hosting; a GitHub commit does not automatically redeploy it. Publish updates through Sites after synchronizing the source. This directory is also portable to other static hosts.

## Output and validation limits

Format selectors provide HTML previews and production prompts, not native Office, PDF or image exports. Contrast checks composite solid background colors; gradients, blur, imagery, keyboard operation, screen-reader behavior and final exported artifacts require further review. The styles are original interpretations, not recovered reference-video code.
