"""Mutation tests for verify.py: each test breaks one rule in a copy of the
repository and asserts the verifier notices. A checker that passes everything
is not a test, so these prove the checks can fail (Red) as well as pass (Green).

    python3 -m unittest discover -s tests -v
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VERIFY = os.path.join(ROOT, "verify.py")


def copy_tree(src, dst):
    """Copy file contents only (no metadata), skipping .git and caches."""
    for dirpath, dirnames, filenames in os.walk(src):
        dirnames[:] = [d for d in dirnames if d not in (".git", "__pycache__")]
        target = os.path.join(dst, os.path.relpath(dirpath, src))
        os.makedirs(target, exist_ok=True)
        for fn in filenames:
            shutil.copyfile(os.path.join(dirpath, fn), os.path.join(target, fn))


def run_verify(root, only=""):
    cmd = [sys.executable, VERIFY, "--root", root] + (["--only", only] if only else [])
    p = subprocess.run(cmd, capture_output=True, text=True)
    return p.returncode, p.stdout + p.stderr


class MutationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.copy = os.path.join(self.tmp, "site")
        copy_tree(ROOT, self.copy)

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def edit(self, rel, fn):
        p = os.path.join(self.copy, rel)
        with open(p, encoding="utf-8") as f:
            src = f.read()
        new = fn(src)
        self.assertNotEqual(src, new, "mutation did not change " + rel)
        with open(p, "w", encoding="utf-8") as f:
            f.write(new)

    def assertFails(self, only, needle):
        code, out = run_verify(self.copy, only)
        self.assertEqual(code, 1, out)
        self.assertIn(needle, out)

    def test_baseline_passes(self):
        code, out = run_verify(self.copy)
        self.assertEqual(code, 0, out)

    def test_R5_1_email_is_caught(self):
        addr = "someone" + "@" + "corp-mail" + ".net"   # built at runtime so this file stays clean
        self.edit("index.html", lambda s: s.replace("</main>", "<p>" + addr + "</p></main>", 1))
        self.assertFails("privacy", "[R5.1] email")

    def test_R5_1_access_key_is_caught(self):
        key = "AKIA" + "Q" * 16
        self.edit("README.md", lambda s: s + "\n" + key + "\n")
        self.assertFails("privacy", "[R5.1] aws-access-key")

    def test_R1_1_remote_script_is_caught(self):
        self.edit("index.html", lambda s: s.replace("</body>", '<script src="https://cdn.example.com/x.js"></script></body>', 1))
        self.assertFails("isolation", "[R1.1]")

    def test_R2_1_missing_translation_is_caught(self):
        def drop_first_zh(s):
            i = s.index("<main")
            return s[:i] + re.sub(r'<span class="zh" lang="zh-Hant">[^<]*</span>', "", s[i:], count=1)
        self.edit("index.html", drop_first_zh)
        self.assertFails("bilingual", "[R2.1]")

    def test_R4_4_overclaim_is_caught(self):
        self.edit("index.html", lambda s: s.replace("</main>", '<p class="en">This makes your code bug-free.</p></main>', 1))
        self.assertFails("honesty", "bug-free")

    def test_R4_1_missing_verified_date_is_caught(self):
        self.edit("index.html", lambda s: s.replace('data-verified="2026-11-25"', 'data-verified="unknown"', 1))
        self.assertFails("structure", "[R4.1]")

    def test_R4_3_credit_multiplier_is_caught(self):
        def add_multiplier(s):
            i = s.index("<main")
            return s[:i] + s[i:].replace('<span class="en">', '<span class="en">Costs 2.4x credits. ', 1)
        self.edit("index.html", add_multiplier)
        self.assertFails("content", "[R4.3]")

    def test_R6_3_broken_anchor_is_caught(self):
        self.edit("index.html", lambda s: s.replace("</main>", '<a href="#no-such-slide">x</a></main>', 1))
        self.assertFails("links", "[R6.3]")

    def test_R6_1_vertical_paging_is_caught(self):
        self.edit("assets/js/site.js", lambda s: s + "\n// ArrowDown\n")
        self.assertFails("structure", "[R6.1]")

    def test_R9_2_missing_boundary_statement_is_caught(self):
        self.edit("index.html", lambda s: s.replace("guardrail, not a security boundary", "useful control"))
        self.assertFails("content", "[R9.2]")

    def test_R9_3_unlabelled_lab_slide_is_caught(self):
        def drop_label(s):
            i = s.index('id="s-gov-intune"')
            j = s.index("</section>", i)
            return s[:i] + s[i:j].replace("no Intune tenant", "a test tenant") + s[j:]
        self.edit("index.html", drop_label)
        self.assertFails("content", "[R9.3] s-gov-intune")

    def test_R9_5_any_nonzero_claim_is_caught(self):
        self.edit("index.html", lambda s: s.replace("</main>", '<p class="en">Any non-zero exit blocks the call.</p></main>', 1))
        self.assertFails("honesty", "any non-zero exit blocks")

    def test_R9_4_missing_disclosure_rule_is_caught(self):
        self.edit("SECURITY.md", lambda s: s.replace("coordinated disclosure", "responsible reporting"))
        self.assertFails("repo", "[R9.4]")

    def test_R9_6_tamper_proof_claim_is_caught(self):
        self.edit("index.html", lambda s: s.replace("</main>", '<p class="en">The policy file is tamper-proof.</p></main>', 1))
        self.assertFails("honesty", "tamper-proof")

    def test_R9_7_mapping_without_disclaimer_is_caught(self):
        self.edit("index.html", lambda s: s.replace("author's interpretation", "official mapping"))
        self.assertFails("content", "[R9.7]")

    def test_R9_8_missing_companion_repo_link_is_caught(self):
        self.edit("index.html", lambda s: s.replace("https://github.com/timwukp/kiro-fsi-best-practices", "https://github.com/timwukp"))
        self.assertFails("content", "[R9.8]")

    def test_R10_2_missing_delivery_warning_is_caught(self):
        self.edit("index.html", lambda s: s.replace("does not notify", "may notify"))
        self.assertFails("content", "[R10.2]")

    def test_R10_3_roi_claim_is_caught(self):
        self.edit("index.html", lambda s: s.replace("</main>", '<p class="en">This dashboard proves ROI.</p></main>', 1))
        self.assertFails("honesty", "proves roi")

    def test_R10_5_missing_dashboard_link_is_caught(self):
        self.edit("index.html", lambda s: s.replace("https://github.com/timwukp/kiro-telemetry-dashboard", "https://github.com/timwukp"))
        self.assertFails("content", "[R10.5]")

    def test_R11_1_chapter_order_is_caught(self):
        self.edit("index.html", lambda s: s.replace('data-topic="gov-decide"', 'data-topic="gov-later"', 1))
        self.assertFails("structure", "[R11.1]")

    def test_R11_3_stale_chapter_number_is_caught(self):
        self.edit("index.html", lambda s: s.replace('<a href="#ch3">Chapter 3</a>', '<a href="#ch3">Chapter 2</a>', 1))
        self.assertFails("content", "[R11.3]")


if __name__ == "__main__":
    unittest.main()
