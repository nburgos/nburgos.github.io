(function () {
  "use strict";

  var root = document.documentElement;
  var KEY = "theme";

  function currentTheme() {
    return root.getAttribute("data-theme") === "dark" ? "dark" : "light";
  }

  // Theme toggle
  var toggle = document.querySelector(".theme-toggle");
  if (toggle) {
    toggle.addEventListener("click", function () {
      var next = currentTheme() === "dark" ? "light" : "dark";
      root.setAttribute("data-theme", next);
      try {
        localStorage.setItem(KEY, next);
      } catch (e) {
        /* storage unavailable — theme resets per page, still functional */
      }
    });
  }

  // Mobile menu toggle
  var navToggle = document.querySelector(".nav-toggle");
  var navList = document.getElementById("site-nav-list");
  if (navToggle && navList) {
    navToggle.addEventListener("click", function () {
      var open = navList.classList.toggle("open");
      navToggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  // Follow OS theme changes unless the user made an explicit choice
  var media = window.matchMedia("(prefers-color-scheme: dark)");
  var stored = null;
  try {
    stored = localStorage.getItem(KEY);
  } catch (e) {
    /* ignore */
  }
  if (!stored) {
    var update = function (e) {
      root.setAttribute("data-theme", e.matches ? "dark" : "light");
    };
    if (media.addEventListener) {
      media.addEventListener("change", update);
    } else if (media.addListener) {
      media.addListener(update);
    }
  }
  // Publication year filters (publications page)
  var groups = document.querySelectorAll("details.pub-group");
  groups.forEach(function (group) {
    var buttons = group.querySelectorAll(".year-filter");
    var count = group.querySelector(".pub-count");
    var totalLabel = null;

    if (count) {
      totalLabel = count.textContent;
    }

    buttons.forEach(function (btn) {
      btn.addEventListener("click", function () {
        var year = btn.getAttribute("data-year");
        buttons.forEach(function (b) {
          b.classList.toggle("is-active", b === btn);
          b.setAttribute("aria-pressed", b === btn ? "true" : "false");
        });

        var shown = 0;
        group.querySelectorAll(".pub").forEach(function (pub) {
          var match = year === "all" || pub.getAttribute("data-year") === year;
          pub.hidden = !match;
          if (match) shown++;
        });

        if (count && totalLabel) {
          count.textContent =
            year === "all" ? totalLabel : shown + " document" + (shown === 1 ? "" : "s");
        }
      });
    });
  });
})();
