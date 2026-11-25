---
inclusion: always
---
# Content accuracy
- Every claim about Kiro must come from a page on kiro.dev (docs or changelog) read during
  the change. Record it in VERIFIED_SOURCES.md.
- Paraphrase; do not copy long passages from the docs. Link the source on the slide.
- Do not quote prices or credit multipliers; link https://kiro.dev/docs/models/ instead.
- Label Preview and Enterprise-only features as Preview on the slide that mentions them.
- Say "recommended pattern" when combining features into a practice. Kiro has no feature named "TDD".
- When content changes, update VERIFIED_DATE in verify.py and every data-verified attribute together.
- Avoid overclaiming: property-based testing gives evidence, not proof.
- Microsoft Intune, Windows and PowerShell behaviour comes from learn.microsoft.com; link it.
- A result from the maintainer's own lab (not on kiro.dev or learn.microsoft.com) goes only on a
  slide badged "Lab observation", with the Kiro version, "no Intune tenant" and "one run".
- When two Kiro pages disagree, say "the pages differ" and teach the form safe under both.
- Never publish reproduction steps for an unfixed way around a Kiro control (SECURITY.md).
