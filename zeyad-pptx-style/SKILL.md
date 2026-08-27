---
name: zeyad-pptx-style
description: >
  Use this skill whenever User asks to create, build, or generate a PowerPoint presentation,
  deck, or slides. This encodes User's personal design language — a clean, professional
  executive style modeled after McKinsey, BCG, and CFI. Trigger on any request like
  "make a presentation", "build a deck", "create slides", or "PPT for X". Always use this
  skill instead of the generic pptx skill when User is the user, as it overrides the
  default design choices with his specific standards. Never use color gradients, AI-aesthetic
  palettes, decorative bars, or extravagant language.
---

# User's Presentation Design System

This skill defines the exact design language used across User's presentations
(AIJRF Rebranding Proposal, Brag Sheet, etc.). It is a McKinsey / CFI-inspired
executive style: dark navy + white, clean sans-serif, minimal decoration, maximum clarity.

**Always read [../pptx/pptxgenjs.md](../pptx/pptxgenjs.md) for PptxGenJS syntax before
generating code.**

---

## Quick Checklist Before Writing Code

- [ ] npm install pptxgenjs
- [ ] Cover slide = dark navy background
- [ ] Section dividers = dark navy background  
- [ ] Content slides = white background
- [ ] Left vertical accent bar on all content slide titles (NOT section dividers)
- [ ] Footer on every content slide (thin horizontal line + breadcrumb dots)
- [ ] Small-caps spaced eyebrow label on every content slide
- [ ] No gradients, no decorative full-width colored bars, no cream/beige backgrounds
- [ ] Font = Calibri (universally available in PowerPoint)

---

## Color Palette

| Token | Hex | Usage |
|-------|-----|-------|
| `NAVY` | `1D3461` | Background on cover/section slides; primary text on light slides |
| `BLUE_ACCENT` | `2563EB` | Left title bar, card left borders, numbered badges, tag pills, icon circles |
| `CARD_BG` | `EEF3FB` | Card/box fill on content slides |
| `WHITE` | `FFFFFF` | Background for all content slides |
| `LIGHT_SEPARATOR` | `CBD5E1` | Thin horizontal footer line on light slides |
| `MUTED_TEXT` | `6B7280` | Subtitle text, body secondary text |
| `FOOTER_TEXT_LIGHT` | `9CA3AF` | Footer text on white slides |
| `FOOTER_TEXT_DARK` | `8BA5CC` | Footer text on navy slides |
| `EYEBROW_TEXT` | `2563EB` | Small caps section label on content slides |

**Never use:** gradients, warm beige/cream (`FAF0E6`, `FFF8E1`, `F5F5DC`), random accent colors, orange, green, or purple unless the content specifically requires it (e.g., a status indicator).

---

## Typography

All fonts use **Calibri** (available in every PowerPoint installation).

| Element | Font | Size | Weight | Color | Notes |
|---------|------|------|--------|-------|-------|
| Cover title | Calibri | 52–60pt | Bold | `FFFFFF` | ALL CAPS or Title Case |
| Cover subtitle | Calibri | 16pt | Regular | `CADCFC` | |
| Cover byline | Calibri | 13pt | Bold | `FFFFFF` | |
| Cover meta | Calibri | 11pt | Regular | `8BA5CC` | |
| Eyebrow label | Calibri | 9pt | Regular | `2563EB` | UPPERCASE, charSpacing: 4 |
| Content title | Calibri | 28–32pt | Bold | `1D3461` | Left-aligned |
| Content subtitle | Calibri | 13pt | Regular | `6B7280` | Left-aligned, below title |
| Section divider title | Calibri | 48–56pt | Bold | `FFFFFF` | |
| Body text | Calibri | 13–14pt | Regular | `374151` | |
| Card header | Calibri | 14pt | Bold | `1D3461` | |
| Card body | Calibri | 12–13pt | Regular | `4B5563` | |
| Stat number | Calibri | 36–48pt | Bold | `2563EB` | Large callout |
| Numbered badge | Calibri | 11pt | Bold | `FFFFFF` | In a navy square |
| Table header text | Calibri | 13pt | Bold | `FFFFFF` | |
| Table body text | Calibri | 12–13pt | Regular | `1D3461` | |
| Tag/pill text | Calibri | 9–10pt | Bold | `FFFFFF` | In colored rect |
| Footer | Calibri | 8–9pt | Regular | `9CA3AF` | Dots between items |

