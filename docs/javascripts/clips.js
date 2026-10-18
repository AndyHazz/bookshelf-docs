// Tutorial clips.
//
// - One clip plays at a time: the one most in view. The rest rest on their
//   poster with a play button, so a page of clips isn't a wall of motion.
// - Every clip has a visible play/pause button (WCAG 2.2.2 Pause, Stop, Hide),
//   and the header has a site-wide "autoplay videos" switch, remembered in
//   this browser. It starts off for readers who ask for reduced motion.
// - Clicking a clip, still or screenshot opens it large in a lightbox, since
//   the text on an e-reader screen is small at the size it sits in the page.
(function () {
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)");
  var KEY = "bs-autoplay";
  var PLAY = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg>';
  var PAUSE = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 5h4v14H6zm8 0h4v14h-4z"/></svg>';
  var ZOOM = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M15.5 14h-.79l-.28-.27A6.47 6.47 0 0 0 16 9.5 6.5 6.5 0 1 0 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14m.5-7H9v2H7v1h2v2h1v-2h2V9h-2z"/></svg>';
  var CLOSE = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M19 6.41 17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"/></svg>';
  var AUTO_ON = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M10 16.5l6-4.5-6-4.5zM12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20m0 18a8 8 0 1 1 0-16 8 8 0 0 1 0 16"/></svg>';
  var AUTO_OFF = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 16h2V8H9zm3-14a10 10 0 1 0 0 20 10 10 0 0 0 0-20m0 18a8 8 0 1 1 0-16 8 8 0 0 1 0 16m1-4h2V8h-2z"/></svg>';

  function readAuto() {
    var v = null;
    try { v = window.localStorage.getItem(KEY); } catch (e) {}
    if (v === "on") return true;
    if (v === "off") return false;
    return !reduce.matches;
  }
  function writeAuto(on) {
    try { window.localStorage.setItem(KEY, on ? "on" : "off"); } catch (e) {}
  }
  var autoplay = readAuto();

  function button(cls, label, svg) {
    var b = document.createElement("button");
    b.className = cls;
    b.type = "button";
    b.setAttribute("aria-label", label);
    b.innerHTML = svg;
    return b;
  }

  // ---- the clips on this page ----
  var clips = [];        // { fig, v, btn, ratio }
  var io = null;
  var held = false;      // the reader paused a clip: nothing else starts by itself on this page

  function setButton(c, playing) {
    c.btn.innerHTML = playing ? PAUSE : PLAY;
    c.btn.setAttribute("aria-label", playing ? "Pause clip" : "Play clip");
    c.fig.classList.toggle("paused", !playing);
  }
  function play(c) {
    clips.forEach(function (o) { if (o !== c && !o.v.paused) { o.v.pause(); setButton(o, false); } });
    if (c.v.preload === "none") c.v.preload = "auto";
    var p = c.v.play();
    if (p && p.catch) p.catch(function () {});
    setButton(c, true);
  }
  function pause(c) {
    c.v.pause();
    setButton(c, false);
  }

  // The clip most in view plays; everything else rests.
  function pick() {
    if (document.querySelector(".bs-lightbox")) return;
    // A clip the reader started wins while it is on screen; otherwise, with
    // autoplay on, the one most in view.
    var active = clips.filter(function (c) { return c.fig.dataset.user === "play" && c.ratio > 0; })[0] || null;
    if (!active && autoplay && !held) {
      clips.forEach(function (c) {
        if (c.ratio >= 0.5 && c.fig.dataset.user !== "pause" && (!active || c.ratio > active.ratio)) active = c;
      });
    }
    clips.forEach(function (c) {
      if (c === active) { if (c.v.paused) play(c); }
      else if (!c.v.paused) pause(c);
    });
  }

  function setupClips() {
    clips = [];
    held = false;
    if (io) io.disconnect();
    io = "IntersectionObserver" in window
      ? new IntersectionObserver(function (entries) {
          entries.forEach(function (e) {
            var c = clips.filter(function (o) { return o.fig === e.target; })[0];
            if (c) {
              c.ratio = e.isIntersecting ? e.intersectionRatio : 0;
              if (!e.isIntersecting && c.fig.dataset.user === "play") delete c.fig.dataset.user;
            }
          });
          pick();
        }, { threshold: [0, 0.25, 0.5, 0.75, 1] })
      : null;

    document.querySelectorAll("figure.clip").forEach(function (fig) {
      if (fig.classList.contains("missing")) return;
      var bezel = fig.querySelector(".bezel");
      var v = fig.querySelector("video");
      var img = fig.querySelector("img");
      if (!bezel.querySelector(".clip-zoom")) bezel.appendChild(button("clip-zoom", "View larger", ZOOM));
      var zoom = bezel.querySelector(".clip-zoom");
      if (v) {
        v.muted = true;
        v.playsInline = true;
        v.loop = true;
        var btn = bezel.querySelector(".clip-ctl") || bezel.appendChild(button("clip-ctl", "Play clip", PLAY));
        var c = { fig: fig, v: v, btn: btn, ratio: 0 };
        clips.push(c);
        setButton(c, false);
        btn.onclick = function () {
          if (v.paused) { fig.dataset.user = "play"; play(c); }
          else { fig.dataset.user = "pause"; held = true; pause(c); }
        };
        zoom.onclick = function () { openVideo(c); };
        v.onclick = function () { openVideo(c); };
        if (io) io.observe(fig);
      } else if (img) {
        zoom.onclick = function () { openImage(img, true); };
        img.onclick = function () { openImage(img, true); };
      }
    });

    document.querySelectorAll("figure.shot").forEach(function (fig) {
      var img = fig.querySelector("img");
      if (!img || fig.dataset.ready) return;
      fig.dataset.ready = "1";
      img.setAttribute("tabindex", "0");
      img.setAttribute("role", "button");
      img.setAttribute("aria-label", (img.alt || "Screenshot") + ": view larger");
      img.addEventListener("click", function () { openImage(img, false); });
      img.addEventListener("keydown", function (e) {
        if (e.key === "Enter" || e.key === " ") { e.preventDefault(); openImage(img, false); }
      });
    });
  }

  // ---- the header switch ----
  function setupSwitch() {
    var bar = document.querySelector(".md-header__inner");
    if (!bar || bar.querySelector(".bs-autoplay")) return syncSwitch();
    var b = button("md-header__button md-icon bs-autoplay", "", AUTO_ON);
    var search = bar.querySelector(".md-search") || bar.querySelector("label[for='__search']");
    bar.insertBefore(b, search ? search : null);
    b.addEventListener("click", function () {
      autoplay = !autoplay;
      writeAuto(autoplay);
      syncSwitch();
      if (!autoplay) clips.forEach(function (c) { if (!c.v.paused) pause(c); });
      else pick();
    });
    syncSwitch();
  }
  function syncSwitch() {
    var b = document.querySelector(".bs-autoplay");
    if (!b) return;
    b.innerHTML = autoplay ? AUTO_ON : AUTO_OFF;
    b.setAttribute("aria-pressed", autoplay ? "true" : "false");
    b.setAttribute("aria-label", "Play videos automatically");
    b.title = autoplay ? "Videos play automatically: on" : "Videos play automatically: off";
  }

  // ---- lightbox ----
  function openBox(content, framed, onClose, extra) {
    var back = document.activeElement;
    var box = document.createElement("div");
    box.className = "bs-lightbox";
    box.setAttribute("role", "dialog");
    box.setAttribute("aria-modal", "true");
    box.setAttribute("aria-label", content.getAttribute("aria-label") || content.alt || "Enlarged view");
    var holder = document.createElement("div");
    holder.className = framed ? "lb-bezel" : "lb-plain";
    holder.appendChild(content);
    var close = button("lb-close", "Close", CLOSE);
    box.appendChild(holder);
    var stops = (extra || []).concat([close]);   // the dialog's buttons, in Tab order
    stops.forEach(function (b) { box.appendChild(b); });
    function shut() {
      document.removeEventListener("keydown", onKey);
      box.remove();
      document.documentElement.classList.remove("bs-lightbox-open");
      if (onClose) onClose();
      if (back && back.focus) back.focus();
    }
    function onKey(e) {
      if (e.key === "Escape") shut();
      else if (e.key === "Tab") {   // keep focus in the dialog, cycling its buttons
        e.preventDefault();
        var i = stops.indexOf(document.activeElement);
        var n = stops.length;
        stops[i < 0 ? 0 : (i + (e.shiftKey ? n - 1 : 1)) % n].focus();
      }
    }
    box.addEventListener("click", function (e) { if (e.target === box) shut(); });
    close.addEventListener("click", shut);
    document.addEventListener("keydown", onKey);
    document.documentElement.classList.add("bs-lightbox-open");
    document.body.appendChild(box);
    close.focus();
  }

  function openVideo(c) {
    var v = c.v;
    var wasPlaying = !v.paused;
    if (wasPlaying) pause(c);
    var big = document.createElement("video");
    big.src = v.currentSrc || v.src;
    big.poster = v.poster;
    big.muted = true;
    big.loop = true;
    big.playsInline = true;
    big.setAttribute("aria-label", v.getAttribute("aria-label") || "Clip");
    // No browser controls: they sit over the caption strip, which is the
    // text people zoom in to read. A click pauses and resumes instead, and a
    // play/pause button beside Close does the same from the keyboard.
    big.title = "Click to pause or play";
    var toggle = button("lb-play", "Play clip", PLAY);
    function syncToggle() {
      toggle.innerHTML = big.paused ? PLAY : PAUSE;
      toggle.setAttribute("aria-label", big.paused ? "Play clip" : "Pause clip");
    }
    function flip() {
      if (big.paused) { var p = big.play(); if (p && p.catch) p.catch(function () {}); }
      else big.pause();
    }
    big.addEventListener("click", flip);
    toggle.addEventListener("click", flip);
    big.addEventListener("play", syncToggle);
    big.addEventListener("pause", syncToggle);
    big.addEventListener("loadedmetadata", function () {
      try { big.currentTime = v.currentTime; } catch (e) {}
      if (autoplay || wasPlaying) { var p = big.play(); if (p && p.catch) p.catch(function () {}); }
    });
    openBox(big, true, function () {
      try { v.currentTime = big.currentTime || v.currentTime; } catch (e) {}
      big.pause();
      pick();
    }, [toggle]);
  }

  function openImage(img, framed) {
    var big = document.createElement("img");
    big.src = img.currentSrc || img.src;
    big.alt = img.alt;
    openBox(big, framed, null);
  }

  // ---- small fixes to the theme's own markup ----
  // A table or code block that scrolls sideways (most of them on a phone) has
  // to take keyboard focus, or its hidden part can't be reached without a
  // mouse (WCAG 2.1.1). The search dialog and the page-load bar need names.
  function labelTheme() {
    var search = document.querySelector(".md-search[role='dialog']");
    if (search && !search.hasAttribute("aria-label")) search.setAttribute("aria-label", "Search");
    var bar = document.querySelector(".md-progress");
    if (bar && !bar.hasAttribute("aria-label")) bar.setAttribute("aria-label", "Loading the page");
    drawerButton();
  }

  // On narrower screens the site menu is a drawer opened by a <label> in the
  // header, which the keyboard can't reach. Make it a button: Enter or Space
  // opens the drawer and moves into it; Escape closes it and comes back.
  function drawerButton() {
    var box = document.getElementById("__drawer");
    var lab = document.querySelector(".md-header label[for='__drawer']");
    if (!box || !lab || lab.dataset.bsButton) return;
    lab.dataset.bsButton = "1";
    lab.setAttribute("role", "button");
    lab.setAttribute("tabindex", "0");
    lab.setAttribute("aria-label", "Site menu");
    var viaKey = false;
    function sync() {
      lab.setAttribute("aria-expanded", box.checked ? "true" : "false");
      // the label only stands in for the menu while the drawer exists
      var shown = getComputedStyle(lab).display !== "none";
      lab.setAttribute("tabindex", shown ? "0" : "-1");
      if (box.checked && viaKey) {
        // once it has slid in, focus the first item actually showing (the
        // drawer opens on the current section, over the levels above it)
        setTimeout(function () {
          var items = document.querySelectorAll(".md-sidebar--primary a[href], .md-sidebar--primary label[tabindex]");
          for (var i = 0; i < items.length; i++) {
            var r = items[i].getBoundingClientRect();
            if (!r.width || !r.height) continue;
            var hit = document.elementFromPoint(r.left + r.width / 2, r.top + r.height / 2);
            if (hit && (hit === items[i] || items[i].contains(hit))) { items[i].focus(); break; }
          }
        }, 300);
      }
      viaKey = false;
    }
    // Material already clicks a focused label on Enter; Space is ours
    lab.addEventListener("keydown", function (e) {
      if (e.key === "Enter") viaKey = true;
      else if (e.key === " ") { e.preventDefault(); viaKey = true; lab.click(); }
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && box.checked && getComputedStyle(lab).display !== "none") {
        lab.click();
        lab.focus();
      }
    });
    box.addEventListener("change", sync);
    window.addEventListener("resize", sync);
    sync();
  }
  function markScrollers() {
    document.querySelectorAll(".md-typeset__scrollwrap, .md-typeset pre > code").forEach(function (el) {
      var scrolls = el.scrollWidth > el.clientWidth;
      if (scrolls && !el.hasAttribute("tabindex")) {
        el.setAttribute("tabindex", "0");
        el.dataset.bsScroll = "1";
        if (el.classList.contains("md-typeset__scrollwrap")) {
          el.setAttribute("role", "region");
          el.setAttribute("aria-label", "Table, scrolls sideways");
        }
      } else if (!scrolls && el.dataset.bsScroll) {
        el.removeAttribute("tabindex");
        el.removeAttribute("role");
        el.removeAttribute("aria-label");
        delete el.dataset.bsScroll;
      }
    });
  }
  var resizeTimer = null;
  window.addEventListener("resize", function () {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(markScrollers, 200);
  });
  // a block inside a closed <details> or an inactive tab only scrolls once shown
  document.addEventListener("toggle", function () { markScrollers(); }, true);
  document.addEventListener("change", function (e) {
    if (e.target && e.target.closest && e.target.closest(".tabbed-set")) markScrollers();
  });

  function setup() { setupSwitch(); setupClips(); labelTheme(); markScrollers(); }
  if (window.document$ && window.document$.subscribe) window.document$.subscribe(setup);
  else document.addEventListener("DOMContentLoaded", setup);
})();
