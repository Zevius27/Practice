---
name: Handwritten-Notes
description: Rules for generating handwritten-style study notes
---
# Handwritten Notes Generation

When generating handwritten-style notes for study material, follow these conventions to ensure clarity, exam excellence, and authentic human presentation.

## Rendering & Styling

1. **Embedded Handwriting Fonts**
   - Use *Kalam* for headings and *Patrick Hand* for body text (Google Fonts, OFL-licensed).
   - Convert font files to base64 and embed via `@font-face { src: url(data:font/truetype;base64,...) }`.
   - This ensures offline functionality and consistent rendering without external dependencies.

2. **Logic Symbols Fallback**
   - Handwriting fonts lack math symbols (¬ ∧ ∨ ∀ ∃, etc.).
   - Let browser font fallback handle symbols: list handwriting fonts first, then generic symbol fonts.
   - This creates natural-looking notes: flowing cursive words with carefully drawn symbols.

3. **Ruled-Paper Background**
   - Create horizontal ruled lines using `repeating-linear-gradient`.
   - Add vertical red margin line using `linear-gradient`.
   - Both should be CSS background layers on the same container.

4. **Section Headings**
   - Use asymmetric `border-radius` (e.g., `255px 15px 225px 15px`) for imperfect, hand-drawn boxes.
   - Apply slight `rotate()` transform to enhance realism.

5. **Callout Boxes**
   - Design "Exam tip" and "Common trap" callouts with dashed borders, slight rotation, and drop shadow.
   - Purpose: appear as hand-placed sticky notes rather than system alerts.

6. **Structure**
   - Wrap each topic/page in `<div class="sheet">` with individual shadows.
   - Background should be dark (desk-like).
   - Include `@media print` rules for clean PDF export (one page per unit).

7. **Portability**
   - All assets must be self-contained (no external images or assets).
   - Output should be a single, portable HTML/CSS file.

## Content Generation Guidelines

- **Concise yet comprehensive**: Material should be understandable on first read and sufficient for exam excellence.
- **Human touch**: Present information as if crafted by an expert educator — warm, precise, and insightful.
- **Exam-focused**: Highlight key concepts, common pitfalls, and high-yield facts.
- **Clarity first**: Prioritize understanding over verbosity; use examples, analogies, and visual spacing.

## File Output

When outputting files:
1. Name the file appropriately based on the subject/topic.

2. Save to :-
`C:\Users\Zevius\Desktop\Projects\Practice\Discrete-Mathematics` folder (create if needed).

3. Ensure the filename reflects the subject matter clearly.





















/Handwritten 

Make human type notes on these topics keep details consise I shall be able to see the material and understand it good enough on the first try and be able to top exams with excellence.  Make the notes at that level, it shall have human touch of respected human who is godly making notes .



What to do ?
= 
**1. Real handwriting fonts, actually embedded**
I pulled two open-source (Google Fonts, OFL-licensed) handwriting fonts — *Kalam* for headings and *Patrick Hand* for body text — from Google's font repo on GitHub. Instead of linking to a font CDN (which might not load inside the file later, e.g. offline or on a locked-down network), I converted both font files to base64 and embedded them directly in the CSS with `@font-face { src: url(data:font/truetype;base64,...) }`. That's why the file is ~900KB and why it renders identically anywhere, no internet needed.

**2. The logic symbols (¬ ∧ ∨ ∀ ∃ etc.) aren't in those fonts**
Handwriting fonts only cover normal letters — no math symbols. Rather than fight that, I just let the browser's normal font-fallback behavior handle it: the font stack lists the handwriting font first, then generic symbol fonts after. So letters render in "handwriting," and the logic symbols automatically fall back to a clean default look — which actually mimics how people really write notes (flowing cursive words, then careful little hand-drawn symbols).

**3. The ruled-paper background is two overlapping CSS gradients**
One `repeating-linear-gradient` makes the horizontal ruled lines, and a second `linear-gradient` draws the vertical red margin line — both painted as background layers on the same div, no images involved.

**4. The "boxed" section headings**
That hand-drawn-looking rectangle around each unit title is a CSS trick: an asymmetric `border-radius` (like `255px 15px 225px 15px`) makes a rectangle look slightly wobbly/imperfect, then a tiny `rotate()` sells the illusion further.

**5. Sticky-note callouts**
The "Exam tip" / "Common trap" boxes are just divs with a dashed border, a slight rotation, and a drop shadow — enough to read as a hand-placed note rather than a system alert box.

**6. Structure**
Each "page" is its own `<div class="sheet">` with its own shadow, sitting on a dark background — like paper on a desk — and there's a `@media print` rule so it also prints/exports to PDF cleanly, one page per unit.

Nothing here needed images or external assets at runtime — it's all self-contained HTML/CSS, which is also why it's portable as a single file.







For Finishing:
= 
1. Make File with appropriate name or Ask for appropriate name .
2. And make file and save it By making a subject folder on Desktop.
    - Subjet Folder Shall be named by Subject Name.
    - Be care ful 
    
