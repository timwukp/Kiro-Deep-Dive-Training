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

- **R3.3** WHERE a topic has a companion course by the same maintainer, THE SITE SHALL link it: the Kiro Crew chapter and the closing slide SHALL link the Kiro Crew Training site (https://timwukp.github.io/Kiro-Crew-Training/) for learners who want Kiro Crew in depth.

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

## Requirement 9 — Enterprise governance: decide, roll out with MDM, monitor
User story: As an endpoint or security engineer in a regulated organisation, I want to know how
to roll out and govern Kiro with my device-management tool, and where the real security
boundary is, so that I can pilot it without trusting the wrong control.
- **R9.1** THE SITE SHALL include governance chapters (decide before you deploy; roll out with MDM; monitor and audit) that together teach control layers, `managed-settings.json` permission policies and `signin_method` rules, managed updates (`UpdateMode`), delivery of the system-wide build with an Intune Win32 app and detection rule, global hooks and steering, drift repair with Intune Remediations, Constrained Language Mode, pilot rings, application control, server-side records (prompt logging, user activity, CloudTrail), a non-Windows MDM example (Jamf), workspace trust, organisation settings in the Kiro console (model approved list, Enterprise Management), the reach of the device policy (not Kiro Web), cross-platform file locks (`chattr`, `chflags`) and a regulator mapping (MAS TRM); THE AGENDA SHALL link it.
- **R9.2** THE SITE SHALL state that policies, hooks and steering on the device are a guardrail, not a security boundary, that Kiro documents its policies as client-enforced, and SHALL NOT claim that MDM enforces Kiro's rules.
- **R9.3** WHERE a statement rests on the maintainer's own lab rather than on vendor documentation, THE SITE SHALL badge the slide "Lab observation" and name the Kiro version tested and that no Intune tenant was used.
- **R9.4** THE SITE SHALL NOT publish reproduction steps for an unfixed way around a Kiro permission control; THE REPOSITORY SHALL state in SECURITY.md that such findings go to the vendor first (coordinated disclosure).
- **R9.5** WHEN two Kiro documentation pages disagree on behaviour the course teaches, THE SITE SHALL say that the pages differ and teach the form that is safe under both (hooks: exit 2 blocks).
- **R9.6** THE SITE SHALL say what MDM can and cannot guarantee: it resists a standard user, does not stop an administrator, detects drift rather than preventing it, gives no secrecy, and reaches only managed devices that run the Kiro client; THE SITE SHALL NOT call these controls tamper-proof.
- **R9.7** WHERE the chapter maps controls to a regulation, THE SITE SHALL say the mapping is the author's interpretation, not the regulator's, and SHALL link the regulator's own page.
- **R9.8** The governance chapters and the closing slide SHALL link the maintainer's companion reference repository (https://github.com/timwukp/kiro-fsi-best-practices) for reference scripts and a fuller treatment.

## Requirement 10 — Monitoring and audit
User story: As a security operations, FinOps or engineering lead, I want to know which Kiro records exist and how to turn them into alerts and reviews, so that governance has a feedback loop and I do not trust a misleading number.
- **R10.1** THE SITE SHALL include a monitoring chapter that teaches Kiro's records (prompt logging, the CSV report, OpenTelemetry metrics, OpenTelemetry real-time events, CloudTrail) with what each contains, a reference architecture with private connectivity (PrivateLink), the IAM Identity Center user ID as the join key, and detection rules including data freshness.
- **R10.2** THE SITE SHALL state that monitoring detects; it does not prevent, and that Kiro does not notify you when an export delivery succeeds or fails.
- **R10.3** WHERE the chapter shows an adoption, productivity or ROI metric, THE SITE SHALL call it a proxy, not proof, and SHALL NOT claim that a metric proves ROI or productivity.
- **R10.4** THE SITE SHALL treat the records as sensitive: least privilege, named queries only, a retention period, and a privacy review of employee monitoring.
- **R10.5** The monitoring chapter and the closing slide SHALL link the maintainer's reference dashboard (https://github.com/timwukp/kiro-telemetry-dashboard) and call it a community sample.

## Requirement 11 — Chapters in customer-journey order
User story: As a decision maker at a regulated customer, I want governance before the feature tour, so that I can decide whether Kiro may be used before I invest an hour in how it works.
- **R11.1** THE SITE SHALL order its chapters: spec- and test-driven development; governance, decide before you deploy; steering and hooks; CLI and agents; skills and MCP; web and remote; rolling out with MDM; monitoring and audit; Scrum and DevSecOps; what's new; Kiro Crew — and SHALL number the dividers ch1 to ch11 in that order.
- **R11.2** THE AGENDA SHALL offer role-based tracks (leaders and security; endpoint and platform teams; developers) that link their chapters.
- **R11.3** WHEN a slide or the README names a chapter by number, that chapter SHALL exist, and a link that names a chapter SHALL point to that chapter.
