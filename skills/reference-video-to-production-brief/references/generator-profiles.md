# Generator capability profiles

Keep the production brief independent of a single model. Complete a profile for the exact host and selected version at use time; do not assume every wrapper exposes the same capabilities.

| Field | Record |
| --- | --- |
| Host and model/version | [exact selection or unknown] |
| Official source and check date | [URL and date, or unverified] |
| Supported inputs | [text/image/video/audio and reference roles] |
| Upload constraints | [type, size, count, duration] |
| Output controls | [duration, aspect ratio, resolution, audio] |
| Reference syntax | [documented attachment mechanism] |
| Optional controls | [seed, keyframes, weights, negative prompts, editing] |
| Access and cost | [account-specific evidence; unknown otherwise] |
| Unavailable requirements | [limitation and fallback] |

Use current official documentation when a final prompt depends on these features. Recheck access/cost for the user's actual host; general model announcements do not prove a free tier or account entitlement. Never silently switch hosts or models.

Starting points, not verified account profiles:
- Gemini Apps: analysis workflow and upload guidance at https://support.google.com/gemini/answer/14903178 . Keep consumer-app behavior distinct from API behavior.
- Gemini API: video understanding documentation at https://ai.google.dev/gemini-api/docs/video-understanding . Sampling and input behavior are model/version-specific; do not apply API defaults to the app without evidence.
- Seedance: official model information at https://seed.bytedance.com/en/models . Follow the selected version and actual host documentation for supported controls.
- Other generators: find the model provider and host's official documentation; do not extrapolate from another model's syntax.

No fixed price, duration, free quota, or upload limit is guaranteed by this package. If current verification is unavailable, produce a portable shot prompt and list the controls requiring confirmation.
