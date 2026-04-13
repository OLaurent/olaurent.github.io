---
title: "{{ replace .File.ContentBaseName "-" " " | title }}"
numero: 1
en_cours: false
annee: "{{ .Site.Params.anneeEnCours }}"
description: "Brève description du chapitre."

documents:
  - label: "Cours complet"
    type: cours
    url: "/assets/pdf/{{ .Section }}/ch01-cours.pdf"
  # - label: "Cours — Version élève"
  #   type: cours
  #   url: "/assets/pdf/{{ .Section }}/ch01-cours-eleve.pdf"
  - label: "Feuille d'exercices 1"
    type: exercices
    url: "/assets/pdf/{{ .Section }}/ch01-exos-1.pdf"
  - label: "Corrigé — Feuille 1"
    type: corrige
    url: "/assets/pdf/{{ .Section }}/ch01-exos-1-corrige.pdf"

# videos:
#   - label: "Titre de la vidéo"
#     youtube_id: "XXXXXXXXX"
#     source: "Mathsettiques"

# mathalea:
#   - label: "Titre de l'exercice"
#     exercices: "CODEID,nb=5&v=eleve"
#     # Trouvez les IDs sur https://coopmaths.fr/alea/

# evaluations:
#   - label: "DS n°X — Titre"
#     sujet_url: "/assets/pdf/{{ .Section }}/dsXX-sujet.pdf"
#     corrige_url: "/assets/pdf/{{ .Section }}/dsXX-corrige.pdf"
#     date_ds: "{{ now.Format "2006-01-02" }}"
#     notes: []  # Liste brute ex: [8, 10, 12, 14, 16]
#     feedback: "Commentaire sur les résultats de la classe."

# coin_expert:
#   - label: "Lien d'approfondissement"
#     url: "https://..."
---

<!-- Contenu Markdown libre : notes de cours complémentaires, rappels, etc. -->
<!-- Utilisez $formule$ ou $$formule$$ pour les équations KaTeX. -->
