---
title: "Calcul intégral"
numero: 11
en_cours: true
annee: "2025-2026"
description: "Intégrales définies et aires sous la courbe."

documents:
  - label: "Cours complet"
    type: cours
    url: "/assets/pdf/terminale-specialite/TEDS11 - Calcul Integral/Cours/TEDS11 - Calcul intégral - Cours.pdf"
  - label: "Exercices"
    type: exercices
    url: "/assets/pdf/seconde/ch05-exos.pdf"

videos:
  - label: "Calculer une intégrale"
    youtube_id: "Z3vKJJE57Uw"
    source: "Yvan Monka"
  - label: "Effectuer une intégration par parties"
    youtube_id: "xbb3vnzF3EA"
    source: "Yvan Monka"

mathalea:
  - label: "MathAlea - Exercice"
    exercices: "id=TSA8-10&nb=5&s=false&i=1&v=eleve"
    
evaluations:
  - label: "DS n°X — Sujet"
    sujet_url: "/assets/pdf/seconde/ds01-sujet.pdf"
    corrige_url: "/assets/pdf/seconde/ds01-corrige.pdf"
    date_ds: "2026-04-24"
    notes: [8, 10, 12, 14, 16]
    feedback: "Commentaire sur les résultats."

coin_expert:
  - label: "Lien d'approfondissement"
    url: "https://..."
---

## Ce que ce chapitre travaille

- Intégrale définie et aire sous la courbe pour une fonction continue positive.
- Définition de $F_a(x)=\int_a^x f(t)\,dt$ et lien avec la primitive.
- Relation $\int_a^b f(x)\,dx = F(b)-F(a)$.
- Intégrale signée pour les fonctions de signe quelconque.

## Carte mentale

{{< mindmap 1 >}}
# Intégration

## Lien avec primitive

- $I = \int_a^b f(x)dx = \left[ F(x)\right]_a^b=F(b)-F(a)$

## Propriétés algébriques

- $\forall \alpha \in \R, \int_a^b (f + \alpha g)(x)dx= \int_a^b f(x)dx+ \alpha\int_a^b g(x)dx$
- $\int_a^a f(x)dx=0$
- $\int_b^a f(x)dx=-\int_a^b f(x)dx$
- $\int_a^b f(x)dx+\int_b^c f(x)dx=\int_a^c f(x)dx=0$

## Inégalités

- Si $f \geqslant 0$ sur $\[a;b]$, alors $\int_a^b f(x)dx \geqslant 0$
- Si $f \geqslant g$ sur $\[a;b]$, alors $\int_a^b f(x)dx \geqslant \int_a^b g(x)dx$


## Valeur moyenne

- $\mu = \dfrac{1}{b-a} \int_a^b f(x)dx$

## Intégration par parties

- $\int_a^b u(x)v'(x)dx=\left[u(x)v(x)\right]_a^b-\int_a^b u(x)v'(x)dx$
{{< /mindmap >}}

## Rappels utiles

- Primitives et dérivées.
- Exemples de fonctions simples dont on sait trouver des primitives.
