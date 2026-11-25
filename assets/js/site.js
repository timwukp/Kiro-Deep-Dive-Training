/* Kiro Deep Dive — navigation, language and view mode. No network access. */
(function () {
  "use strict";
  var root = document.documentElement;
  root.classList.add("js");
  var slides = Array.prototype.slice.call(document.querySelectorAll("main section.slide"));
  if (!slides.length) { return; }
  var idx = 0;
  var $ = function (id) { return document.getElementById(id); };
  var store = {
    get: function (k) { try { return window.localStorage.getItem(k); } catch (e) { return null; } },
    set: function (k, v) { try { window.localStorage.setItem(k, v); } catch (e) { /* private mode */ } }
  };
  var params = new URLSearchParams(window.location.search);
  var navLinks = Array.prototype.slice.call(document.querySelectorAll("#chapter-nav a[href^='#']"));
  var drawer = $("chapter-nav");

  function lang() { return root.getAttribute("data-lang") === "zh" ? "zh" : "en"; }
  function setLang(l) {
    l = l === "zh" ? "zh" : "en";
    root.setAttribute("data-lang", l);
    root.setAttribute("lang", l === "zh" ? "zh-Hant" : "en");
    store.set("kdd-lang", l);
    $("lang-toggle").setAttribute("aria-pressed", String(l === "zh"));
    label();
  }
  function presenting() { return root.classList.contains("present"); }
  function setMode(m) {
    var pres = m === "present";
    root.classList.toggle("present", pres);
    store.set("kdd-mode", pres ? "present" : "reading");
    $("mode-toggle").setAttribute("aria-pressed", String(!pres));
    slides.forEach(function (s, j) {
      if (pres && j !== idx) { s.setAttribute("aria-hidden", "true"); } else { s.removeAttribute("aria-hidden"); }
    });
    if (pres) { show(idx, false); } else { slides[idx].scrollIntoView({ block: "start" }); }
  }
  function textOf(el) {
    if (!el) { return ""; }
    var span = el.querySelector("." + lang());
    return (span || el).textContent.trim();
  }
  function label() {
    var s = slides[idx];
    var ch = document.querySelector('section.chapter[data-chapter="' + s.getAttribute("data-chapter") + '"] h2');
    var here = textOf(s.querySelector("h1, h2"));
    $("where").textContent = (ch && ch !== s.querySelector("h2") ? textOf(ch) + " · " : "") + here;
    $("counter").textContent = (idx + 1) + " / " + slides.length;
    $("progress").style.width = ((idx + 1) / slides.length * 100) + "%";
    navLinks.forEach(function (a) {
      a.setAttribute("aria-current", String(a.getAttribute("href") === "#" + s.id));
    });
  }
  function show(i, updateHash) {
    idx = Math.max(0, Math.min(slides.length - 1, i));
    slides.forEach(function (s, j) {
      var on = j === idx;
      s.classList.toggle("active", on);
      if (presenting() && !on) { s.setAttribute("aria-hidden", "true"); } else { s.removeAttribute("aria-hidden"); }
    });
    if (updateHash !== false && window.history && window.history.replaceState) {
      window.history.replaceState(null, "", "#" + slides[idx].id);
    }
    if (presenting()) { window.scrollTo(0, 0); }
    label();
  }
  function fromHash() {
    var id = decodeURIComponent(window.location.hash.slice(1));
    if (!id) { return; }
    var el = document.getElementById(id);
    var s = el && el.closest ? el.closest("section.slide") : null;
    var j = slides.indexOf(s);
    if (j >= 0) {
      idx = j;
      if (presenting()) { show(j, false); } else { label(); }
    }
  }
  function openNav(open) {
    drawer.classList.toggle("open", open);
    $("nav-toggle").setAttribute("aria-expanded", String(open));
    if (open) { var cur = drawer.querySelector('a[aria-current="true"]') || drawer.querySelector("a"); if (cur) { cur.focus(); } }
  }

  // reading mode: keep the counter in step with scrolling
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      if (presenting()) { return; }
      entries.forEach(function (e) {
        if (e.isIntersecting) { idx = slides.indexOf(e.target); label(); }
      });
    }, { rootMargin: "-45% 0px -50% 0px" });
    slides.forEach(function (s) { io.observe(s); });
  }

  $("prev").addEventListener("click", function () { if (presenting()) { show(idx - 1); } else { slides[Math.max(0, idx - 1)].scrollIntoView(); } });
  $("next").addEventListener("click", function () { if (presenting()) { show(idx + 1); } else { slides[Math.min(slides.length - 1, idx + 1)].scrollIntoView(); } });
  $("lang-toggle").addEventListener("click", function () { setLang(lang() === "en" ? "zh" : "en"); });
  $("mode-toggle").addEventListener("click", function () { setMode(presenting() ? "reading" : "present"); });
  $("nav-toggle").addEventListener("click", function () { openNav(!drawer.classList.contains("open")); });
  $("scrim").addEventListener("click", function () { openNav(false); });
  navLinks.forEach(function (a) { a.addEventListener("click", function () { openNav(false); }); });
  window.addEventListener("hashchange", fromHash);

  // a click anywhere on a card opens or closes its deep dive
  document.addEventListener("click", function (e) {
    var card = e.target.closest ? e.target.closest(".card.click") : null;
    if (!card || e.target.closest("a, summary, pre, details.deep[open] > *:not(summary)")) { return; }
    var d = card.querySelector("details.deep");
    if (d) { d.open = !d.open; }
  });

  document.addEventListener("keydown", function (e) {
    if (e.metaKey || e.ctrlKey || e.altKey) { return; }
    var t = e.target;
    if (t && (t.isContentEditable || /^(INPUT|TEXTAREA|SELECT)$/.test(t.tagName))) { return; }
    var k = e.key;
    if (k === "m" || k === "M") { e.preventDefault(); openNav(!drawer.classList.contains("open")); return; }
    if (k === "l" || k === "L") { setLang(lang() === "en" ? "zh" : "en"); return; }
    if (k === "r" || k === "R") { setMode(presenting() ? "reading" : "present"); return; }
    if (k === "Escape") { openNav(false); return; }
    if (!presenting() || drawer.classList.contains("open")) { return; }
    if (k === " " && t && t.closest && t.closest("button, summary, a")) { return; }
    if (k === "ArrowRight" || k === "PageDown" || (k === " " && !e.shiftKey)) { e.preventDefault(); show(idx + 1); }
    else if (k === "ArrowLeft" || k === "PageUp" || (k === " " && e.shiftKey)) { e.preventDefault(); show(idx - 1); }
    else if (k === "Home") { e.preventDefault(); show(0); }
    else if (k === "End") { e.preventDefault(); show(slides.length - 1); }
  });

  // swipe left / right on touch screens (present mode only)
  var x0 = null, y0 = null;
  document.addEventListener("touchstart", function (e) { x0 = e.touches[0].clientX; y0 = e.touches[0].clientY; }, { passive: true });
  document.addEventListener("touchend", function (e) {
    if (x0 === null || !presenting()) { return; }
    var dx = e.changedTouches[0].clientX - x0, dy = e.changedTouches[0].clientY - y0;
    if (Math.abs(dx) > 60 && Math.abs(dx) > Math.abs(dy) * 1.5) { show(idx + (dx < 0 ? 1 : -1)); }
    x0 = null;
  }, { passive: true });

  setLang(params.get("lang") || store.get("kdd-lang") || "en");
  var m = params.get("mode") || store.get("kdd-mode") || (window.innerWidth < 760 ? "reading" : "present");
  root.classList.toggle("present", m === "present");
  $("mode-toggle").setAttribute("aria-pressed", String(m !== "present"));
  fromHash();
  if (presenting()) { show(idx, false); } else { label(); }
}());
