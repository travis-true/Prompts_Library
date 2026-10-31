# Animate a PowerPoint slide with Copilot

**Audience:** Workplace

## Purpose

Turn a slide image into a restrained animation brief for Copilot, requesting an MP4 when supported and a precise PowerPoint animation plan otherwise.

## When to use it

When a process, chart, or diagram would benefit from a timed visual reveal in a presentation. The reference video demonstrates uploading a slide image, requesting an animated MP4, and inserting the result into PowerPoint. Its Copilot demonstration is labeled illustrative; it does not establish availability in every account. An MP4 is embedded video, not editable PowerPoint object animations.

## Copy-ready prompt

```txt
Animate the attached PowerPoint slide as a short, professional video that helps viewers understand its main message.

Goal
Guide the audience’s attention through this idea: [MAIN MESSAGE].
Audience: [AUDIENCE].
Desired animation order: [FIRST → SECOND → THIRD].

Source
Use the attached slide image as the visual source of truth. Preserve its exact wording, numbers, chart values, colors, fonts, logo, proportions, and final layout. Do not invent or rewrite content.

Animation direction
- Keep the camera fixed and the background stationary.
- Animate individual visual elements in the specified order.
- Use subtle fades, directional reveals, and restrained emphasis.
- For process diagrams, reveal each step and then its connecting arrow.
- For charts, reveal the existing data without changing values, scales, or relationships.
- Keep text sharp and stable. Avoid distorted letters, moving labels, or altered logos.
- Avoid decorative motion, flashing, bouncing, spinning, and unnecessary zooms.
- End with the complete original slide visible and hold it still for the final two seconds.

Output
Create an approximately [8]-second, silent MP4 suitable for inserting into PowerPoint. Match the source slide’s aspect ratio; target 1920 × 1080 for a 16:9 slide if supported. Include no narration, music, or additional captions.

Before generating, check whether this session supports animating the uploaded image and exporting an MP4. If supported, create the actual downloadable video. If unsupported, state that clearly and provide a precise PowerPoint animation plan instead, listing each object, effect, order, start setting, duration, and delay. Clearly distinguish a generated file from instructions.
```

## Customize before running

- **Source image:** Attach a high-resolution export of the slide that you are authorized to share. Retain the original editable slide.
- **Message and audience:** Identify the one idea the animation should clarify and who will view it.
- **Sequence:** Name the exact elements in order, such as request → review → resolution.
- **Duration:** Replace `[8]` with a supported duration that leaves time to read the slide.
- **Delivery:** Use the MP4 route for timed playback. Use the fallback plan when you need editable objects or presenter-controlled clicks; implementing that plan requires the original slide objects.

## Example output

*Fictional planning example; no generated video or verified Copilot result is implied.*

Input: An eight-second slide animation for employees showing Request → Review → Resolution.

Fallback if MP4 generation is unavailable:

| Order | Object | Effect | Start | Duration | Delay |
| --- | --- | --- | --- | --- | --- |
| 1 | Request box | Fade | With Previous | 0.5 s | 0 s |
| 2 | First connector | Wipe from left | After Previous | 0.5 s | 0.5 s |
| 3 | Review box | Fade | After Previous | 0.5 s | 0.5 s |
| 4 | Second connector | Wipe from left | After Previous | 0.5 s | 0.5 s |
| 5 | Resolution box | Fade | After Previous | 0.5 s | 0.5 s |

Keep the title visible throughout. The sequence completes at 4.5 seconds; hold the complete slide through eight seconds. Verify effect availability and timings in PowerPoint before use.

## Check before using

- Wording, numbers, labels, logos, and chart relationships match the source in every frame.
- The reveal order supports the stated message, with readable text and restrained motion.
- The final frame matches the original slide and remains still for at least two seconds.
- The actual output has the requested duration, aspect ratio, resolution where supported, and no unwanted audio.
- A claimed MP4 is downloadable and plays correctly after insertion into PowerPoint.
- A fallback plan is clearly identified as instructions and has not been described as an applied animation.
- Retain an accessible static slide so meaning does not depend on motion alone.

## About this entry

Version 1.0.0. Based on the user-supplied video by @robert.triebwasser. The video shows the brief prompt “Animate this slide. Keep the colours and export as an MP4.” This expanded prompt was drafted in the conversation and adds sequence, fidelity, output, and capability checks. Not runtime-tested in Copilot.

Microsoft documents [AI-generated short clips](https://support.microsoft.com/en-gb/microsoft-365-copilot/create-ai-generated-short-clips-in-the-microsoft-365-copilot-app) as an early-access capability for eligible accounts. That documentation does not establish exact slide-image animation support for every session. Check current capabilities before promising output.
