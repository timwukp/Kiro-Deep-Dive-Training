# Updates

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
- Corrections versus earlier internal drafts: hooks block on **any** non-zero exit (not only
  exit 2); headless runs use `kiro-cli chat --no-interactive` (not `--print`); credit
  multipliers are no longer quoted.
- Built test-first: `verify.py` was written before the pages (first run on the empty
  repository: 128 checks, 73 failed), then the site was built until it passed.
- Offline and dependency-free: no CDN, no fonts, no analytics.