---

## Slide Dimensions

Use `LAYOUT_16x9` — dimensions are **10" × 5.625"**.

Coordinate reference:
- Left margin: `0.5"`
- Right margin: `9.5"` (content ends here)
- Top margin: `0.5"`
- Bottom margin (above footer): `5.0"`
- Footer zone: `5.1" – 5.5"`

---

## Slide Templates

### 1. COVER SLIDE (dark)

Full navy background. Large bold title. Thin horizontal divider. Author block.

```javascript
// Background
slide.addShape(pres.ShapeType.rect, {
  x: 0, y: 0, w: 10, h: 5.625,
  fill: { color: "1D3461" }, line: { color: "1D3461" }
});

// Eyebrow (optional — e.g., "REBRANDING PROPOSAL · MAY 2026")
slide.addText("REBRANDING PROPOSAL  ·  MAY 2026", {
  x: 0.5, y: 0.35, w: 8, h: 0.25,
  fontFace: "Calibri", fontSize: 9, color: "8BA5CC",
  charSpacing: 3, margin: 0
});

// Main title
slide.addText("YOUR BRAND SHOULD\nREFLECT YOUR LEGACY.", {
  x: 0.5, y: 1.0, w: 8.5, h: 2.2,
  fontFace: "Calibri", fontSize: 54, bold: true, color: "FFFFFF",
  align: "left", valign: "top", margin: 0
});

// Subtitle row (dot-separated deliverables)
slide.addText("Website  ·  Visual Identity  ·  Presentation Design", {
  x: 0.5, y: 3.3, w: 8, h: 0.35,
  fontFace: "Calibri", fontSize: 14, color: "CADCFC",
  align: "left", margin: 0
});

// Horizontal divider
slide.addShape(pres.ShapeType.rect, {
  x: 0.5, y: 3.75, w: 8.5, h: 0.025,
  fill: { color: "3D5A8A" }, line: { color: "3D5A8A" }
});

// Author name (in accent blue)
slide.addText("User", {
  x: 0.5, y: 3.9, w: 6, h: 0.35,
  fontFace: "Calibri", fontSize: 15, bold: true, color: "4D9FEC",
  margin: 0
});

// Role + org
slide.addText("User Title", {
  x: 0.5, y: 4.25, w: 8, h: 0.25,
  fontFace: "Calibri", fontSize: 11, color: "8BA5CC", margin: 0
});

// Prepared for
slide.addText("Prepared for: [Client Name]", {
  x: 0.5, y: 4.55, w: 8, h: 0.25,
  fontFace: "Calibri", fontSize: 11, color: "6B8DB5", margin: 0
});
```

---

### 2. SECTION DIVIDER SLIDE (dark)

Same navy background. Section label in spaced caps top-left. Large serif-weight title center-left. Optional 2×2 or 4-item numbered grid below.

