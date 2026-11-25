## What changed and why

## Kiro release or doc page this follows (if any)

## Evidence
- [ ] `python3 verify.py` — paste the last line: `verify.py: ___ checks, 0 failed`
- [ ] `python3 -m unittest discover -s tests -v` — all passed
- [ ] If content changed: `VERIFIED_DATE` in verify.py, every `data-verified`, `UPDATES.md` and `VERIFIED_SOURCES.md` updated together

## Manual checks (design.md → Manual checks)
- [ ] R2.2 language toggle and reload keep the choice
- [ ] R6.1 Left/Right/Space move one slide; Up/Down do not page
- [ ] R6.2 chapter menu (M) jumps correctly
- [ ] R7.2 keyboard-only pass with visible focus
- [ ] R7.3 checked at phone, laptop and wide widths
- [ ] R5.2 examples are fictional; no customer or personal names
- [ ] R1.3 readable with JavaScript disabled
