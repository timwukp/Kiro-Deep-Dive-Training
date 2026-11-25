---
inclusion: always
---
# Test-first policy
- For any behaviour change, first write a test named after the requirement ID
  (test_R2_1_..., prop_P2_...). For this repository the tests are checks in verify.py,
  and every check name carries its requirement ID, e.g. [R4.3].
- Run it and show that it fails before writing implementation code.
- Never weaken, skip or delete a failing check to make the build pass.
  If a check looks wrong, stop and ask.
- Implementation tasks must not modify the checks written for them.
- After each task, run `python3 verify.py` and `python3 -m unittest discover -s tests`,
  and report the last line of each.
