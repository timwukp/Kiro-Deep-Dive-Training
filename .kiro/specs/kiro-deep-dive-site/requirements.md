# Requirements — Kiro Deep Dive training site

Spec type: Feature Spec, Requirements-First. Every acceptance criterion has an ID
(`R<n>.<m>`). Each ID is covered by at least one check in `verify.py` (the check name
carries the ID) or by a manual check listed in `design.md` → *Manual checks*.
`verify.py` enforces that mapping, so a requirement cannot silently lose its test.

## Requirement 1 — Works offline, with no third-party code
User story: As a learner, I want the site to open from a file or GitHub Pages with no
external downloads, so that it works on restricted networks and leaks nothing.
- **R1.1** THE SITE SHALL load every script, stylesheet and image from this repository.
- **R1.2** THE SITE SHALL NOT make network requests from script.
- **R1.3** WHEN JavaScript is disabled, THE SITE SHALL show every slide as readable English text.

## Requirement 2 — English and Traditional Chinese
- **R2.1** THE SITE SHALL provide every slide's text in English and Traditional Chinese.
- **R2.2** WHEN the reader presses L or the language button, THE SITE SHALL switch language and remember the choice.

## Requirement 3 — Spec-driven and test-driven depth
- **R3.1** THE SITE SHALL teach EARS, the three spec files, Analyze Requirements, property-based testing, shrinking, Bugfix Specs, Red-Green-Refactor, traceability, hook-based gates, headless test runs, Workflows and saved recipes, Memory, approval controls (Approve for me, Permission Request Hooks), and remote development (Connect to Host over SSH, Dev Containers, cloud sessions, VPC connections, Kiro for VS Code with Workspace Trust).
- **R3.2** THE SITE SHALL state that Kiro has no feature named "TDD", that property-based testing is IDE only, and that it gives evidence, not proof.

- **R3.3** WHERE a topic has a companion course by the same maintainer, THE SITE SHALL link it: Chapter 8 and the closing slide SHALL link the Kiro Crew Training site (https://timwukp.github.io/Kiro-Crew-Training/) for learners who want Kiro Crew in depth.

## Requirement 4 — Honest and current
- **R4.1** THE SITE SHALL show the date its content was verified against kiro.dev on every chapter.
- **R4.2** WHERE a feature is in Preview at the verification date, THE SITE SHALL label it Preview.
- **R4.3** THE SITE SHALL NOT quote credit multipliers; it SHALL link to the models page instead.
- **R4.4** THE SITE SHALL NOT use overclaiming phrases from the forbidden list in `verify.py`.

## Requirement 5 — Public-safe content
- **R5.1** THE REPOSITORY SHALL NOT contain email addresses (other than example/noreply placeholders), home-directory paths, or credential-shaped values.
- **R5.2** THE SITE SHALL use only fictional examples and SHALL NOT name customers or individuals other than the maintainer's public handle.

## Requirement 6 — Navigation like turning pages
- **R6.1** WHILE in present mode, THE SITE SHALL move one slide per Left/Right arrow (or Space) press and SHALL NOT page on Up/Down.
- **R6.2** THE SITE SHALL provide a chapter menu (button or M key) that jumps to any chapter or slide.
- **R6.3** Every internal link SHALL resolve, and every external link SHALL use https and open safely.

## Requirement 7 — Accessible and responsive
- **R7.1** THE SITE SHALL have one h1, a title, a description, a language attribute and a main landmark.
- **R7.2** THE SITE SHALL provide a skip link, visible keyboard focus, and respect reduced motion.
- **R7.3** THE SITE SHALL scale type and layout to the viewport, from phone to wide monitor.

## Requirement 8 — A repository others can maintain
- **R8.1** THE REPOSITORY SHALL include a README that links the live site, plus SECURITY, UPDATES, VERIFIED_SOURCES and CONTRIBUTING documents and a CI workflow.
- **R8.2** THE REPOSITORY SHALL include Kiro steering and valid v1 hook files that apply this spec's rules while editing.
- **R8.3** WHEN a requirement ID exists in this file, THE VERIFIER SHALL fail unless that ID has an automated or manual check.
- **R8.4** THE REPOSITORY SHALL license its code under MIT (`LICENSE`) and its original teaching content under CC BY 4.0 (`LICENSE-CONTENT.md`), SHALL state that Kiro names and documentation are not covered, and THE SITE SHALL show the licence on its closing slide.
