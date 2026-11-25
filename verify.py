#!/usr/bin/env python3
"""verify.py - the executable specification for this training site.

It was written before the site existed, and the site was built until it passed
(Red -> Green -> Refactor). Standard library only; nothing to install.

    python3 verify.py                       # every group
    python3 verify.py --only privacy,links  # selected groups
    python3 verify.py --root PATH           # check another checkout (used by tests/)

Every check name carries the requirement ID it covers, e.g. [R5.1], matching
.kiro/specs/kiro-deep-dive-site/requirements.md. Prints each failure and the total
number of checks; exits 1 on any failure and 2 on a usage error, so a run that
silently checks nothing is visible rather than reported as success.
"""
import argparse
import json
import os
import re
import sys
from html.parser import HTMLParser

VERIFIED_DATE = "2026-11-25"
LIVE_URL = "https://timwukp.github.io/Kiro-Deep-Dive-Training/"
CHAPTERS = ["ch%d" % i for i in range(1, 9)]
GROUPS = ["structure", "isolation", "bilingual", "content", "honesty", "privacy", "links", "repo"]
MIN_SLIDES = 50

# [R3.1] SDD + TDD topics the course must teach (matched in visible English text).
REQUIRED_TOPICS = [
    "EARS", "requirements.md", "design.md", "tasks.md", "Analyze Requirements",
    "property-based testing", "shrinking", "Bugfix Spec", "SHALL CONTINUE TO",
    "Red", "Green", "Refactor", "traceability", "PreToolUse", "PreTaskExec",
    "PostTaskExec", "--no-interactive", "--sandbox", "Workflows", "Steering", "Hooks",
    # v1.1 — approval controls, remote development and Kiro for VS Code
    "Approve for me", "Permission Request Hook", "recipe", "Dev Container", "Connect to Host",
    "VPC", "Workspace Trust", "Memory",
]
# [R3.2] honesty statements that must be present.
REQUIRED_STATEMENTS = [
    "no feature named", "evidence, not proof", "IDE only",
    "not affiliated with or endorsed by", "fictional",
]
# [R4.4] overclaiming phrases a training page must never use (English + Chinese).
FORBIDDEN = [
    "guarantees correctness", "guaranteed to be correct", "bug-free", "zero bugs",
    "100% coverage", "proves your code", "official tdd feature", "tdd mode",
    "fully autonomous", "never fails", "always correct",
    "保證正確", "零錯誤", "零 bug", "完全沒有錯誤", "100% 覆蓋",
]
# [R4.2] features that are Preview at the verification date.
PREVIEW_TERMS = ["Fable 5.2", "Enterprise Management", "Dynamic Dashboard", "Remote Crews"]
# [R4.3] credit multipliers change often - link to the models page instead of quoting them.
VOLATILE = re.compile(r"\b\d+(?:\.\d+)?x\b")
# [R5.1] high-confidence sensitive data.
PRIVACY = {
    "email": re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}"),
    "home-path": re.compile(r"(?:/Users/|/home/)[A-Za-z0-9._-]+/|[A-Za-z]:\\\\Users\\\\"),
    "aws-access-key": re.compile(r"\b(?:AKIA|ASIA)[0-9A-Z]{16}\b"),
    "private-key": re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    "github-token": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b"),
    "slack-token": re.compile(r"\bxox[abprs]-[A-Za-z0-9-]{10,}\b"),
    "bearer-token": re.compile(r"(?i)\bbearer\s+[A-Za-z0-9._~+/=-]{24,}"),
}
EMAIL_ALLOW_DOMAINS = ("example.com", "example.org", "users.noreply.github.com")
TEXT_EXT = (".html", ".css", ".js", ".md", ".py", ".json", ".yml", ".yaml", ".txt", ".sh", ".svg")
HOOK_TRIGGERS = {
    "PostFileSave", "PostFileCreate", "PostFileDelete", "PreToolUse", "PostToolUse",
    "UserPromptSubmit", "SessionStart", "Stop", "PreTaskExec", "PostTaskExec", "SubagentStop",
}
REQUIRED_FILES = [
    "index.html", "assets/css/site.css", "assets/js/site.js", "README.md", "SECURITY.md",
    "UPDATES.md", "VERIFIED_SOURCES.md", "CONTRIBUTING.md", ".nojekyll",
    ".github/workflows/verify.yml", ".github/pull_request_template.md",
    ".kiro/specs/kiro-deep-dive-site/requirements.md",
    ".kiro/specs/kiro-deep-dive-site/design.md",
    ".kiro/specs/kiro-deep-dive-site/tasks.md",
    ".kiro/steering/test-first.md", ".kiro/steering/content-accuracy.md",
    ".kiro/steering/privacy.md", "tests/test_verify.py",
]
CJK = re.compile(r"[\u3400-\u9fff]")
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta",
        "source", "track", "wbr"}


