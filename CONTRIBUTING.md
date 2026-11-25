# Contributing

Changes follow the same loop the site teaches.

1. **Find the source.** Read the Kiro changelog (https://kiro.dev/changelog/) or the doc page
   you are reflecting. Note the URL.
2. **Spec first.** If the change adds a new rule for the site, add an acceptance criterion with
   a new ID to `.kiro/specs/kiro-deep-dive-site/requirements.md`.
3. **Red.** Add or change a check in `verify.py` whose name carries that ID. Run
   `python3 verify.py` and confirm it fails.
4. **Green.** Edit `index.html` (and CSS/JS if needed). Every string needs both an English
   `<span class="en">` and a Traditional Chinese `<span class="zh" lang="zh-Hant">`.
5. **Refactor**, keeping both suites green:
   `python3 verify.py` and `python3 -m unittest discover -s tests -v`.
6. **Record it.** Update `VERIFIED_DATE` in `verify.py` and every `data-verified` attribute when
   you re-verify content; add a line to `UPDATES.md`; add or update rows in
   `VERIFIED_SOURCES.md`.
7. **Pull request** with the template filled in, including the manual checks.

## Rules
- Paraphrase the docs and link them; don't copy long passages.
- No prices or credit multipliers — link the models page.
- Label Preview features as Preview.
- Fictional examples only. No emails, internal links, customer or employer names.

## Licence of contributions
By opening a pull request you agree that your contribution is licensed under the same terms as
the part of the repository it changes: MIT for code and configuration, CC BY 4.0 for content.

On macOS, `python3` needs the Xcode Command Line Tools (`xcode-select --install`).
