# Design — Kiro Deep Dive training site

## Shape
One static page (`index.html`) with 8 chapters plus intro and closing slides, one
stylesheet and one script, no libraries. GitHub Pages serves the repository root.

| Concern | Decision | Requirement |
|---|---|---|
| Dependencies | None. No CDN, no fonts, no analytics. Diagrams are HTML/CSS and inline SVG. | R1.1, R1.2 |
| No-JS reading | Slides are plain `<section class="slide">` blocks; only `html.present` hides inactive ones, and only the script adds that class. | R1.3 |
| Bilingual | Every string is a pair: `<span class="en">` + `<span class="zh" lang="zh-Hant">`. CSS shows one by `html[data-lang]`. Without JS, English shows. | R2.1, R2.2 |
| Modes | *Present*: one slide at a time, Left/Right/Space, swipe. *Reading*: all slides scroll. Default is Present on wide screens, Reading on phones. | R6.1 |
| Deep dives | `<details class="deep">` inside cards: click a card or its summary to expand official detail, code and source link. Works without JS. | R3.1 |
| Sizing | Root font `clamp()` on viewport width and height; grids use `auto-fit` + `minmax`. | R7.3 |
| Currency | Every chapter divider carries `data-verified`; volatile numbers are linked, not quoted. | R4.1, R4.3 |

## Build approach (test-first)
1. Write `requirements.md` (this spec) and `verify.py` before any page content.
2. Run `verify.py` against the empty repository — it must fail (Red). Record the count.
3. Add the page, styles and script until `verify.py` passes (Green).
4. Write `tests/test_verify.py` mutation tests that break one rule each and prove the verifier notices.
5. Refactor content with both suites green.

## Enforcement strengths
| Strength | Mechanism here | Can it be bypassed? |
|---|---|---|
| Advisory | `.kiro/steering/*.md` guide the agent while editing | Yes — it guides, it doesn't block |
| Feedback | `.kiro/hooks/*.json` run `verify.py` after saves and spec tasks | Yes — output informs, it doesn't block |
| Blocking | GitHub Actions `verify` job, made a *required* check by branch protection | Only by a repository admin changing protection |

## Manual checks
These cannot be judged by `verify.py`; do them before each release and record the
result in the pull request:
- R2.2 — press L and the language button; reload; the choice is kept.
- R6.1 — in present mode, Left/Right/Space move exactly one slide; Up/Down do not page.
- R6.2 — the M key and the menu button open the chapter menu; every entry jumps correctly.
- R7.2 — tab through every control with the keyboard; focus is always visible.
- R7.3 — check at 390 px (phone), 1440 px (laptop) and 2560 px (wide) widths.
- R5.2 — read every example once for real names; examples must be fictional.
- R1.3 — open with JavaScript disabled; all slides readable in English.
