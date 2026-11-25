# Updates

## 2026-11-25 — v1.3.0, governance in customer-journey order, plus monitoring
- Chapters now follow how a regulated customer decides: 1 SDD and TDD (why adopt) → **2 Governance:
  decide before you deploy** (can we allow it) → 3–6 how developers use Kiro → **7 Rolling out with
  MDM** → **8 Monitor and audit** → 9 Scrum and DevSecOps → 10 What's new → 11 Kiro Crew.
- The single governance chapter of v1.2.0 is split: Chapter 2 (8 slides, for CISOs, risk and
  compliance, with a new sign-off checklist and a map of the terms taught later) and Chapter 7
  (12 slides, for endpoint and platform teams).
- New Chapter 8, Monitor and audit (8 slides): Kiro's records and what each contains; who asks what;
  two reference architectures (batch in your account, and OpenTelemetry streaming over PrivateLink);
  detection rules led by data freshness; protecting the monitoring system and the privacy review;
  closing the loop back to the pilot ring; six metrics that mislead. Links the reference dashboard
  [kiro-telemetry-dashboard](https://github.com/timwukp/kiro-telemetry-dashboard) (community sample).
- Agenda: role-based tracks (leaders and security; endpoint and platform; developers).
- Chapters are now found by topic (`data-topic`) in `verify.py`, so a reorder cannot silently break
  a check; a link that names a chapter must point to it.
- New requirements R10 (monitoring) and R11 (order, tracks, chapter references). Red: 1365 checks,
  64 failed; Green: 1677 checks, 0 failed. 5 new mutation tests (22 in total).

## 2026-11-25 — v1.2.0, Chapter 9: enterprise governance with MDM
- New Chapter 9 (19 slides, about 20 minutes) for endpoint, security and platform teams: four governance
  questions; six control layers and which two are real boundaries; what MDM can and cannot
  guarantee; workspace trust and Kiro's hardcoded invariants; organisation settings in the Kiro
  console (model approved list, MCP, web tools, API keys, Enterprise Management Preview); lock,
  detect and repair on Linux, macOS and Windows; a MAS TRM control mapping (the author's
  interpretation); `managed-settings.json`
  (permission and `signin_method` rules, paths, fail-closed vs fail-open); rule design and
  permission modes; the MDM rollout (policy app → Kiro app → drift repair → pilot ring → fleet,
  Intune and Jamf); a worked Intune Win32 app; four scripting traps (encoding, locked file,
  silent exit 0, Constrained Language Mode); global hooks and steering; update rings and pinning;
  server-side records; governance as a spec; a red-team table of seven assumptions that fail;
  and a link to the companion reference repo
  [kiro-fsi-best-practices](https://github.com/timwukp/kiro-fsi-best-practices).
- Reviewed against that repo before release. Taken from it, and re-checked on kiro.dev: the
  device policy does not reach Kiro Web; workspace trust; hardcoded invariants; guards that exit 2
  on their own failures; Kiro documents team steering pushed by MDM; per-MDM drift conventions.
  Corrected here where it is newer than the repo: Enterprise Management is in Preview in US East
  (N. Virginia) **and** Europe (Frankfurt); its "Enforced" capabilities are decided by the service.
  Fixed in this chapter: blocking the public download host (Kiro's pages differ — it also serves
  the Powers registry).
- Kiro claims come from kiro.dev, Intune and Windows claims from Microsoft Learn. Results from
  the maintainer's own lab sit only on slides badged **Lab observation** (Kiro IDE 1.5.11, no
  Intune tenant, one run per result). The example bank, Harbor Lending, is fictional.
- **Correction:** v1.0.0 said hooks block on any non-zero exit. Kiro's pages differ — Hook
  actions says so, the v1 hooks page says only exit 2 blocks. Chapters 1 and 2 now teach exit 2,
  which blocks under both readings.
- New requirement R9 (R9.1–R9.8). Red first: 996 checks, 24 failed (R9.1–R9.5), then 1205
  checks, 13 failed (R9.6–R9.8); Green: 1320 checks, 0 failed. 7 new mutation tests (17 in total).
  SECURITY.md adds a coordinated-disclosure rule for findings about Kiro itself.

## 2026-11-25 — v1.1.2, link to the Kiro Crew Training course
- Chapter 8 now points learners who want Kiro Crew in depth to the companion course
  https://timwukp.github.io/Kiro-Crew-Training/ by the same author: a note on the chapter
  divider and a new slide, *Go deeper: the Kiro Crew Training course*, with what it covers,
  key facts and its verification date (2026-08-31).
- Also linked from the closing slide, the sources table and the README.
- New requirement R3.3: its 2 checks failed first, then passed (964 checks, 0 failed).

## 2026-11-25 — v1.1.1, licences
- Code and configuration under the MIT licence (`LICENSE`); original teaching content under
  CC BY 4.0 (`LICENSE-CONTENT.md`), with a scope table and how to credit.
- Kiro, AWS and Amazon names and logos, and Kiro's own documentation, are stated as not covered.
- Licence shown on the About and closing slides; contributions use the same terms
  (`CONTRIBUTING.md`). New requirement R8.4: its 5 checks failed first, then passed (937 checks).

## 2026-11-25 — v1.1.0, features from the Kiro IDE "What's new" panel
- New slide **Approve for me** (Chapter 3): rules first, then an LLM review that approves routine
  actions, blocks unsafe ones and asks when unsure; how to turn it on; how it compares with
  permission rules and trust-all-tools; why it doesn't replace human review of red tests.
- **Memory** (Chapter 2): now in Kiro IDE and Kiro for VS Code, settings in the Memories view,
  read-only Kiro Memory Preview in Crew.
- **Multi-agent workflows** (Chapter 4): save and rerun recipes, a model per step, the runtime
  keeps the plan, opt-in per client (VS Code: Settings → Extensions → Kiro), credit trade-off.
- **Remote environments** (Chapter 5): SSH, Dev Containers and IDE cloud sessions retitled to match
  the IDE; VPC connections for Enterprise cloud sessions.
- **Kiro for VS Code** (Chapter 5): same .kiro folder, Supervised / Approve for me / Autopilot,
  Workspace Trust, steering transparency, ACP for other editors.
- **Hooks**: Permission Request Hooks and PreToolUse input rewriting (IDE 1.4.236), also added to
  the test-gates table in Chapter 1; a new anti-pattern row on approving on autopilot.
- New What's new slide (Chapter 7) for these items. Built test-first again: 8 new topic checks
  were added first (5 failed), then content was added until 927 checks passed.

## 2026-11-25 — v1.0.0, first public version
- Eight chapters plus intro and closing, 69 slides, English and Traditional Chinese.
- Chapter 1 deepened into spec-driven **and** test-driven development: EARS, traceability
  from criterion to test name, Analyze Requirements, test-first tasks and steering,
  property-based testing (IDE only), strong vs weak properties, shrinking and triage,
  Bugfix Specs, hooks as test gates, AI-specific anti-patterns, and a hands-on lab with a
  fictional library app.
- Test-first threads in later chapters: test-writer vs implementer agents, headless test runs
  in CI with `--no-interactive` and `--sandbox`, a test-first Workflow, SubagentStop hooks,
  dev containers for reproducible test environments.
- Content verified against kiro.dev on 2026-11-25, including releases up to Nov 24, 2026
  (Kiro for VS Code, Remote SSH and Dev Containers, CLI 3.6, Kiro Enterprise for iPhone,
  Claude Fable 5.2 Preview, Crew 0.13 conductor mode).
- Corrections versus earlier internal drafts (the first one revised in v1.2.0): hooks block on **any** non-zero exit (not only
  exit 2); headless runs use `kiro-cli chat --no-interactive` (not `--print`); credit
  multipliers are no longer quoted.
- Built test-first: `verify.py` was written before the pages (first run on the empty
  repository: 128 checks, 73 failed), then the site was built until it passed.
- Offline and dependency-free: no CDN, no fonts, no analytics.
