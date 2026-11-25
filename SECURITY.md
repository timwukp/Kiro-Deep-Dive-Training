# Security policy

## Reporting a problem
If you find personal data, a credential, or a security issue in this repository, please use
GitHub's **private vulnerability reporting** (Security tab → Report a vulnerability) rather
than a public issue. If that is unavailable, open an issue that says only "security report —
please contact me" without the details.

## Findings about Kiro itself (coordinated disclosure)
If you find a way around a Kiro control — a permission policy, a sign-in control, a hook or a
permission mode — do **not** put the details in an issue, a pull request or a slide here. Report
it to the vendor first, privately, through AWS vulnerability reporting
(https://aws.amazon.com/security/vulnerability-reporting/), and publish only after a fix or with
the vendor's agreement (coordinated disclosure). The course teaches the principle — client-side
controls are a guardrail, not a security boundary — and does not publish reproduction steps for
unfixed findings (requirement R9.4, checked by a reviewer: design.md → Manual checks).

## What the repository does to stay public-safe
- `verify.py --only privacy` scans every text file for email addresses, home-directory paths,
  and access-key, private-key, GitHub, Slack and bearer-token shapes. It reports the category,
  file and line, never the matched value.
- `tests/test_verify.py` proves the scanner fails when a fake email or key is injected.
- The CI workflow runs both on every pull request, with read-only repository permissions.
- The site loads no third-party scripts, fonts or analytics, and makes no network requests.

## Limits
- A clean scan does not prove the repository contains no personal data. The scanner does not
  detect names or free-form text; human review is still required (design.md → Manual checks, R5.2).
- Kiro hooks in `.kiro/hooks/` give feedback while editing; they do not block. The required
  CI check is the backstop, and only when branch protection makes it required.
- If a real credential is ever committed, rotate it immediately — removing it from history is
  not enough.
