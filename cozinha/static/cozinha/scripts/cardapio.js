// cardapio.js
document.addEventListener('DOMContentLoaded', () => {
  const buttons = document.querySelectorAll('button[data-target]');

  buttons.forEach(btn => {
    const targetId = btn.dataset.target;
    const container = document.getElementById(targetId);
    if (!container) return;

    const initialHiddenCards = Array.from(container.querySelectorAll('.menu-card.hidden'));
    const hiddenCount = initialHiddenCards.length;

    if (hiddenCount === 0) {
      btn.style.display = 'none';
      return;
    }

    btn.dataset.hiddenCount = String(hiddenCount);
    btn.dataset.expanded = 'false';

    btn.addEventListener('click', () => {
      const isExpanded = btn.dataset.expanded === 'true';
      const allCards = Array.from(container.querySelectorAll('.menu-card'));
      const n = Number(btn.dataset.hiddenCount);

      if (!isExpanded) {
        allCards.slice(-n).forEach(card => card.classList.remove('hidden'));
        btn.textContent = 'Ver menos';
        btn.dataset.expanded = 'true';
      } else {
        allCards.slice(-n).forEach(card => card.classList.add('hidden'));
        btn.textContent = 'Ver mais';
        btn.dataset.expanded = 'false';
      }
    });
  });
});
