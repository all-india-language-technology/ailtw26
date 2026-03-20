/* ============================================================
   AILT 2026 · Prompt Engineering Module — script.js
   Shared interactivity: prompt reveals, lane tabs, animations
   Facilitator control via BroadcastChannel API
   ============================================================ */

(function () {
  'use strict';

  /* ── 1. PROMPT REVEAL BUTTONS ──────────────────────────── */
  document.querySelectorAll('.reveal-btn').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var targetId = btn.getAttribute('data-target');
      var target   = document.getElementById(targetId);
      if (!target) return;

      var isOpen = target.classList.contains('open');

      if (isOpen) {
        target.classList.remove('open');
        btn.classList.remove('open');
        btn.querySelector('.btn-text').textContent = btn.getAttribute('data-open-text') || 'Show strong prompt';
      } else {
        target.classList.add('open');
        btn.classList.add('open');
        btn.querySelector('.btn-text').textContent = btn.getAttribute('data-close-text') || 'Hide prompt';
        // Smooth scroll into view
        setTimeout(function () {
          target.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        }, 50);
      }
    });
  });

  /* ── 2. LANE TOGGLE TABS ────────────────────────────────── */
  document.querySelectorAll('.lane-group').forEach(function (group) {
    var buttons  = group.querySelectorAll('.lane-btn');
    var contents = group.querySelectorAll('.lane-content');

    // Activate first lane by default
    if (buttons.length > 0) {
      buttons[0].classList.add('active');
    }
    if (contents.length > 0) {
      contents[0].classList.add('active');
    }

    buttons.forEach(function (btn) {
      btn.addEventListener('click', function () {
        var targetLane = btn.getAttribute('data-lane');

        buttons.forEach(function (b) { b.classList.remove('active'); });
        contents.forEach(function (c) { c.classList.remove('active'); });

        btn.classList.add('active');
        var targetContent = group.querySelector('.lane-content[data-lane="' + targetLane + '"]');
        if (targetContent) targetContent.classList.add('active');
      });
    });
  });

  /* ── 3. PHASE BAR ACTIVE STATE (scroll spy) ─────────────── */
  var sections = document.querySelectorAll('.c-section[id]');
  var pips     = document.querySelectorAll('.phase-pip');

  if (sections.length && pips.length) {
    var sectionObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          var id = entry.target.id;
          pips.forEach(function (pip) {
            var pipSection = pip.getAttribute('data-section');
            pip.classList.toggle('inactive', pipSection !== id);
          });
        }
      });
    }, { rootMargin: '-35% 0px -55% 0px' });

    sections.forEach(function (s) { sectionObserver.observe(s); });
  }

  /* ── 4. STAGGER CARD ANIMATIONS (must run before observer setup) ── */
  document.querySelectorAll('.card-grid').forEach(function (grid) {
    var cards = grid.querySelectorAll('.card');
    cards.forEach(function (card, i) {
      card.style.transitionDelay = (i * 0.07) + 's';
      card.classList.add('fade-up');
    });
  });

  /* ── 5. SCROLL-IN ANIMATIONS (queries .fade-up after cards are tagged) ── */
  var animEls = document.querySelectorAll('.fade-up');
  if (animEls.length) {
    var fadeObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          fadeObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.08 });

    animEls.forEach(function (el) { fadeObserver.observe(el); });
  }

  /* ── 6. PRINT COMMITMENT BUTTONS ─────────────────────────── */
  document.querySelectorAll('.btn-print').forEach(function (btn) {
    btn.addEventListener('click', function () {
      window.print();
    });
  });

  /* ── 7. MARK CURRENT CHAPTER IN NAV ─────────────────────── */
  var currentPath = window.location.pathname.split('/').pop();
  document.querySelectorAll('.nav-link').forEach(function (link) {
    var href = link.getAttribute('href');
    if (href && (href === currentPath || href.split('/').pop() === currentPath)) {
      link.classList.add('active');
    }
  });

  /* ── 8. SMOOTH NAV SCROLL WITHIN CHAPTER ─────────────────── */
  document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
    anchor.addEventListener('click', function (e) {
      var target = document.querySelector(anchor.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });

  /* ── 9. BROADCAST CHANNEL — FACILITATOR CONTROL ──────────── */
  // Expose a global trigger for reveals (used by facilitator and internal)
  window.triggerReveal = function (targetId) {
    var target = document.getElementById(targetId);
    if (!target) return;
    var btn = document.querySelector('.reveal-btn[data-target="' + targetId + '"]');
    var isOpen = target.classList.contains('open');
    if (!isOpen) {
      target.classList.add('open');
      if (btn) {
        btn.classList.add('open');
        var textEl = btn.querySelector('.btn-text');
        if (textEl) textEl.textContent = btn.getAttribute('data-close-text') || 'Hide';
      }
      setTimeout(function () {
        target.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }, 60);
    }
  };

  window.triggerLane = function (laneNum) {
    document.querySelectorAll('.lane-group').forEach(function (group) {
      var buttons  = group.querySelectorAll('.lane-btn');
      var contents = group.querySelectorAll('.lane-content');
      buttons.forEach(function (b) { b.classList.remove('active'); });
      contents.forEach(function (c) { c.classList.remove('active'); });
      var btn = group.querySelector('.lane-btn[data-lane="' + laneNum + '"]');
      var content = group.querySelector('.lane-content[data-lane="' + laneNum + '"]');
      if (btn) btn.classList.add('active');
      if (content) content.classList.add('active');
    });
  };

  window.scrollToSection = function (sectionId) {
    var el = document.getElementById(sectionId);
    if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
  };

  if (window.BroadcastChannel) {
    var ch = new BroadcastChannel('ailt-2026-facilitator');

    ch.onmessage = function (e) {
      var msg = e.data;
      if (!msg || !msg.action) return;

      switch (msg.action) {
        case 'scroll':
          if (msg.section) window.scrollToSection(msg.section);
          break;
        case 'reveal':
          if (msg.target) window.triggerReveal(msg.target);
          break;
        case 'lane':
          if (msg.lane) window.triggerLane(msg.lane);
          break;
        case 'navigate':
          if (msg.url) window.location.href = msg.url;
          break;
        case 'ping':
          // Reply with current page info
          ch.postMessage({
            action: 'pong',
            page: currentPath,
            title: document.title
          });
          break;
        case 'opendetails':
          // Open a named <details> accordion
          if (msg.target) {
            var det = document.querySelector('details[data-fm="' + msg.target + '"]');
            if (det) {
              det.open = true;
              det.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
            }
          }
          break;
      }
    };

    // Announce presence on load
    ch.postMessage({
      action: 'pong',
      page: currentPath,
      title: document.title
    });
  }

})();
