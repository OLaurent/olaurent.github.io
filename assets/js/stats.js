/**
 * OXL MATH — Stats d'évaluation (Chart.js)
 * Calcul automatique depuis les notes brutes (data-notes)
 * et rendu d'un histogramme par tranche de 2 points.
 */
(function () {
  'use strict';

  /**
   * Calcule les statistiques d'un tableau de notes.
   * @param {number[]} notes
   * @returns {{ moyenne, mediane, ecarttype, min, max, effectif }}
   */
  function calculerStats(notes) {
    if (!notes.length) return null;
    const sorted = [...notes].sort((a, b) => a - b);
    const effectif = sorted.length;
    const somme = sorted.reduce((acc, n) => acc + n, 0);
    const moyenne = somme / effectif;

    const mediane = effectif % 2 === 0
      ? (sorted[effectif / 2 - 1] + sorted[effectif / 2]) / 2
      : sorted[Math.floor(effectif / 2)];

    const variance = sorted.reduce((acc, n) => acc + Math.pow(n - moyenne, 2), 0) / effectif;
    const ecarttype = Math.sqrt(variance);

    return {
      moyenne: Math.round(moyenne * 100) / 100,
      mediane: Math.round(mediane * 100) / 100,
      ecarttype: Math.round(ecarttype * 100) / 100,
      min: sorted[0],
      max: sorted[effectif - 1],
      effectif
    };
  }

  /**
   * Construit les tranches de l'histogramme (par intervalles de 2 points, 0-20).
   */
  function construireHistogramme(notes) {
    const tranches = [];
    for (let i = 0; i < 20; i += 2) {
      const label = `${i}–${i + 2}`;
      const count = notes.filter(n => n >= i && n < i + 2).length;
      tranches.push({ label, count });
    }
    // Inclure la note 20
    tranches[tranches.length - 1].count += notes.filter(n => n === 20).length;
    return tranches;
  }

  /**
   * Affiche une valeur dans un élément stat-value.
   */
  function afficherStat(canvas, key, value) {
    const id = canvas.id.replace('chart-', '');
    const el = document.getElementById(`stat-${key}-${id}`);
    if (el) el.textContent = typeof value === 'number' ? value.toFixed(2).replace('.00', '') : value;
  }

  /**
   * Initialise un graphique Chart.js dans un canvas donné.
   */
  function initChart(canvas) {
    let notes;
    try {
      notes = JSON.parse(canvas.dataset.notes);
    } catch (e) {
      console.warn('OXL Stats: notes JSON invalides', e);
      return;
    }

    if (!Array.isArray(notes) || notes.length === 0) return;

    const stats = calculerStats(notes);
    const histo = construireHistogramme(notes);

    // Afficher les indicateurs
    afficherStat(canvas, 'moyenne',   stats.moyenne);
    afficherStat(canvas, 'mediane',   stats.mediane);
    afficherStat(canvas, 'ecarttype', stats.ecarttype);
    afficherStat(canvas, 'max',       stats.max);
    afficherStat(canvas, 'effectif',  stats.effectif);

    // Couleur de fond dynamique depuis CSS
    const couleur = getComputedStyle(document.documentElement)
      .getPropertyValue('--couleur-niveau').trim() || '#D4AF37';

    new Chart(canvas, {
      type: 'bar',
      data: {
        labels: histo.map(t => t.label),
        datasets: [{
          label: 'Élèves',
          data: histo.map(t => t.count),
          backgroundColor: `${couleur}55`,
          borderColor: couleur,
          borderWidth: 1.5,
          borderRadius: 4,
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: true,
        plugins: {
          legend: { display: false },
          tooltip: {
            callbacks: {
              title: (items) => `Notes ${items[0].label}`,
              label: (item) => ` ${item.raw} élève${item.raw !== 1 ? 's' : ''}`
            }
          }
        },
        scales: {
          x: {
            ticks: { color: '#A0A0B0', font: { size: 10 } },
            grid: { color: 'rgba(255,255,255,0.05)' }
          },
          y: {
            beginAtZero: true,
            ticks: {
              color: '#A0A0B0',
              font: { size: 10 },
              stepSize: 1,
              precision: 0
            },
            grid: { color: 'rgba(255,255,255,0.07)' }
          }
        }
      }
    });
  }

  // Initialiser tous les canvas de stats sur la page
  document.querySelectorAll('canvas[data-notes]').forEach(initChart);

})();
