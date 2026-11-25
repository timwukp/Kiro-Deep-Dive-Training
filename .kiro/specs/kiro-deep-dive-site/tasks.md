# Tasks — Kiro Deep Dive training site

- [x] 1. Write requirements.md — 8 requirements, 23 acceptance criteria with IDs
- [x] 2. Write verify.py before any page content (Red)
  - Evidence: `python3 verify.py` on the empty repository → 128 checks, 73 failed
  - _Requirements: all_
- [x] 3. Write design.md, including the manual checks for criteria a script can't judge
- [x] 4. Styles and navigation script: offline, present/reading modes, Left/Right paging, chapter menu, language toggle
  - _Requirements: R1.1, R1.2, R1.3, R2.2, R6.1, R6.2, R7.2, R7.3_
- [x] 5. Write the eight chapters in English and Traditional Chinese, Chapter 1 deepened for SDD and TDD
  - _Requirements: R2.1, R3.1, R3.2, R4.1–R4.4, R5.2, R6.3, R7.1_
- [x] 6. Repository documents, steering, hooks and CI workflow (Green)
  - Evidence: `python3 verify.py` → 885 checks, 0 failed
  - _Requirements: R5.1, R8.1, R8.2, R8.3_
- [x] 7. Mutation tests that break one rule each and prove the verifier notices
  - Evidence: `python3 -m unittest discover -s tests -v` → 10 tests, OK
- [x] 10. v1.1: add features from the IDE What's new panel (Approve for me, Memory, Workflows recipes, remote environments, VPC, Kiro for VS Code)
  - Red: 8 new topic checks added to verify.py → 893 checks, 5 failed
  - Green: content added in chapters 1, 2, 3, 4, 5, 7 and 8 → 927 checks, 0 failed
  - _Requirements: R3.1_
- [x] 11. v1.1.1: licences — MIT for code, CC BY 4.0 for content
  - Red: R8.4 checks added → 933 checks, 5 failed
  - Green: LICENSE, LICENSE-CONTENT.md, README and slide text → 937 checks, 0 failed
  - _Requirements: R8.4_
- [x] 12. v1.1.2: link the Kiro Crew Training course from Chapter 8 and the closing slide
  - Red: R3.3 checks added → 940 checks, 2 failed
  - Green: divider note, new slide, closing card, sources row, README → 964 checks, 0 failed
  - _Requirements: R3.3_
- [x] 13. v1.2.0: Chapter 9, enterprise governance with MDM; hook exit-code correction
  - Plan: critical review of the lab reports first (evidence strength, disclosure, customer
    neutrality, MDM ≠ enforcement); vendor docs for Kiro claims, Microsoft Learn for Intune,
    lab results only on slides badged "Lab observation"
  - Red: Requirement 9 (R9.1–R9.5) and its checks added first → 996 checks, 24 failed
  - Green: 13 slides in Chapter 9, agenda, takeaways, sources, hook exit-2 fix → 1186 checks, 0 failed
  - Review against the companion repo kiro-fsi-best-practices (re-checked on kiro.dev): R9.6–R9.8
    added first → 1205 checks, 13 failed; 6 new slides and fixes → 1320 checks, 0 failed
  - 7 mutation tests added (R9.2–R9.8), 17 in total
  - _Requirements: R9.1–R9.8_
- [x] 15. v1.3.0: customer-journey order, governance split into Chapters 2 and 7, new Chapter 8 (monitor)
  - Red: R10 and R11 checks added, chapters found by topic → 1365 checks, 64 failed
  - Green: renumbered chapters, 2 new dividers, sign-off checklist, 7 monitoring slides, agenda
    tracks, linked chapter references → 1677 checks, 0 failed
  - 5 mutation tests added (R10.2, R10.3, R10.5, R11.1, R11.3), 22 in total
  - _Requirements: R3.3, R9.1–R9.8, R10.1–R10.5, R11.1–R11.3_
- [ ] 14. R9.4 reviewer check before merge (design.md → Manual checks) — maintainer
- [ ] 8. Manual checks before the first release (design.md → Manual checks) — maintainer
- [ ] 9. Push to GitHub, enable Pages, make the `verify` job a required status check — maintainer
