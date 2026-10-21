# Release / quality checklist

Use **PASS**, **FAIL**, or **NOT CHECKED** for each row. No item passes by assumption. An overall **PASS** requires all mandatory checks to pass; if actual upload behavior is not tested, describe it as **not verified in platform**.

| Check | Acceptance evidence |
|---|---|
| Correct placement | Exact platform and account/surface identified |
| Current requirements | Official/current spec consulted where release needs it; otherwise explicitly `NOT CHECKED` |
| Exact dimensions | Export inspected by image metadata or video probe |
| Correct aspect ratio | Computed W÷H matches requested geometry |
| No unintended distortion | Subject, text and logos are not stretched |
| Safe content area | Visually reviewed for app overlays, edge margins and responsive crops |
| Text legibility | Read at typical mobile scale; no unintended clipping |
| Contrast / accessibility | Contrast and color-only meaning reviewed; alt-text/caption guidance prepared as applicable |
| Appropriate export | Supported candidate format, crisp output, appropriate compression |
| Naming | Platform, placement and dimensions distinguish variants |
| Preview | At least one relevant rendered preview actually inspected |
| Publication acceptance | Mark `NOT CHECKED` unless actual platform upload/display was tested |

## Suggested status summary
`File: <name> | Destination: <platform/placement> | Dimensions: <W×H> | Geometry: PASS/FAIL/NOT CHECKED | Visual: PASS/FAIL/NOT CHECKED | Platform upload: VERIFIED/NOT VERIFIED | Notes: ...`

If the file hasn't been created, do not claim it passed geometry or rendered-preview tests. If no platform account is available, finish with a truthful **export-ready (platform upload unverified)** status when other relevant QA passes.