class Page(HTMLParser):
    """Collects structure and visible text, split by language span."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack, self.elements, self.ids, self.slides = [], [], set(), []
        self.h1 = 0
        self.cur = None
        self.text = []  # (lang, in_code, data)

    def _start(self, tag, attrs, push):
        a = {k: (v or "") for k, v in attrs}
        cls = a.get("class", "").split()
        if a.get("id"):
            self.ids.add(a["id"])
        self.elements.append({"tag": tag, "attrs": a, "cls": cls})
        if tag == "h1":
            self.h1 += 1
        if tag == "section" and "slide" in cls:
            self.cur = {"id": a.get("id", ""), "attrs": a, "cls": cls, "en": 0, "zh": 0,
                        "text_en": [], "text_zh": [], "code": []}
            self.slides.append(self.cur)
        if self.cur is not None:
            if "en" in cls:
                self.cur["en"] += 1
            if "zh" in cls:
                self.cur["zh"] += 1
        if push and tag not in VOID:
            self.stack.append((tag, cls))

    def handle_starttag(self, tag, attrs):
        self._start(tag, attrs, True)

    def handle_startendtag(self, tag, attrs):
        self._start(tag, attrs, False)

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                del self.stack[i:]
                break
        if tag == "section" and not any(t == "section" for t, _ in self.stack):
            self.cur = None

    def handle_data(self, data):
        tags = [t for t, _ in self.stack]
        if "script" in tags or "style" in tags or not data.strip():
            return
        in_code = "pre" in tags or "code" in tags
        langs = [c for _, cls in self.stack for c in cls if c in ("en", "zh")]
        lang = langs[-1] if langs else None
        self.text.append((lang, in_code, data))
        if self.cur is not None:
            if in_code:
                self.cur["code"].append(data)
            if lang in (None, "en"):
                self.cur["text_en"].append(data)
            if lang in (None, "zh"):
                self.cur["text_zh"].append(data)


class Runner:
    def __init__(self, root, groups):
        self.root, self.groups = root, groups
        self.count, self.failures = 0, []

    def check(self, group, name, ok, detail=""):
        if group not in self.groups:
            return
        self.count += 1
        if not ok:
            self.failures.append("[%s] %s%s" % (group, name, (" - " + detail) if detail else ""))

    def read(self, rel):
        p = os.path.join(self.root, rel)
        if not os.path.isfile(p):
            return None
        with open(p, encoding="utf-8") as f:
            return f.read()


def visible(page, langs=("en", None), code=False):
    return " ".join(d for l, c, d in page.text if l in langs and (code or not c))


def run(root, groups):
    r = Runner(root, groups)
    html = r.read("index.html")
    r.check("structure", "[R7.1] index.html exists", html is not None)
    page = Page()
    if html is not None:
        page.feed(html)
    css = r.read("assets/css/site.css") or ""
    js = r.read("assets/js/site.js") or ""
    slides = page.slides
    en_text = visible(page)
    all_text = visible(page, ("en", "zh", None))

    # ---- structure -------------------------------------------------------------
    tags = [e["tag"] for e in page.elements]
    attrs_of = lambda t: [e["attrs"] for e in page.elements if e["tag"] == t]
    r.check("structure", "[R7.1] exactly one h1", page.h1 == 1, "found %d" % page.h1)
    html_attrs = attrs_of("html")
    r.check("structure", "[R7.1] <html lang> set", bool(html_attrs and html_attrs[0].get("lang")))
    r.check("structure", "[R7.1] <title> present", "title" in tags)
    r.check("structure", "[R7.3] viewport meta present",
            any(a.get("name") == "viewport" for a in attrs_of("meta")))
    r.check("structure", "[R7.1] description meta present",
            any(a.get("name") == "description" for a in attrs_of("meta")))
    r.check("structure", "[R7.2] skip link targets #main",
            any(a.get("href") == "#main" and "skip-link" in a.get("class", "") for a in attrs_of("a")))
    r.check("structure", "[R7.1] <main id=main> landmark",
            any(a.get("id") == "main" for a in attrs_of("main")))
    r.check("structure", "[R6.2] chapter menu <nav> with label",
            any(a.get("aria-label") for a in attrs_of("nav")))
    for bid in ("nav-toggle", "lang-toggle", "mode-toggle", "prev", "next"):
        r.check("structure", "[R6.1] control #%s present" % bid, bid in page.ids)
    r.check("structure", "[R6.1] at least %d slides" % MIN_SLIDES, len(slides) >= MIN_SLIDES,
            "found %d" % len(slides))
    seen = set()
    for s in slides:
        sid = s["id"]
        r.check("structure", "[R6.3] slide has unique id", bool(sid) and sid not in seen, sid or "(none)")
        seen.add(sid)
        r.check("structure", "[R6.2] slide %s has data-chapter" % sid, bool(s["attrs"].get("data-chapter")))
        r.check("structure", "[R1.3] slide %s not hidden in markup" % sid, "hidden" not in s["attrs"])
    for ch in CHAPTERS:
        div = [s for s in slides if s["attrs"].get("data-chapter") == ch and "chapter" in s["cls"]]
        r.check("structure", "[R4.1] %s has a chapter divider" % ch, len(div) == 1, "found %d" % len(div))
        if div:
            r.check("structure", "[R4.1] %s divider data-verified=%s" % (ch, VERIFIED_DATE),
                    div[0]["attrs"].get("data-verified") == VERIFIED_DATE)
    unscoped = re.search(r"(^|})\s*\.slide\s*\{[^}]*display\s*:\s*none", css)
    r.check("structure", "[R1.3] slides hidden only under html.present", unscoped is None)
    r.check("structure", "[R7.3] responsive root font uses clamp()", "clamp(" in css)
    r.check("structure", "[R7.2] visible focus style", ":focus-visible" in css)
    r.check("structure", "[R7.2] reduced-motion respected", "prefers-reduced-motion" in css)
    r.check("structure", "[R6.1] ArrowRight/ArrowLeft handled", "ArrowRight" in js and "ArrowLeft" in js)
    r.check("structure", "[R6.1] ArrowUp/ArrowDown not used for paging",
            "ArrowUp" not in js and "ArrowDown" not in js)
    r.check("structure", "[R2.2] language choice persisted", "localStorage" in js and "lang" in js)

    # ---- isolation -------------------------------------------------------------
    ext = re.compile(r"^(?:https?:)?//", re.I)
    for e in page.elements:
        a = e["attrs"]
        for key in ("src", "srcset", "data", "poster"):
            if a.get(key):
                r.check("isolation", "[R1.1] <%s %s> is local" % (e["tag"], key), not ext.match(a[key]), a[key])
        if e["tag"] == "link" and a.get("href"):
            r.check("isolation", "[R1.1] <link href> is local", not ext.match(a["href"]), a["href"])
        if e["tag"] in ("iframe", "embed", "object"):
            r.check("isolation", "[R1.1] no <%s>" % e["tag"], False)
    for e in page.elements:
        a = e["attrs"]
        local = (e["tag"] == "script" and a.get("src")) or (e["tag"] == "link" and a.get("href"))
        if local and not ext.match(local):
            r.check("isolation", "[R1.1] referenced asset exists: %s" % local,
                    os.path.isfile(os.path.join(root, local)))
    for name, src in (("site.css", css), ("site.js", js), ("index.html", html or "")):
        r.check("isolation", "[R1.1] %s has no remote url()" % name,
                re.search(r"url\(\s*['\"]?(?:https?:)?//", src, re.I) is None)
        r.check("isolation", "[R1.1] %s has no @import" % name, "@import" not in src)
    for api in ("fetch(", "XMLHttpRequest", "WebSocket", "sendBeacon", "EventSource"):
        r.check("isolation", "[R1.2] site.js makes no network call (%s)" % api, api not in js)

    # ---- bilingual -------------------------------------------------------------
    for s in slides:
        sid = s["id"]
        r.check("bilingual", "[R2.1] %s has English and Chinese spans" % sid, s["en"] > 0 and s["zh"] > 0)
        r.check("bilingual", "[R2.1] %s en/zh span counts match" % sid, s["en"] == s["zh"],
                "en=%d zh=%d" % (s["en"], s["zh"]))
        zh = " ".join(t for t in s["text_zh"] if t not in s["code"])
        r.check("bilingual", "[R2.1] %s Chinese text is Chinese" % sid, CJK.search(zh) is not None)

    # ---- content ---------------------------------------------------------------
    low = en_text.lower()
    for term in REQUIRED_TOPICS:
        hit = re.search(r"(?<![A-Za-z])" + re.escape(term) + r"(?![A-Za-z])", en_text + " " +
                        visible(page, code=True), re.I) is not None
        r.check("content", "[R3.1] teaches '%s'" % term, hit)
    for st in REQUIRED_STATEMENTS:
        r.check("content", "[R3.2] states '%s'" % st, st.lower() in low)
    r.check("content", "[R4.1] verification date shown", VERIFIED_DATE in all_text)
    for s in slides:
        body = " ".join(s["text_en"])
        for term in PREVIEW_TERMS:
            if term in body:
                r.check("content", "[R4.2] %s labels %s as Preview" % (s["id"], term), "Preview" in body)
        prose = " ".join(t for t in s["text_en"] if t not in s["code"])
        m = VOLATILE.search(prose)
        r.check("content", "[R4.3] %s quotes no credit multiplier" % s["id"], m is None,
                m.group(0) if m else "")

    # ---- honesty ---------------------------------------------------------------
    alow = all_text.lower()
    for phrase in FORBIDDEN:
        r.check("honesty", "[R4.4] no overclaim '%s'" % phrase, phrase.lower() not in alow)

    # ---- privacy ---------------------------------------------------------------
    scanned = 0
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in (".git", "node_modules", "__pycache__")]
        for fn in filenames:
            if not fn.lower().endswith(TEXT_EXT):
                continue
            rel = os.path.relpath(os.path.join(dirpath, fn), root)
            with open(os.path.join(dirpath, fn), encoding="utf-8", errors="replace") as f:
                src = f.read()
            scanned += 1
            for cat, rx in PRIVACY.items():
                for m in rx.finditer(src):
                    if cat == "email" and m.group(0).lower().endswith(EMAIL_ALLOW_DOMAINS):
                        continue
                    line = src.count("\n", 0, m.start()) + 1
                    # never print the matched value
                    r.check("privacy", "[R5.1] %s at %s:%d" % (cat, rel, line), False)
    r.check("privacy", "[R5.1] scanned the repository", scanned >= 10, "%d files" % scanned)

    # ---- links -----------------------------------------------------------------
    for e in page.elements:
        href = e["attrs"].get("href", "")
        if e["tag"] != "a" or not href:
            continue
        if href.startswith("#"):
            r.check("links", "[R6.3] anchor %s resolves" % href, href[1:] in page.ids)
        elif ext.match(href):
            r.check("links", "[R6.3] external link is https: %s" % href, href.startswith("https://"))
            r.check("links", "[R6.3] external link opens safely: %s" % href,
                    "noopener" in e["attrs"].get("rel", ""))
        else:
            target = href.split("#")[0]
            r.check("links", "[R6.3] local link exists: %s" % href, os.path.exists(os.path.join(root, target)))

    # ---- repo ------------------------------------------------------------------
    for rel in REQUIRED_FILES:
        r.check("repo", "[R8.1] %s exists" % rel, os.path.exists(os.path.join(root, rel)))
    readme = r.read("README.md") or ""
    r.check("repo", "[R8.1] README links the live site", LIVE_URL in readme)
    hooks_dir = os.path.join(root, ".kiro", "hooks")
    hook_files = sorted(f for f in os.listdir(hooks_dir) if f.endswith(".json")) if os.path.isdir(hooks_dir) else []
    r.check("repo", "[R8.2] at least one Kiro hook file", len(hook_files) >= 1)
    for hf in hook_files:
        try:
            with open(os.path.join(hooks_dir, hf), encoding="utf-8") as f:
                doc = json.load(f)
            ok = doc.get("version") == "v1" and isinstance(doc.get("hooks"), list) and all(
                h.get("name") and h.get("trigger") in HOOK_TRIGGERS
                and (h.get("action") or {}).get("type") in ("command", "agent") for h in doc["hooks"])
        except (ValueError, OSError):
            ok = False
        r.check("repo", "[R8.2] hook %s is valid v1" % hf, ok)
    lic = r.read("LICENSE") or ""
    r.check("repo", "[R8.4] LICENSE is the MIT licence", "MIT License" in lic and "Permission is hereby granted" in lic)
    licc = r.read("LICENSE-CONTENT.md") or ""
    r.check("repo", "[R8.4] LICENSE-CONTENT.md is CC BY 4.0",
            "CC BY 4.0" in licc and "https://creativecommons.org/licenses/by/4.0/" in licc)
    r.check("repo", "[R8.4] licence excludes Kiro names and docs",
            "not covered" in licc.lower() and "kiro" in licc.lower())
    r.check("repo", "[R8.4] README has a License section", "## License" in readme)
    end = [s for s in slides if s["id"] == "s-end"]
    end_text = " ".join(end[0]["text_en"]) if end else ""
    r.check("repo", "[R8.4] closing slide states the licence", "MIT" in end_text and "CC BY 4.0" in end_text)
    reqs = r.read(".kiro/specs/kiro-deep-dive-site/requirements.md") or ""
    ids = sorted(set(re.findall(r"\bR(\d+\.\d+)\b", reqs)))
    r.check("repo", "[R8.3] requirements.md declares requirement IDs", len(ids) >= 10, "%d ids" % len(ids))
    me = r.read("verify.py") or ""
    design = r.read(".kiro/specs/kiro-deep-dive-site/design.md") or ""
    for rid in ids:
        covered = ("[R%s]" % rid) in me or ("R%s" % rid) in design.split("## Manual checks")[-1]
        r.check("repo", "[R8.3] requirement R%s has a check (automated or manual)" % rid, covered)
    return r


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--root", default=os.path.dirname(os.path.abspath(__file__)))
    ap.add_argument("--only", default="", help="comma-separated groups: " + ",".join(GROUPS))
    args = ap.parse_args(argv)
    groups = [g.strip() for g in args.only.split(",") if g.strip()] or GROUPS
    bad = [g for g in groups if g not in GROUPS]
    if bad:
        print("unknown group(s): " + ", ".join(bad), file=sys.stderr)
        return 2
    r = run(os.path.abspath(args.root), groups)
    for f in r.failures:
        print("FAIL " + f)
    print("verify.py: %d checks, %d failed (%s)" % (r.count, len(r.failures), ", ".join(groups)))
    if r.count == 0:
        print("verify.py: no checks ran - treating as failure", file=sys.stderr)
        return 1
    return 1 if r.failures else 0


if __name__ == "__main__":
    sys.exit(main())
