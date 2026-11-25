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
| Hooks v1 schema (IDE 1.0) | Only exit 2 blocks PreToolUse, UserPromptSubmit and PreTaskExec; other non-zero codes are errors — **differs from Hook actions**, so the site teaches exit 2 | https://kiro.dev/docs/ide/whats-new-v1/hooks/ |
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
| Kiro Crew Training (companion course) | What the course covers; Crew uses Kiro subscription credits; setup through kiro-cli, no AWS account or Bedrock; verified by its author on 2026-08-31 | https://github.com/timwukp/Kiro-Crew-Training |
| Permission policies (Ch. 2, 7) | managed-settings.json; deny > ask > allow; admin rules deny/ask only; client-enforced, local admins can circumvent; macOS path; MDM (Jamf, Kandji); malformed file fails closed; unknown fields reject the file; restart Kiro; Enterprise Management (Preview) | https://kiro.dev/docs/enterprise/governance/permissions/ |
| Sign-in controls (Ch. 2, 7) | signin_method rules and method names (idc, external_idp…); settings keys; enforced by the installed client; fails open; BOM / non-UTF-8 invalid; Linux path /etc/kiro/managed-settings.json; AuthPortalUrl under HKLM\SOFTWARE\Policies\Kiro | https://kiro.dev/docs/enterprise/governance/sign-in/ |
| Managed updates (Ch. 2, 7) | UpdateMode=none (HKLM\SOFTWARE\Policies\Kiro, REG_SZ); UpdateUrl manifests; -system default Windows variant; phased rollout, 3–7 days; pinning ≠ locking; block download hosts; CLI update.baseUrl, app.disableAutoupdates, KIRO_NO_AUTO_UPDATE | https://kiro.dev/docs/enterprise/managed-updates/ |
| MCP governance (Ch. 2, 7) | Toggle and registry per org/account; client-enforced; fails closed if the governance API is unreachable; not for Builder ID / social users | https://kiro.dev/docs/enterprise/governance/mcp/ |
| API keys (Ch. 2, 7) | Off by default; console toggle | https://kiro.dev/docs/enterprise/governance/api-keys/ |
| Prompt logging (Ch. 8) | Prompts and responses from IDE and CLI to an S3 bucket in your account, in the profile's Region; console toggle | https://kiro.dev/docs/enterprise/monitor-and-track/prompt-logging/ |
| Per-user activity and OpenTelemetry (Ch. 8) | CSV daily 02:00 UTC to S3 incl. GovCloud; OTel metrics daily 00:30 UTC (kiro.daily.*); real-time events per LLM request and tool call in us-east-1 and eu-central-1; KMS key and secret; public internet by default, PrivateLink or VPC Lattice; Kiro does not notify on delivery success or failure; no prompts, responses or code; IdC or external IdP user ID; users cannot turn exports off | https://kiro.dev/docs/enterprise/monitor-and-track/user-activity/ |
| CloudTrail (Ch. 8) | Kiro service MCP tool calls only; arguments replaced; us-east-1 and eu-central-1 | https://kiro.dev/docs/enterprise/monitor-and-track/cloudtrail/ |
| Reference dashboard (Ch. 8) | Architecture A (S3, Glue, Athena, named-query API, cache, CloudFront, Cognito); a community sample by the maintainer, MIT-0 | https://github.com/timwukp/kiro-telemetry-dashboard |
| Permissions — workspace trust (Ch. 2, 7) | Untrusted workspaces do not load agents, steering, MCP config, skills or workflows; ask before every shell and MCP call; decision stored outside the repo; hardcoded always-deny and always-ask paths | https://kiro.dev/docs/permissions/ |
| Steering — team steering (Ch. 2, 7) | Team steering can be pushed to ~/.kiro/steering via MDM or Group Policy | https://kiro.dev/docs/steering/ |
| Enterprise Management (Ch. 2, 7) | Preview in us-east-1 and eu-central-1; rules, settings, files; IDE, CLI and Kiro Web; "Enforced" (service) vs "Client rollout" (client) capabilities; migration one-way | https://kiro.dev/docs/enterprise/enterprise-management/ |
| Model governance (Ch. 2, 7) | Approved list; with it on, new models stay unavailable until selected | https://kiro.dev/docs/enterprise/governance/model/ |
| Web tools governance (Ch. 2, 7) | On/off for web_search and web_fetch | https://kiro.dev/docs/enterprise/governance/web-tools/ |
| Windows system-wide installer (Ch. 2, 7) | Added in IDE 1.4.62 | https://kiro.dev/changelog/ide/1-4-62/ |
| Intune Win32 apps, Remediations (Ch. 2, 7) | Detection rules, 32-bit setting, dependencies; detection + remediation scripts | https://learn.microsoft.com/en-us/intune/app-management/deployment/add-win32 · https://learn.microsoft.com/en-us/intune/device-management/tools/deploy-remediations |
| Intune detection conventions (Ch. 2, 7) | Remediations: detection exit 1 runs the remediation; Win32 custom detection: exit 0 and STDOUT | https://learn.microsoft.com/en-us/intune/device-management/tools/deploy-remediations · https://learn.microsoft.com/en-us/intune/app-management/deployment/add-win32 |
| MAS TRM (Ch. 2, 7) | Section numbers of the January 2021 guidelines (3.4, 6.3, 7.5, 9.1, 9.2, 11.1, 11.2, 12.2); the mapping is the author's interpretation. The MAS page could not be fetched from the build environment — open it to confirm | https://www.mas.gov.sg/regulation/guidelines/technology-risk-management-guidelines |
| kiro-fsi-best-practices (companion repo, Ch. 2, 7) | Source of patterns re-checked on kiro.dev: device policy does not reach Kiro Web, OS file locks, per-MDM drift conventions, fail-closed guards; personal work with its own dates | https://github.com/timwukp/kiro-fsi-best-practices |
| App Control script enforcement, language modes (Ch. 2, 7) | Scripts the policy does not allow run in Constrained Language Mode | https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/design/script-enforcement |
| Changelog | Memory, command sandbox, local autonomous mode, Markdown Review, Kimi K3 (Oct); Kiro for VS Code, Crew 0.13 (Nov 19); Remote SSH / Dev Containers, Enterprise Management in Frankfurt (Nov 20); Fable 5.2 Preview (Nov 23); CLI 3.6, Kiro Enterprise for iPhone (Nov 24); VPC connections, Kiro Memory in Crew (Nov 19); IDE 1.4.236 Permission Request Hooks | https://kiro.dev/changelog/ |

