# OXL MATH — Guide d'enrichissement

Ce dépôt contient le site Hugo d'OXL MATH. Le site est construit avec Hugo Extended, SCSS, KaTeX, GLightbox et des shortcodes pour intégrer :

- des documents PDF
- des vidéos YouTube
- des exercices MathAlea
- des évaluations avec notes et feedback
- des pages de niveau / chapitres

---

## Structure principale

- `hugo.toml` : configuration du site
- `content/` : contenu du site
  - `_index.md` : page d'accueil
  - `<section>/_index.md` : page de niveau (`seconde`, `premiere-specialite`, `terminale-specialite`, `maths-expertes`, `tools`)
  - `<section>/chXX-slug.md` : fiche de chapitre
- `archetypes/chapitre.md` : modèle pour créer un nouveau chapitre
- `static/assets/pdf/` : fichiers PDF accessibles via `/assets/pdf/...`
- `data/actualites.yaml` : actualités / ticker
- `layouts/shortcodes/` : shortcodes pour PDF, YouTube et MathAlea
- `assets/scss/` : styles SCSS du site
- `.github/workflows/hugo.yml` : déploiement GitHub Pages

---

## Ajouter un nouveau niveau ou une nouvelle page de section

1. Crée un dossier sous `content/` si il n'existe pas déjà :
   - `content/nouveau-niveau/`
2. Ajoute un `_index.md` dans ce dossier pour définir la page de section :

```yaml
---
title: "Mon nouveau niveau"
description: "Description du niveau"
---

Texte de présentation du niveau.
```

3. Si ton niveau doit apparaître dans le menu, le dossier doit simplement être une section de Hugo.

---

## Créer un nouveau chapitre

Le plus simple est d'utiliser le modèle (`archetypes/chapitre.md`) :

```bash
hugo new seconde/ch05-fonctions.md
```

Puis édite le fichier créé dans `content/seconde/` et adapte les champs YAML.

### Champs front matter recommandés

```yaml
---
title: "Titre du chapitre"
numero: 5
en_cours: false
annee: "2025-2026"
description: "Brève description du chapitre."

documents:
  - label: "Cours complet"
    type: cours
    url: "/assets/pdf/seconde/ch05-cours.pdf"
  - label: "Exercices"
    type: exercices
    url: "/assets/pdf/seconde/ch05-exos.pdf"
  - label: "Corrigé"
    type: corrige
    url: "/assets/pdf/seconde/ch05-corrige.pdf"

videos:
  - label: "Titre de la vidéo"
    youtube_id: "XXXXXXXXXXX"
    source: "Mathsettiques"

mathalea:
  - label: "MathAlea - Exercice"
    exercices: "CODEID,nb=5&v=eleve"

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
```

### Contenu Markdown

Sous le front matter, ajoute ton contenu en Markdown :

- titres `##`
- listes
- tableaux
- équations KaTeX avec `$...$` ou `$$...$$`

Exemple :

```md
## Rappels

Une fonction $f$ est continue si ...

$$rac{d}{dx} e^x = e^x$$
```

---

## Ajouter ou mettre à jour des documents PDF

1. Place les fichiers PDF dans `static/assets/pdf/<section>/`.
2. Réfère-toi à ces fichiers depuis le front matter des chapitres avec des liens absolus commençant par `/assets/pdf/...`.

Exemple :

```yaml
- label: "Cours"
  type: cours
  url: "/assets/pdf/terminale-specialite/ch04-cours.pdf"
```

---

## Ajouter une vidéo YouTube

La liste `videos` dans le front matter crée automatiquement une carte vidéo.

```yaml
videos:
  - label: "Titre de la vidéo"
    youtube_id: "rfG8ce4nNh0"
    source: "Mathsettiques"
```

Tu peux aussi insérer une vidéo directement dans le contenu Markdown avec le shortcode :

```md
{{< youtube "rfG8ce4nNh0" "Titre de la vidéo" >}}
```

---

## Ajouter un exercice MathAlea

Dans le front matter :

```yaml
mathalea:
  - label: "Calcul de primitives"
    exercices: "can3F10,nb=5&v=eleve"
```

Ou directement dans un contenu Markdown avec le shortcode :

```md
{{< mathalea "can3F10,nb=5&v=eleve" "Exercices MathAlea" >}}
```

Le champ `exercices` doit contenir l'ID MathAlea suivi des paramètres URL.

---

## Ajouter un document PDF direct dans le contenu

Utilise le shortcode `pdf` pour afficher un lien / bouton PDF :

```md
{{< pdf "/assets/pdf/seconde/ch05-cours.pdf" "Cours Chapitre 5" >}}
```

---

## Ajouter une actualité

Édite `data/actualites.yaml` et ajoute un élément :

```yaml
items:
  - texte: "Nouvelle ressource disponible"
    niveau: seconde
    date: "2026-05-01"
```

Le code affiche automatiquement les actualités dans le ticker de la page d'accueil.

---

## Ajouter une page `Tools`

La page `content/tools/_index.md` contient le texte et les sections du lab.
Tu peux enrichir cette page en ajoutant du contenu Markdown, des liens ou des prises en main Python.

---

## Ajouter un nouveau chapitre via l’archetype

Pour créer un fichier chapitres cohérent avec la structure attendue :

```bash
hugo new premiere-specialite/ch06-nouveau-chapitre.md
```

Puis édite ce fichier en suivant le modèle `archetypes/chapitre.md`.

---

## Tests et build local

Pour prévisualiser le site localement :

```bash
cd /Users/olivierlaurent/Documents/Travail Olivier/Git/olaurent.github.io
hugo server -D
```

Ouvre ensuite :

```text
http://localhost:1313
```

Pour construire le site sans le serveur :

```bash
hugo --minify
```

---

## Déploiement

Le site se déploie automatiquement sur GitHub Pages via `.github/workflows/hugo.yml`.

- Le contenu généré provient du dossier `public/`.
- `public/` est ignoré par Git (`.gitignore`).
- Pousse sur `main` pour déclencher le workflow.

---

## Bons usages

- Respecte les slugs de dossier : `seconde`, `premiere-specialite`, `terminale-specialite`, `maths-expertes`, `tools`.
- Place les PDF dans `static/assets/pdf/<section>/`.
- Utilise `hugo new` pour créer de nouveaux chapitres et garder un front matter propre.
- Si tu ajoutes des CSS ou JS personnalisés, mets-les dans `assets/` puis adapte les templates.

---

## Notes techniques rapides

- Les templates Hugo se trouvent dans `layouts/`.
- Les styles SCSS sont dans `assets/scss/`.
- Les shortcodes les plus utiles :
  - `{{< pdf ... >}}`
  - `{{< youtube ... >}}`
  - `{{< mathalea ... >}}`

Bonne mise à jour du site !