```javascript
// Background
slide.addShape(pres.ShapeType.rect, {
  x: 0, y: 0, w: 10, h: 5.625,
  fill: { color: "1D3461" }, line: { color: "1D3461" }
});

// Section label (eyebrow)
slide.addText("SCOPE OF WORK", {
  x: 0.5, y: 0.35, w: 4, h: 0.25,
  fontFace: "Calibri", fontSize: 9, color: "8BA5CC",
  charSpacing: 4, margin: 0
});

// Large title
slide.addText("Four Deliverables.\nOne Cohesive Brand.", {
  x: 0.5, y: 0.85, w: 8.5, h: 2.0,
  fontFace: "Calibri", fontSize: 50, bold: true, color: "FFFFFF",
  align: "left", valign: "top", margin: 0
});

// 2x2 numbered grid — each item:
// Large number (01, 02...) in accent blue, bold header, small description
const items = [
  { num: "01", label: "Website Redesign", desc: "Full rebuild — responsive, SEO-ready, bilingual" },
  { num: "02", label: "Visual Identity", desc: "Logo, color, typography, brand guide PDF" },
  { num: "03", label: "Social Media Templates", desc: "10–15 Canva templates — LinkedIn, Instagram" },
  { num: "04", label: "Presentation Template", desc: "8–10 slide layouts in PowerPoint" },
];
const cols = [0.5, 5.2];
const rows = [3.2, 4.5];
items.forEach((item, i) => {
  const x = cols[i % 2];
  const y = rows[Math.floor(i / 2)];
  slide.addText(item.num, {
    x, y, w: 0.55, h: 0.45,
    fontFace: "Calibri", fontSize: 28, bold: true, color: "2563EB",
    margin: 0
  });
  slide.addText(item.label, {
    x: x + 0.65, y: y + 0.02, w: 3.8, h: 0.3,
    fontFace: "Calibri", fontSize: 14, bold: true, color: "4D9FEC",
    margin: 0
  });
  slide.addText(item.desc, {
    x: x + 0.65, y: y + 0.35, w: 3.8, h: 0.3,
    fontFace: "Calibri", fontSize: 11, color: "8BA5CC", margin: 0
  });
});
```

---

### 3. CONTENT SLIDE — Standard (light, signature style)

White background. **Left vertical accent bar on title.** Eyebrow label. Footer line + breadcrumb.

```javascript
// White background (implicit — no shape needed)

// ── EYEBROW LABEL ──────────────────────────────────────────────────────────
slide.addText("01  |  SECTION NAME", {
  x: 0.5, y: 0.28, w: 8, h: 0.22,
  fontFace: "Calibri", fontSize: 9, color: "2563EB",
  charSpacing: 3, margin: 0
});

// ── LEFT VERTICAL ACCENT BAR (the McKinsey signature element) ──────────────
// Sits flush left, covering the title + subtitle height
slide.addShape(pres.ShapeType.rect, {
  x: 0.5, y: 0.55, w: 0.07, h: 1.05,
  fill: { color: "2563EB" }, line: { color: "2563EB" }
});

// ── TITLE ──────────────────────────────────────────────────────────────────
slide.addText("Slide Title That States the Key Insight", {
  x: 0.68, y: 0.55, w: 8.8, h: 0.65,
  fontFace: "Calibri", fontSize: 28, bold: true, color: "1D3461",
  align: "left", valign: "top", margin: 0
});

// ── SUBTITLE / SUPPORTING SENTENCE ────────────────────────────────────────
slide.addText("One sentence that adds context or states the so-what.", {
  x: 0.68, y: 1.22, w: 8.8, h: 0.28,
  fontFace: "Calibri", fontSize: 12, color: "6B7280",
  align: "left", margin: 0
});

// ── CONTENT AREA ───────────────────────────────────────────────────────────
// [Add cards, bullets, table, chart, etc. — see Layout Patterns below]
// Content y starts at ~1.65", ends at ~4.85"

// ── FOOTER ─────────────────────────────────────────────────────────────────
// Thin line
slide.addShape(pres.ShapeType.rect, {
  x: 0.5, y: 5.1, w: 9.0, h: 0.02,
  fill: { color: "CBD5E1" }, line: { color: "CBD5E1" }
});
// Breadcrumb text left
slide.addText("Organization  ·  Document Title  ·  Author", {
  x: 0.5, y: 5.15, w: 7, h: 0.22,
  fontFace: "Calibri", fontSize: 8, color: "9CA3AF", margin: 0
});
// Slide number right
slide.addText("2", {
  x: 9.0, y: 5.15, w: 0.5, h: 0.22,
  fontFace: "Calibri", fontSize: 8, color: "9CA3AF",
  align: "right", margin: 0
});
```

