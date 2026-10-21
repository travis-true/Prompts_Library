# Format-specific QA checks

## Contents

1. DOCX and word-processing documents
2. PPTX and slide decks
3. XLSX and spreadsheets
4. PDF
5. Raster images and screenshots
6. SVG and vector graphics
7. HTML and web content
8. JSON, XML, CSV, and structured data
9. Audio and video
10. Archives and mixed packages

## 1. DOCX and word-processing documents

- Open in the required editor.
- Render every page and inspect at full size.
- Verify styles, headings, lists, tables, page breaks, sections, headers, footers, numbering, fields, links, references, comments, and tracked-change state.
- Check widows, orphans, clipping, overlap, missing glyphs, blank pages, table splitting, and image quality.
- Verify document properties, language, title, alt text, reading order, table headers, and navigation.
- Compare exported PDF with the editable source.

## 2. PPTX and slide decks

- Open in the required presentation application.
- Render every slide and inspect individually plus as a contact sheet.
- Verify masters, layouts, theme, fonts, notes, slide order, hidden slides, transitions, animations, media, charts, links, footers, and page numbers.
- Check clipping, overlap, wrapping, off-canvas content, broken connectors, unresolved placeholders, crop quality, and contrast.
- Verify slide titles, reading order, alt text, table structure, media alternatives, and audience-facing copy.
- Confirm exported PDF or imported platform version preserves content and meaning.

## 3. XLSX and spreadsheets

- Open and recalculate using a compatible engine.
- Check formulas, references, named ranges, tables, filters, validation, protections, hidden rows/columns/sheets, charts, pivots, external links, macros, dates, units, and number formats.
- Test representative inputs, boundary values, errors, blanks, and invalid data.
- Verify totals, denominators, rounding, currency, percentages, and cached results.
- Inspect every sheet for usability, clipping, print area, frozen panes, instructions, and accessibility.
- Distinguish values, formulas, and manually entered overrides.

## 4. PDF

- Open with multiple required readers where risk justifies it.
- Render every page and inspect at full size.
- Verify page count, size, orientation, crop, fonts, images, links, bookmarks, forms, attachments, signatures, and printing.
- Check text extraction, searchability, reading order, tags, headings, lists, tables, alt text, language, and form labels.
- Compare semantically with the authoritative editable source.
- Do not infer PDF accessibility from the source document.

## 5. Raster images and screenshots

- Inspect the exact final pixels at native resolution and intended display size.
- Verify dimensions, aspect ratio, crop, sharpness, color, transparency, compression, artifacts, and safe areas.
- Check platform fidelity, interface state, text accuracy, fictional or permitted data, annotation accuracy, and callout legibility.
- Verify no sensitive data, hidden metadata, or unintended background details remain.
- Record alt text and intended use.

## 6. SVG and vector graphics

- Parse and render in required viewers.
- Verify viewBox, dimensions, transparency, fonts or text conversion, paths, clipping, masks, filters, links, scripts, and embedded assets.
- Test resizing and background contrast.
- Inspect source for hidden, external, unsafe, or inaccessible content.
- Provide a text alternative when the SVG conveys information.

## 7. HTML and web content

- Validate markup, styles, scripts, links, forms, media, responsive breakpoints, printing, and browser compatibility.
- Test keyboard navigation, focus, landmarks, headings, labels, error messages, zoom, reflow, contrast, reduced motion, and screen-reader semantics.
- Verify no secrets, local paths, development code, console errors, broken assets, or prohibited trackers remain.
- Test the actual deployed or packaged state when release depends on it.

## 8. JSON, XML, CSV, and structured data

- Parse with the required standard or schema.
- Verify encoding, delimiter, escaping, types, required fields, unique IDs, ordering where material, null handling, ranges, relationships, and referential integrity.
- Compare counts, totals, and representative records with the source.
- Check for sensitive fields, formula injection, unsafe content, and undocumented schema changes.

## 9. Audio and video

- Play the complete final file.
- Verify duration, resolution, frame rate, aspect ratio, audio levels, synchronization, transitions, screen states, text, branding, and export artifacts.
- Check captions for timing and accuracy, transcript completeness, audio description or equivalent, and readable on-screen text.
- Confirm permitted people, data, music, images, footage, licenses, and releases.
- Inspect thumbnails, posters, chapters, metadata, and alternate formats.

## 10. Archives and mixed packages

- Extract into a clean location.
- Verify manifest, checksums where used, folder structure, relative links, dependencies, and startup instructions.
- Open every required item and scan for unexpected or prohibited content.
- Check duplicate versions, stale drafts, temporary files, hidden files, broken references, and nested archives.
- Repackage only the approved contents and retest extraction.
