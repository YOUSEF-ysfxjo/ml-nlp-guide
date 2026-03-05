/**
 * ML & NLP Guide — TOC, theme, progress, copy
 */
(function () {
  const tocNav = document.getElementById('tocNav');
  if (!tocNav) return;

  const tocData = [
    { id: '1-the-linear-model', label: 'The Linear Model' },
    { id: '2-the-problem-with-linear-models', label: 'The Problem with Linear Models' },
    { id: '3-neural-networks', label: 'Neural Networks' },
    { id: '4-activation-functions', label: 'Activation Functions' },
    { id: '5-learnable-parameters', label: 'Learnable Parameters' },
    { id: '6-optimization', label: 'Optimization' },
    { id: '7-the-text-problem', label: 'The Text Problem' },
    { id: '8-one-hot-encoding', label: 'One-Hot Encoding' },
    { id: '9-word-embeddings', label: 'Word Embeddings' },
    { id: '10-word2vec', label: 'Word2Vec' },
    { id: '11-word2vec-architecture', label: 'Word2Vec Architecture' },
    { id: '12-dot-product-similarity', label: 'Dot Product Similarity' },
    { id: '13-distributional-hypothesis', label: 'Distributional Hypothesis' },
    { id: '14-limitations-of-word2vec', label: 'Limitations of Word2Vec' },
    { id: '15-representing-sentences', label: 'Representing Sentences' },
    { id: '16-the-road-ahead', label: 'The Road Ahead' },
    { id: 'related-papers', label: 'Related Papers' }
  ];

  tocData.forEach(function (item) {
    var a = document.createElement('a');
    a.href = '#' + item.id;
    a.textContent = item.label;
    tocNav.appendChild(a);
  });

  var sections = document.querySelectorAll('.section[id], [id="related-papers"]');
  var observer = new IntersectionObserver(
    function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var id = entry.target.id;
        tocNav.querySelectorAll('a').forEach(function (link) {
          link.classList.toggle('active', link.getAttribute('href') === '#' + id);
        });
      });
    },
    { rootMargin: '-20% 0px -70% 0px', threshold: 0 }
  );
  sections.forEach(function (s) { return observer.observe(s); });

  /* Theme toggle */
  var STORAGE_KEY = 'ml-nlp-guide-theme';
  var themeToggle = document.getElementById('themeToggle');
  var themeLabel = document.getElementById('themeLabel');
  if (themeToggle && themeLabel) {
    var iconSun = themeToggle.querySelector('.icon-sun');
    var iconMoon = themeToggle.querySelector('.icon-moon');

    function getTheme() {
      return localStorage.getItem(STORAGE_KEY) ||
        (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
    }

    function setTheme(theme) {
      document.documentElement.setAttribute('data-theme', theme === 'dark' ? 'dark' : '');
      localStorage.setItem(STORAGE_KEY, theme);
      themeLabel.textContent = theme === 'dark' ? 'Light mode' : 'Dark mode';
      if (iconSun) iconSun.style.display = theme === 'dark' ? 'none' : 'inline';
      if (iconMoon) iconMoon.style.display = theme === 'dark' ? 'inline' : 'none';
    }

    themeToggle.addEventListener('click', function () {
      setTheme(getTheme() === 'dark' ? 'light' : 'dark');
    });
    setTheme(getTheme());
  }

  /* Read progress bar */
  var progressBar = document.getElementById('readProgress');
  if (progressBar) {
    window.addEventListener('scroll', function () {
      var winScroll = document.documentElement.scrollTop;
      var height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      progressBar.style.width = height ? (winScroll / height) * 100 + '%' : '0%';
    });
  }

  /* Copy code buttons */
  document.querySelectorAll('.copy-btn[data-copy]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var codeBlock = btn.closest('.code-block');
      var pre = codeBlock ? codeBlock.querySelector('pre code') : null;
      var text = pre ? pre.textContent : '';
      navigator.clipboard.writeText(text).then(function () {
        btn.textContent = 'Copied!';
        btn.classList.add('copied');
        setTimeout(function () {
          btn.textContent = 'Copy';
          btn.classList.remove('copied');
        }, 2000);
      });
    });
  });
})();