---

## Layout Patterns for the Content Area

### A. Card Grid (2-column or 3-column)

Cards have a light blue-gray fill and a **left accent border** (3–4pt wide colored rect).

```javascript
function addCard(slide, pres, x, y, w, h, header, body) {
  // Card background
  slide.addShape(pres.ShapeType.rect, {
    x, y, w, h,
    fill: { color: "EEF3FB" },
    line: { color: "D1DCF0", pt: 1 }
  });
  // Left accent border
  slide.addShape(pres.ShapeType.rect, {
    x, y: y, w: 0.06, h,
    fill: { color: "2563EB" }, line: { color: "2563EB" }
  });
  // Header
  slide.addText(header, {
    x: x + 0.18, y: y + 0.16, w: w - 0.25, h: 0.3,
    fontFace: "Calibri", fontSize: 13, bold: true, color: "1D3461", margin: 0
  });
  // Body
  slide.addText(body, {
    x: x + 0.18, y: y + 0.5, w: w - 0.25, h: h - 0.6,
    fontFace: "Calibri", fontSize: 12, color: "4B5563",
    valign: "top", margin: 0
  });
}

// 2-column example (left: x=0.5, right: x=5.15, each w=4.35)
addCard(slide, pres, 0.5,  1.65, 4.35, 1.5, "First-Impression Cost", "Partners form a judgment within seconds of landing.");
addCard(slide, pres, 5.15, 1.65, 4.35, 1.5, "Missed Reach", "Content without identity is ignored — even when substance is strong.");
addCard(slide, pres, 0.5,  3.3,  4.35, 1.5, "Zero Brand Recall", "Without a system, every event starts from zero.");
addCard(slide, pres, 5.15, 3.3,  4.35, 1.5, "Execution Cost", "Ad hoc design multiplies time and budget waste.");

// 3-column example (each w=2.9, gaps at 0.1)
// x positions: 0.5, 3.5, 6.5
```

---

### B. Numbered Badge Card Grid (icon + number + label)

Used for overview/agenda slides on a light background.

```javascript
function addBadgeCard(slide, pres, x, y, w, h, num, icon_char, label, desc) {
  // Card bg + left border
  slide.addShape(pres.ShapeType.rect, { x, y, w, h, fill: { color: "EEF3FB" }, line: { color: "D1DCF0", pt: 1 } });
  slide.addShape(pres.ShapeType.rect, { x, y, w: 0.06, h, fill: { color: "2563EB" }, line: { color: "2563EB" } });
  // Number label (small, above title)
  slide.addText(num, { x: x + 0.18, y: y + 0.1, w: 0.4, h: 0.2, fontFace: "Calibri", fontSize: 9, bold: true, color: "2563EB", margin: 0 });
  // Label (bold)
  slide.addText(label, { x: x + 0.18, y: y + 0.3, w: w - 0.5, h: 0.35, fontFace: "Calibri", fontSize: 14, bold: true, color: "1D3461", margin: 0 });
  // Description
  slide.addText(desc, { x: x + 0.18, y: y + 0.68, w: w - 0.3, h: 0.4, fontFace: "Calibri", fontSize: 11, color: "6B7280", margin: 0 });
}
```

---

### C. Bullet List (left side, paired with visual right side)

```javascript
// Section header above list
slide.addText("What this delivers:", {
  x: 0.68, y: 1.65, w: 4, h: 0.3,
  fontFace: "Calibri", fontSize: 13, bold: true, color: "1D3461", margin: 0
});

// Bullets — use navy filled circle (not default bullet)
const bullets = [
  "Clear navigation — visitors know exactly where to go",
  "Mobile-first design — 65%+ of traffic comes from mobile",
  "SEO-structured pages — visible for keywords you own",
];
slide.addText(
  bullets.map((b, i) => ({
    text: b,
    options: { bullet: { type: "bullet", indent: 15 }, breakLine: i < bullets.length - 1 }
  })),
  {
    x: 0.68, y: 2.05, w: 4.2, h: 2.8,
    fontFace: "Calibri", fontSize: 13, color: "374151",
    lineSpacingMultiple: 1.4, margin: 0
  }
);
```

