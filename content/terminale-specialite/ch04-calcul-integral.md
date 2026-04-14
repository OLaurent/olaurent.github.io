---
title: "Calcul Intégral"
numero: 4
en_cours: false
annee: "2025-2026"
description: "Primitives, intégrales définies et aires sous la courbe."

documents:
  - label: "Cours — Version élève"
    type: cours
    url: "/assets/pdf/terminale-specialite/ch04-cours-eleve.pdf"
  - label: "Cours — Version complète"
    type: cours
    url: "/assets/pdf/terminale-specialite/ch04-cours-complet.pdf"
  - label: "Feuille d'exercices 1 — Primitives"
    type: exercices
    url: "/assets/pdf/terminale-specialite/ch04-exos-1.pdf"
  - label: "Corrigé — Feuille 1"
    type: corrige
    url: "/assets/pdf/terminale-specialite/ch04-exos-1-corrige.pdf"
  - label: "Feuille d'exercices 2 — Intégrales"
    type: exercices
    url: "/assets/pdf/terminale-specialite/ch04-exos-2.pdf"
  - label: "Corrigé — Feuille 2"
    type: corrige
    url: "/assets/pdf/terminale-specialite/ch04-exos-2-corrige.pdf"

videos:
  - label: "Comprendre l'intégrale (Mathsettiques)"
    youtube_id: "rfG8ce4nNh0"
    source: "Mathsettiques"
  - label: "Calcul de primitives — méthode"
    youtube_id: "WUvTyaaNkzM"
    source: "Mathsettiques"

mathalea:
  - label: "Calcul de primitives (niveau 1)"
    exercices: "can3F10,nb=5&v=eleve"
  - label: "Intégrales et aires"
    exercices: "can3F11,nb=5&v=eleve"

evaluations:
  - label: "DS n°4 — Calcul Intégral"
    sujet_url: "/assets/pdf/terminale-specialite/ds04-sujet.pdf"
    corrige_url: "/assets/pdf/terminale-specialite/ds04-corrige.pdf"
    date_ds: "2026-03-18"
    notes: [4, 6, 7, 8, 8, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 16, 17, 19]
    feedback: "Bonne maîtrise du calcul de primitives. Difficultés observées sur les aires entre deux courbes — retravailler ce point avant le bac."

coin_expert:
  - label: "Paradoxe de Gabriel (trompette de Torricelli)"
    url: "https://fr.wikipedia.org/wiki/Trompette_de_Torricelli"
  - label: "Intégration numérique — méthodes de Riemann"
    url: "https://fr.wikipedia.org/wiki/Somme_de_Riemann"
---

## Rappels de cours

Le **calcul intégral** est l'un des piliers de l'analyse mathématique. Il permet de calculer des **aires**, des **volumes** et de résoudre de nombreux problèmes en physique et en probabilités.

### Définition — Primitive

Une fonction $F$ est une **primitive** de $f$ sur un intervalle $I$ si $F'(x) = f(x)$ pour tout $x \in I$.

> **Théorème fondamental** : Si $f$ est continue sur $[a; b]$, alors :
> $$\int_a^b f(x)\,dx = \left[F(x)\right]_a^b = F(b) - F(a)$$

### Formules de base

| Fonction $f(x)$ | Primitive $F(x)$ |
|:---:|:---:|
| $x^n$ ($n \neq -1$) | $\dfrac{x^{n+1}}{n+1}$ |
| $e^x$ | $e^x$ |
| $\dfrac{1}{x}$ | $\ln\|x\|$ |
| $\cos x$ | $\sin x$ |
| $\sin x$ | $-\cos x$ |
