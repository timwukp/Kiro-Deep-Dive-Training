# Verified sources

All rows verified on **2026-11-25**. Claims are paraphrased on the site and linked to these pages.

| Topic | What the site relies on | Source |
|---|---|---|
| Specs | Three files; Feature (Requirements-First / Design-First), Bugfix and Quick Spec; parallel task waves | https://kiro.dev/docs/specs/ |
| Specs best practices | When to use each spec type; Analyze Requirements; Sync Files; #spec; bug descriptions; SHALL CONTINUE TO | https://kiro.dev/docs/specs/best-practices/ |
| Property-based testing | IDE only; optional by default; properties extracted from EARS; shrinking; evidence, not proof; weak properties pass while wrong | https://kiro.dev/docs/specs/correctness/ |
| Steering | Scopes, inclusion modes, AGENTS.md incl. per-folder, custom agents need resources | https://kiro.dev/docs/steering/ |
| Hooks | v1 JSON in .kiro/hooks; triggers; which triggers can block; matcher, timeout, enabled, confirm | https://kiro.dev/docs/hooks/ |
| Hook actions | Exit 0 adds stdout to context; non-zero sends stderr and blocks PreToolUse / prompt submit; command hooks use no credits | https://kiro.dev/docs/hooks/actions/ |
| Hooks best practices | Design, scope, maintenance guidance | https://kiro.dev/docs/hooks/best-practices/ |
| Skills | Progressive disclosure; SKILL.md; scopes; skill:// resources | https://kiro.dev/docs/skills/ |
| Custom agents | JSON/Markdown; tags; permissions rules; scopes; IDE and CLI only | https://kiro.dev/docs/custom-agents/ |
| Built-in tools | Tool categories; sub-agents; surface availability | https://kiro.dev/docs/tools/ |
| Permissions defaults | Read workspace and read-only git without prompting | https://kiro.dev/docs/ide/whats-new-v1/ |
| CLI 3 | Spec agent, permissions, hooks, tangent | https://kiro.dev/docs/cli/v3/ |
| Headless mode | --no-interactive, --v3/--v2, --trust-tools, --sandbox, --mode spec, stream-json, exit codes 3 and 4, hooks in headless | https://kiro.dev/docs/cli/headless/ |
| Workflows | Step, handoff, branch and join, loop, wait; built-in recipes; opt-in; token trade-off | https://kiro.dev/docs/workflows/ |
| Models | Families and Auto only — lineup and pricing linked, not quoted | https://kiro.dev/docs/models/ |
| Crew | Overview, install, channels, workflows | https://kiro.dev/docs/crew/ |
| Approve for me | Rules first, LLM review for uncovered actions, safe / unsafe / unsure outcomes, three-block fallback, off by default, paid plans, regions, version minimums, charged per review, pair with sandbox | https://kiro.dev/blog/introducing-approve-for-me/ |
| Kiro for VS Code | Same .kiro folder, specs both ways, steering transparency, approval modes, per-file review, Workspace Trust, workflows and memory opt-in, ACP for other editors | https://kiro.dev/blog/kiro-for-vs-code |
| Changelog | Memory, command sandbox, local autonomous mode, Markdown Review, Kimi K3 (Oct); Kiro for VS Code, Crew 0.13 (Nov 19); Remote SSH / Dev Containers, Enterprise Management in Frankfurt (Nov 20); Fable 5.2 Preview (Nov 23); CLI 3.6, Kiro Enterprise for iPhone (Nov 24); VPC connections, Kiro Memory in Crew (Nov 19); IDE 1.4.236 Permission Request Hooks | https://kiro.dev/changelog/ |

## Not stated as fact
- Prices, credit multipliers and per-model context sizes (they change monthly).
- The exact JSON a hook receives on stdin — the PreTaskExec / PreToolUse test gates are
  presented as a pattern to script and check.
- Exact field names for SubagentStop hooks and Workflow recipes beyond what the docs show.
- Learning outcomes or productivity numbers.
