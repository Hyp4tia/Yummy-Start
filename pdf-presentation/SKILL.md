---
name: pdf-presentation
description: >
  Use this skill whenever user asks for a presentation-style PDF — a deck meant to be presented
  or shared as a finished document, not edited further in PowerPoint. Triggers: "create a PDF for
  them to present", "make a PDF deck", "Arabic presentation PDF", "turn this into a PDF I can show
  the family/client", or any request for a PDF where the content is slide-shaped (cover, sections,
  cards, tables, action items) rather than a form, contract, or scanned document. Covers both Arabic
  (RTL) and English output. Always read ../pptx-style/SKILL.md FIRST for the full color
  palette, typography, and component templates — this skill only covers what's different for PDF
  output, Arabic/RTL handling, and the mandatory pre-delivery QA pass. Do NOT use the generic public
  pdf skill (forms/merge/split) or the generic public pptx skill's default styling for these requests
  — this skill plus pptx-style override both.
---

# user's PDF Presentation Skill (Arabic & English)

## Build approach

1. Read `../pptx-style/SKILL.md` for colors, fonts, and slide/card/table templates. Apply
   that design system exactly, including its card-shadow rule (no colored accent-edge stripes —
   see the deprecation note in that skill).
2. Build the deck with PptxGenJS, same as a normal user deck.
3. Convert to PDF with the pptx skill's LibreOffice helper:
   ```bash
   python3 /mnt/skills/public/pptx/scripts/office/soffice.py --headless --convert-to pdf output.pptx
   ```
4. Run the mandatory QA pass below on the converted PDF.
5. Deliver **only the PDF** to `/mnt/user-data/outputs` unless user also asked for the editable
   `.pptx` — mention it's available on request rather than delivering both by default.

## Language-specific setup

### Arabic (RTL)

- **Font:** use `"Noto Sans Arabic"` as the literal `fontFace`, not `"Arial"`. This sandbox's
  LibreOffice has no Arabic-capable Arial, so declaring Arial renders broken/missing glyphs in the
  PDF. Noto Sans Arabic is the closest modern sans-serif that actually shapes correctly here. (If
  user ever needs a real `.pptx` for Windows PowerPoint specifically, Arial substitutes fine there
  automatically — but for a PDF deliverable built in this environment, declare Noto Sans Arabic
  directly.) If it's missing, install once per environment and rebuild the font cache:
  ```bash
  apt-get install -y fonts-noto-core && fc-cache -f
  fc-list | grep -i "noto.*arabic"   # verify Regular + Bold are present
  ```
- `rtlMode: true` on every Arabic text box, plus explicit `align: "right"`.
- **Never use `charSpacing` on Arabic text.** It breaks cursive letter joining and renders as
  garbled, disconnected glyphs (confirmed bug, June 2026 build). Spaced-caps eyebrow styling is a
  Latin-only typographic trick — for Arabic eyebrows, use color + bold only, no spacing.
- **Never use PptxGenJS's built-in `bullet: true` for RTL lists.** Its indent anchors to the text
  box's left edge regardless of paragraph direction, producing a zigzag column of bullets that
  doesn't line up (confirmed bug, June 2026 build). Instead, place a small filled ellipse
  (`pres.ShapeType.ellipse`, ~0.09" diameter) at a fixed x near the right margin for each line, with
  a right-aligned text box next to it. This guarantees a clean vertical column of bullets.
- **Mirror the whole layout, not just text alignment:**
  - Title accent bar → right edge of the content area, not left.
  - Eyebrow / breadcrumb footer → right-aligned; put the slide number on the **left** edge
    (mirrors the LTR convention of the page number sitting opposite the running header text).
  - Numbered/badge grids and multi-column layouts → the first logical item goes in the
    **rightmost** column/position, reading right-to-left from there.
  - Tables → the first logical column is the **rightmost** column.
  - Cards/boxes → identical fill + neutral border + soft shadow treatment as English (no accent
    stripe, per the pptx-style deprecation — applies to both languages equally).
- Use Western numerals (`0–9`) with standard comma thousand-separators inside Arabic text (e.g.
  `1,400,000 جنيه`) — this is standard practice in Egyptian financial apps and documents, not
  Eastern Arabic-Indic numerals, unless user says otherwise.
- `pptxgenjs`'s oval/ellipse shape constant is `pres.ShapeType.ellipse` — there is no `.oval`.

### English (LTR)

- Standard `pptx-style` templates apply as-is, including `charSpacing` on eyebrow labels.
- If a slide uses **math or physics notation** (Greek letters, subscripts/superscripts, ×, ÷, ≈,
  √, ∑, π, etc.), don't assume a generic sans font carries every glyph. Confirm in the rendered QA
  image that each symbol shows as the intended character — not a "tofu" box, not a silently
  substituted ASCII approximation. If a symbol doesn't render correctly, either switch to a font
  confirmed to carry it, or build that expression as a small inline image instead of risking a
  missing-glyph defect in the delivered PDF.

## Mandatory QA — before presenting, every single time

Not optional, not skippable for a "quick" deck. After converting to PDF:

```bash
rm -f slide-*.jpg
pdftoppm -jpeg -r 150 output.pdf slide
```

Do a contact-sheet pass first for triage (cheap, catches gross issues fast across all pages at
once), then zoom into the full-resolution image for anything ambiguous or text-dense. Check
explicitly for:

1. **Text visible or not** — nothing white-on-white, nothing below readable contrast against its
   background, nothing hidden behind a shape, nothing clipped off the slide edge.
2. **Morphing / distorted glyphs** — letters rendering as broken, disconnected, or malformed. This
   is the #1 Arabic-specific risk (charSpacing breaking cursive joining — see above). For English,
   watch for symbol substitution in math/physics content.
3. **Floating elements** — anything visually disconnected from what it should be anchored to: a
   label drifted from its data point, a shape off the grid the rest of the slide follows, an accent
   bar not flush against its title.
4. **Spacing — too close or too far** — overlapping elements, text touching a border, two cards
   nearly touching, or unintentionally large empty gaps. Specifically check that tables and lists
   end with margin before the footer line rather than colliding with it — this is the most common
   real defect in dense data slides.
5. **Arabic symbols visible and easy to read** — correct letter shaping/joining, correct RTL
   reading order (read the rendered line right-to-left the way the audience will, not
   left-to-right out of habit), diacritics not clipped or floating oddly.
6. **English math/physics symbols** (when used) — every special character renders as intended.
7. **Overflow** — every text box's rendered content fits inside its shape; every table/list fits
   above the footer line at the font sizes actually used (don't trust a pre-render estimate).
8. **Placeholder/leftover content:**
   ```bash
   extract-text output.pptx | grep -iE "\bx{3,}\b|lorem|ipsum|TODO|\[insert"
   ```
9. **Numbering consistency** — eyebrow section numbers and footer page numbers both increment
   correctly and agree with each other after any slide insertion/deletion.

Fix what's found, re-render, re-check only the affected pages, then stop — don't keep iterating
past real, user-visible defects into sub-pixel nudging.

## Known fixes from past builds (check here before re-debugging from scratch)

- Oval/circle shapes: use `pres.ShapeType.ellipse`, not `.oval` (throws otherwise).
- Shadow opacity must use the `opacity` property — never bake it into an 8-char hex color string.
- A single deck inserted/removed a slide mid-build once and the eyebrow numbers + footer page
  numbers got out of sync — always grep both after a structural change, not just visually skim.
