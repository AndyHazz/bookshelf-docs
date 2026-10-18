// The shelf menu's search cell: put the cursor in the header's search field.
// Delegated from the document, so it keeps working across instant navigation.
document.addEventListener("click", function (e) {
  if (!e.target.closest || !e.target.closest(".bs-tab-search .md-tabs__link")) return;
  var toggle = document.getElementById("__search");
  var input = document.querySelector(".md-search__input");
  if (toggle && !toggle.checked) {
    toggle.checked = true;
    toggle.dispatchEvent(new Event("change"));
  }
  if (input) {
    input.focus();
    input.select();
  }
});

// The shelf menu's light/dark cell works the header's own palette switch
// (hidden where the shelf menu shows), and wears that switch's current icon.
function bsThemeLabel() {
  return document.querySelector("[data-md-component=palette] label:not([hidden])");
}
var BS_MOON = '<svg class="bs-ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 14.5A8.5 8.5 0 1 1 9.5 4a6.6 6.6 0 0 0 10.5 10.5z"/></svg>';
var BS_SUN = '<svg class="bs-ico" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2.5v2M12 19.5v2M4.6 4.6l1.4 1.4M18 18l1.4 1.4M2.5 12h2M19.5 12h2M4.6 19.4 6 18M18 6l1.4-1.4"/></svg>';
function bsSyncTheme() {
  // the icon shows what a tap switches to, as Material's own toggle does
  var cell = document.querySelector(".bs-tab-theme .md-tabs__link");
  var label = bsThemeLabel();
  if (!cell) return;
  var dark = document.body.getAttribute("data-md-color-scheme") === "slate";
  cell.innerHTML = dark ? BS_SUN : BS_MOON;
  var t = (label && label.title) || (dark ? "Switch to light mode" : "Switch to dark mode");
  cell.title = t;
  cell.setAttribute("aria-label", t);
}
document.addEventListener("click", function (e) {
  if (!e.target.closest || !e.target.closest(".bs-tab-theme .md-tabs__link")) return;
  var label = bsThemeLabel();
  if (label) label.click();
  setTimeout(bsSyncTheme, 30);
});
if (window.document$ && window.document$.subscribe) window.document$.subscribe(bsSyncTheme);
else document.addEventListener("DOMContentLoaded", bsSyncTheme);