---

### D. Data Table

Dark navy header row. Alternating light rows. Optional badge pills for tags.

```javascript
// Header row
slide.addShape(pres.ShapeType.rect, { x: 0.5, y: 1.65, w: 9.0, h: 0.45, fill: { color: "1D3461" }, line: { color: "1D3461" } });
slide.addText([
  { text: "Project", options: { w: 2.5 } },
  { text: "Type", options: { w: 1.5 } },
  { text: "What Was Built & Why It Matters", options: {} },
], { x: 0.65, y: 1.65, w: 8.8, h: 0.45, fontFace: "Calibri", fontSize: 12, bold: true, color: "FFFFFF", valign: "middle", margin: 0 });

// Data rows — alternate fill
const rows = [
  { project: "Rankings Intelligence Engine", tag: "ABOVE JD", tagColor: "2563EB", desc: "Python + Power BI system aggregating QS, THE & Shanghai data." },
  { project: "AI-Powered Grant Matcher", tag: "ABOVE JD", tagColor: "2563EB", desc: "LLM semantic search pipeline matching USAID, EU Horizon grants to faculty." },
  { project: "Power BI SQL Dashboard", tag: "CORE JD", tagColor: "4B5563", desc: "Live dashboard connected to SQL Server, published on LinkedIn." },
];
rows.forEach((row, i) => {
  const ry = 2.15 + i * 0.75;
  const fill = i % 2 === 0 ? "F7F9FD" : "FFFFFF";
  slide.addShape(pres.ShapeType.rect, { x: 0.5, y: ry, w: 9.0, h: 0.7, fill: { color: fill }, line: { color: "E2E8F0", pt: 0.5 } });
  // Project name
  slide.addText(row.project, { x: 0.65, y: ry + 0.15, w: 2.3, h: 0.4, fontFace: "Calibri", fontSize: 12, bold: true, color: "1D3461", margin: 0 });
  // Tag pill
  slide.addShape(pres.ShapeType.rect, { x: 3.1, y: ry + 0.18, w: 1.0, h: 0.28, fill: { color: row.tagColor }, line: { color: row.tagColor }, rounding: 0.1 });
  slide.addText(row.tag, { x: 3.1, y: ry + 0.18, w: 1.0, h: 0.28, fontFace: "Calibri", fontSize: 8, bold: true, color: "FFFFFF", align: "center", valign: "middle", margin: 0 });
  // Description
  slide.addText(row.desc, { x: 4.25, y: ry + 0.1, w: 5.1, h: 0.5, fontFace: "Calibri", fontSize: 11, color: "374151", valign: "top", margin: 0 });
});
```

---

### E. Large Stat Callouts

For impact slides — one to three large numbers with labels.

```javascript
// Centered in content area or side-by-side
slide.addText("8", {
  x: 1.0, y: 2.0, w: 2.5, h: 1.5,
  fontFace: "Calibri", fontSize: 72, bold: true, color: "2563EB",
  align: "center", valign: "middle", margin: 0
});
slide.addText("years of leadership", {
  x: 1.0, y: 3.5, w: 2.5, h: 0.4,
  fontFace: "Calibri", fontSize: 13, color: "6B7280",
  align: "center", margin: 0
});
```

---

## What NEVER to Do

- ❌ No color gradients (no `schemeColor`, no multi-stop fills)
- ❌ No decorative full-width colored header/footer bars
- ❌ No warm cream/beige backgrounds (`FAF0E6`, `FFF8E1`, `F5F5DC`)
- ❌ No accent underline lines below titles (AI hallmark)
- ❌ No extravagant language in slide titles ("Unleashing…", "Skyrocketing…")
- ❌ No mixing of random accent colors — stick to navy + blue accent system
- ❌ No centered body text — always left-align except cover title
- ❌ No text-only slides — every content slide needs at least one structured visual element (card, table, stat, chart)
- ❌ No placeholder filler text left in output
- ❌ No left vertical bar on cover or section divider slides (dark bg slides only use the large title)

