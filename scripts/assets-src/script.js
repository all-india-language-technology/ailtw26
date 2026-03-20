/* ============================================================
   AILT 2026 · Prompt Engineering for Bible Translators
   Shared site script — merged from 004 module + site features
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
    if (buttons.length > 0) buttons[0].classList.add('active');
    if (contents.length > 0) contents[0].classList.add('active');
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

  /* ── 3. PHASE BAR ACTIVE STATE ──────────────────────────── */
  var sections = document.querySelectorAll('.c-section[id]');
  var pips     = document.querySelectorAll('.phase-pip');
  if (sections.length && pips.length) {
    var sectionObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          var id = entry.target.id;
          pips.forEach(function (pip) {
            pip.classList.toggle('inactive', pip.getAttribute('data-section') !== id);
          });
        }
      });
    }, { rootMargin: '-35% 0px -55% 0px' });
    sections.forEach(function (s) { sectionObserver.observe(s); });
  }

  /* ── 4. CARD STAGGER ANIMATIONS ─────────────────────────── */
  document.querySelectorAll('.card-grid').forEach(function (grid) {
    grid.querySelectorAll('.card').forEach(function (card, i) {
      card.style.transitionDelay = (i * 0.07) + 's';
      card.classList.add('fade-up');
    });
  });

  /* ── 5. SCROLL-IN ANIMATIONS ────────────────────────────── */
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
    btn.addEventListener('click', function () { window.print(); });
  });

  /* ── 7. MARK CURRENT CHAPTER IN MODULE SUB-NAV ───────────── */
  var currentPath = window.location.pathname.split('/').pop();
  document.querySelectorAll('.nav-link').forEach(function (link) {
    var href = link.getAttribute('href');
    if (href && (href === currentPath || href.split('/').pop() === currentPath)) {
      link.classList.add('active');
    }
  });

  /* ── 8. SMOOTH ANCHOR SCROLL ────────────────────────────── */
  document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
    anchor.addEventListener('click', function (e) {
      var target = document.querySelector(anchor.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });

  /* ── 9. HAMBURGER MENU TOGGLE ─────────────────────────────── */
  var hamburger = document.getElementById('hamburger');
  var navLinks  = document.getElementById('nav-links');
  if (hamburger && navLinks) {
    hamburger.addEventListener('click', function () {
      var isOpen = hamburger.classList.toggle('open');
      navLinks.classList.toggle('open');
      hamburger.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });
    // Close menu when a link is clicked (mobile)
    navLinks.querySelectorAll('.shell-nav-link').forEach(function (link) {
      link.addEventListener('click', function () {
        hamburger.classList.remove('open');
        navLinks.classList.remove('open');
        hamburger.setAttribute('aria-expanded', 'false');
      });
    });
  }

  /* ── 10. SCROLL PROGRESS BAR ──────────────────────────────── */
  var progressBar = document.getElementById('scroll-progress');
  if (progressBar) {
    window.addEventListener('scroll', function () {
      var scrollTop = window.scrollY;
      var docHeight = document.documentElement.scrollHeight - window.innerHeight;
      var progress  = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
      progressBar.style.width = progress + '%';
    }, { passive: true });
  }

  /* ── 11. BACK TO TOP BUTTON ──────────────────────────────── */
  var backToTop = document.getElementById('back-to-top');
  if (backToTop) {
    window.addEventListener('scroll', function () {
      if (window.scrollY > 400) {
        backToTop.classList.add('visible');
      } else {
        backToTop.classList.remove('visible');
      }
    }, { passive: true });
    backToTop.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  /* ── 12. PRESENTATION MODE NAV LINK ─────────────────────── */
  var presentBtn = document.getElementById('nav-present');
  if (presentBtn) {
    presentBtn.addEventListener('click', function (e) {
      e.preventDefault();
      var url = new URL(window.location.href);
      if (url.searchParams.has('present')) {
        url.searchParams.delete('present');
      } else {
        url.searchParams.set('present', '1');
      }
      window.location.href = url.toString();
    });
  }

  /* ── 13. PRESENTATION MODE BOOTSTRAP ────────────────────── */
  if (new URLSearchParams(window.location.search).has('present')) {
    document.body.classList.add('present-mode');
    initPresentation();
    // Update present button label
    if (presentBtn) presentBtn.textContent = '✕ Exit';
  }

  /* ── 14. BROADCAST CHANNEL — FACILITATOR CONTROL ─────────── */
  window.triggerReveal = function (targetId) {
    var target = document.getElementById(targetId);
    if (!target) return;
    var btn = document.querySelector('.reveal-btn[data-target="' + targetId + '"]');
    if (!target.classList.contains('open')) {
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
      var btn     = group.querySelector('.lane-btn[data-lane="' + laneNum + '"]');
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
        case 'scroll':   if (msg.section) window.scrollToSection(msg.section); break;
        case 'reveal':   if (msg.target)  window.triggerReveal(msg.target); break;
        case 'lane':     if (msg.lane)    window.triggerLane(msg.lane); break;
        case 'navigate': if (msg.url)     window.location.href = msg.url; break;
        case 'ping':
          ch.postMessage({ action: 'pong', page: currentPath, title: document.title });
          break;
      }
    };
  }

  /* ════════════════════════════════════════════════════════════
     PRESENTATION MODE
     ════════════════════════════════════════════════════════════ */

  function initPresentation() {
    var main = document.getElementById('main-content');
    if (!main) return;

    var slides = [];

    /* Strategy 1: use existing .c-section elements */
    var cSections = Array.from(main.querySelectorAll('.c-section'));
    if (cSections.length >= 2) {
      // Show chapter hero + phase bar as slide 0 (never hidden)
      slides = cSections;
    } else {
      /* Strategy 2: wrap by h2 boundaries in .prose-content */
      slides = buildH2Slides(main);
    }

    if (slides.length < 2) return;

    var current = 0;
    var total   = slides.length;

    /* Hide all slides except first */
    slides.forEach(function (s, i) {
      if (i > 0) s.style.display = 'none';
    });

    var controls = document.getElementById('slide-controls');
    var prevBtn  = document.getElementById('prev-btn');
    var nextBtn  = document.getElementById('next-btn');
    var exitBtn  = document.getElementById('exit-btn');
    var progress = document.getElementById('slide-progress');

    function render() {
      progress.textContent = (current + 1) + ' / ' + total;
      prevBtn.disabled = current === 0;
      nextBtn.disabled = current === total - 1;
    }

    function goTo(idx) {
      slides[current].style.display = 'none';
      current = Math.max(0, Math.min(idx, total - 1));
      slides[current].style.display = '';
      render();
      window.scrollTo({ top: 0, behavior: 'auto' });
    }

    render();

    prevBtn.addEventListener('click', function () { goTo(current - 1); });
    nextBtn.addEventListener('click', function () { goTo(current + 1); });
    exitBtn.addEventListener('click', function () {
      var url = new URL(window.location.href);
      url.searchParams.delete('present');
      window.location.href = url.toString();
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowRight' || e.key === 'ArrowDown') {
        e.preventDefault(); goTo(current + 1);
      } else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') {
        e.preventDefault(); goTo(current - 1);
      } else if (e.key === 'Escape') {
        exitBtn.click();
      }
    });
  }

  function buildH2Slides(container) {
    /* Find the prose content wrapper if present, else use container */
    var content = container.querySelector('.prose-content') || container;
    var children = Array.from(content.childNodes);

    /* Find indices of H2 nodes */
    var h2Indices = [];
    children.forEach(function (node, i) {
      if (node.nodeName === 'H2') h2Indices.push(i);
    });
    if (h2Indices.length < 2) return [];

    var wrappers = [];
    h2Indices.forEach(function (h2Idx, sIdx) {
      var endIdx = (sIdx + 1 < h2Indices.length) ? h2Indices[sIdx + 1] : children.length;
      var group  = children.slice(h2Idx, endIdx);

      var wrapper = document.createElement('div');
      wrapper.className = 'slide-h2-section';
      content.insertBefore(wrapper, group[0]);
      group.forEach(function (node) { wrapper.appendChild(node); });
      wrappers.push(wrapper);
    });
    return wrappers;
  }

}());
