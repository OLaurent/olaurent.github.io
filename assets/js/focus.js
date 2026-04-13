/**
 * OXL MATH — Focus Mode
 * Toggle via bouton œil — masque header/footer — persiste via localStorage.
 */
(function () {
  'use strict';

  const STORAGE_KEY = 'oxl-focus-mode';
  const btn = document.getElementById('focus-toggle');
  if (!btn) return;

  function setFocusMode(active) {
    document.body.classList.toggle('focus-mode', active);
    btn.setAttribute('aria-pressed', String(active));
    btn.setAttribute('aria-label', active ? 'Désactiver le mode focus' : 'Activer le mode focus');
    try { localStorage.setItem(STORAGE_KEY, active ? '1' : '0'); } catch (_) {}
  }

  // Restaurer l'état au chargement
  try {
    if (localStorage.getItem(STORAGE_KEY) === '1') setFocusMode(true);
  } catch (_) {}

  btn.addEventListener('click', function () {
    setFocusMode(!document.body.classList.contains('focus-mode'));
  });

  // Raccourci clavier : Ctrl+F (ou Cmd+F sur Mac) → désactivé pour ne pas interférer.
  // On utilise Alt+F à la place.
  document.addEventListener('keydown', function (e) {
    if (e.altKey && e.key === 'f') {
      e.preventDefault();
      setFocusMode(!document.body.classList.contains('focus-mode'));
    }
  });

})();
