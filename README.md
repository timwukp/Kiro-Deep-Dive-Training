# Kiro Deep Dive — spec-driven and test-driven development

**Live site: https://timwukp.github.io/Kiro-Deep-Dive-Training/**

A free, bilingual (English / 繁體中文) training site for developers on spec-driven and
test-driven development with [Kiro](https://kiro.dev). Eleven chapters, about two and a half hours, in the order a
regulated customer decides: why adopt, can we allow it, how developers use it, how we roll it out
and watch it.
Present it like slides or read it like a guide.

> Independent training material, not affiliated with or endorsed by Amazon Web Services or the
> Kiro team. All examples are fictional. Content verified against kiro.dev on **2026-11-25**.

## What you will learn
- Write EARS requirements you can test, and carry each requirement ID into a test name.
- Run Red → Green → Refactor with an agent, with a person reviewing every failing test first.
- Use property-based testing (IDE only), write strong properties, and triage a shrunk failure.
- Fix bugs with Bugfix Specs that keep unchanged behaviour under test.
- Make tests hard to skip: steering guides, hooks give feedback, required CI checks block.
- Scale the loop with custom agents, headless CI runs, the command sandbox and Workflows.
- Plus the rest of Kiro: CLI, skills, MCP and Powers, Web and remote development, Crew,
  and the November 2026 releases.
- Govern Kiro in three steps. Chapter 2, decide before you deploy: control layers, what MDM
  can and cannot guarantee, console settings, a MAS TRM mapping and a sign-off checklist.
  Chapter 7, roll out with MDM: `managed-settings.json`, workspace trust, an Intune Win32 app,
  lock / detect / repair on every OS, managed updates. Chapter 8, monitor and audit: Kiro's
  records (prompt logging, CSV report, OpenTelemetry metrics and real-time events,
  CloudTrail), two reference architectures, detection rules and metrics that mislead.

## Related course
Want Kiro Crew in depth? Chapter 11 here is an overview; the companion course
**[Kiro Crew Training](https://timwukp.github.io/Kiro-Crew-Training/)** by the same author
covers it in about 60 minutes ([source](https://github.com/timwukp/Kiro-Crew-Training)).

Want working governance scripts? Chapters 2 and 7 link the companion reference repository
**[kiro-fsi-best-practices](https://github.com/timwukp/kiro-fsi-best-practices)** by the same
author: lockdown scripts for Linux, macOS and Windows, Intune wrappers, an example banking
policy, guard hooks with tests and a MAS TRM mapping. Chapter 8 links the reference monitoring
dashboard **[kiro-telemetry-dashboard](https://github.com/timwukp/kiro-telemetry-dashboard)**
(a community sample: S3 → Athena → a named-query API → CloudFront).

## Use it
Open `index.html` in a browser — there is nothing to install or build, and it works offline.

| Key | Action |
|---|---|
| ← → or Space | Previous / next slide |
| M | Chapter menu (jump anywhere) |
| L | English / 中文 |
| R | Switch between present view and reading view |

Links take query parameters: `?lang=zh` and `?mode=reading`.

## How this site was built
With the loop it teaches. The spec is in `.kiro/specs/kiro-deep-dive-site/`
(`requirements.md` with 40 acceptance criteria, `design.md`, `tasks.md`). `verify.py` was
written before any page existed; its first run against the empty repository reported
**128 checks, 73 failed**. The site was then built until it passed (now 1677 checks, 0 failed).

```
python3 verify.py                          # spec checks — prints the check count
python3 -m unittest discover -s tests -v   # mutation tests — prove the checks can fail
```

Standard library only. `verify.py` exits non-zero on any failure and when no checks run.
Its groups: structure, isolation (no external assets or network calls), bilingual parity,
content (required topics and honesty statements), honesty (forbidden overclaims), privacy,
links and repository. Every check name carries its requirement ID, and a requirement with no
check fails the run. Checks a script can't judge are listed in `design.md` → *Manual checks*.

On macOS, `python3` needs the Xcode Command Line Tools: `xcode-select --install`.

## Layout
```
index.html                     the site: 100 slides, English + Traditional Chinese
assets/css/site.css            styles (no external fonts or imports)
assets/js/site.js              paging, chapter menu, language and view mode (no network calls)
verify.py                      the executable spec
tests/test_verify.py           mutation tests for verify.py
.kiro/specs/kiro-deep-dive-site/   requirements, design and tasks for this site
.kiro/steering/                test-first, content accuracy, privacy and product guidance
.kiro/hooks/                   run the checks after saves and after each spec task
.github/workflows/verify.yml   CI: both suites on every push and pull request
VERIFIED_SOURCES.md            the kiro.dev pages each topic relies on
LICENSE · LICENSE-CONTENT.md   MIT for code, CC BY 4.0 for content
UPDATES.md · CONTRIBUTING.md · SECURITY.md
```

## Publish with GitHub Pages
1. Push this folder to the `main` branch of the repository.
2. **Settings → Pages → Build and deployment**: Source *Deploy from a branch*, branch `main`,
   folder `/ (root)`.
3. **Settings → Branches → Add rule** for `main`: require a pull request and require the
   `verify` status check. A check is only a gate once it is required.

## Keeping it current
Kiro ships changes almost weekly. Follow `CONTRIBUTING.md`: read the changelog, add or change a
check first, update the page, then update `VERIFIED_DATE`, `UPDATES.md` and
`VERIFIED_SOURCES.md` together.

## License
- **Code and configuration** (`verify.py`, `tests/`, `assets/`, `.github/`, `.kiro/`): [MIT](LICENSE).
- **Teaching content** (slide text and the Markdown documents): [CC BY 4.0](LICENSE-CONTENT.md).
  Reuse and adapt it freely, with credit.
- Kiro, AWS and Amazon names and logos, and Kiro's own documentation, are not covered by either
  licence. See `LICENSE-CONTENT.md` for details and how to credit.

Maintained by [@timwukp](https://github.com/timwukp).