## Lab observations (Chapters 2 and 7, badged on the slide)
From the maintainer's own tests: one Windows 11 Enterprise Evaluation VM, Kiro IDE 1.5.11 (some
results 1.4.236), Intune contexts emulated with SYSTEM scheduled tasks, no Intune tenant, one run
per result. Silent-install switches, per-user build as SYSTEM, `/MERGETASKS=!runcode`, `/LOG=`
folder, registry view, PowerShell 5.1 encodings, locked-file overwrite, silent exit 0, Constrained
Language Mode, global hooks running in the IDE. Not vendor documentation.

## Not stated as fact
- The Windows path of managed-settings.json is given as the path used in the lab; the
  Permission policies page shows it on its Windows tab, which the text fetch did not render.
- Reproduction details of unfixed ways around Kiro controls (coordinated disclosure, SECURITY.md).
- From the companion repo, not imported: its model approval matrix and credit multipliers
  (volatile), and statements it dates before newer kiro.dev pages (Enterprise Management Regions,
  CloudTrail event names).
- Prices, credit multipliers and per-model context sizes (they change monthly).
- The exact JSON a hook receives on stdin — the PreTaskExec / PreToolUse test gates are
  presented as a pattern to script and check.
- Exact field names for SubagentStop hooks and Workflow recipes beyond what the docs show.
- Learning outcomes or productivity numbers.