---

## How to Adapt the Palette Per Context

The navy + blue system is the default. For specific contexts, shift one variable:

| Context | Change |
|---------|--------|
| Corporate / formal | Keep navy `1D3461` + blue `2563EB` as-is |
| University / academic | Add `1B5E3B` (dark green) as secondary, keep navy primary |
| E-commerce / Opaline | Swap navy for `1A1A2A` (near-black) + `C8A96E` (gold) accent |
| Finance / investment | Keep navy, add `16A34A` (green) for positive, `DC2626` (red) for negative |

---

## Full Script Template

```javascript
const pptxgen = require("pptxgenjs");
const pres = new pptxgen();
pres.layout = "LAYOUT_16x9";
pres.title = "Presentation Title";
pres.author = "User";

// -- Helpers --
const NAVY = "1D3461";
const BLUE = "2563EB";
const CARD_BG = "EEF3FB";
const WHITE = "FFFFFF";

function addFooter(slide, org, title, pageNum) {
  slide.addShape(pres.ShapeType.rect, { x: 0.5, y: 5.1, w: 9.0, h: 0.02, fill: { color: "CBD5E1" }, line: { color: "CBD5E1" } });
  slide.addText(`${org}  ·  ${title}`, { x: 0.5, y: 5.15, w: 7.5, h: 0.22, fontFace: "Calibri", fontSize: 8, color: "9CA3AF", margin: 0 });
  slide.addText(String(pageNum), { x: 9.0, y: 5.15, w: 0.5, h: 0.22, fontFace: "Calibri", fontSize: 8, color: "9CA3AF", align: "right", margin: 0 });
}

function addTitleBar(slide, eyebrow, title, subtitle) {
  // Eyebrow
  slide.addText(eyebrow, { x: 0.5, y: 0.28, w: 8.5, h: 0.22, fontFace: "Calibri", fontSize: 9, color: BLUE, charSpacing: 3, margin: 0 });
  // Accent bar
  slide.addShape(pres.ShapeType.rect, { x: 0.5, y: 0.55, w: 0.07, h: subtitle ? 1.05 : 0.7, fill: { color: BLUE }, line: { color: BLUE } });
  // Title
  slide.addText(title, { x: 0.68, y: 0.55, w: 8.8, h: subtitle ? 0.65 : 0.75, fontFace: "Calibri", fontSize: 28, bold: true, color: NAVY, margin: 0 });
  // Subtitle
  if (subtitle) {
    slide.addText(subtitle, { x: 0.68, y: 1.22, w: 8.8, h: 0.28, fontFace: "Calibri", fontSize: 12, color: "6B7280", margin: 0 });
  }
}

// -- Slides --
// 1. Cover
const cover = pres.addSlide();
// ... (use Cover template above)

// 2. Content slide
const s2 = pres.addSlide();
addTitleBar(s2, "01  |  PROBLEM", "The Insight Goes Here As a Full Sentence", "Supporting context in one line.");
addFooter(s2, "Organization", "Document Title", 2);
// ... add content

pres.writeFile({ fileName: "output.pptx" });
```

---

## QA Checklist

After generating, convert to images and verify:

1. **Left accent bar** is present on every content slide title
2. **Footer line + breadcrumb** appears on every non-cover slide
3. **No text overflow** — all text fits inside its box
4. **Cards have left accent border** — not just a plain box
5. **Dark slides** (cover/section) have no footer line (optional: can add muted footer on section slides)
6. **Eyebrow text** is uppercase with `charSpacing: 3` — should look spaced, not cramped
7. **No gradients, no cream backgrounds**
8. Slide numbers increment correctly
