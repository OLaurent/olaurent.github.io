# Exercice App - Application de Gestion d'Exercices Mathématiques

Cette application Flask a été conçue pour gérer et présenter des exercices mathématiques. Elle utilise SQLAlchemy pour les interactions avec la base de données et suit une architecture modèle en Factory Pattern avec des blueprints pour une meilleure organisation du code.

## Nouvelle Structure du Projet

```
olaurent.github.io/
├── wsgi.py                    # Point d'entrée principal de l'application
├── src/                       # Code source principal
│   ├── __init__.py            # Factory pour créer l'application Flask
│   ├── config.py              # Configuration centralisée
│   ├── extensions.py          # Extensions Flask (SQLAlchemy, etc.)
│   ├── models/                # Définitions des modèles de données
│   │   ├── __init__.py        
│   │   └── entities.py        # Classes de modèles (Exercice, Level, Theme, Tag)
│   ├── routes/                # Routes de l'application organisées par module
│   │   ├── __init__.py        
│   │   ├── main_routes.py     # Routes générales (accueil, métadonnées)
│   │   ├── exercise_routes.py # Routes pour la gestion des exercices
│   │   └── export_routes.py   # Routes pour l'exportation
│   ├── exporters/             # Classes pour l'exportation des données
│   │   ├── __init__.py        
│   │   ├── latex_exporter.py  # Exportateur de format LaTeX
│   │   └── docx_exporter.py   # Exportateur de format DOCX
│   ├── static/                # Fichiers statiques
│   │   ├── css/               # Styles CSS (Bulma, personnalisations)
│   │   ├── js/                # Scripts JavaScript
│   │   └── img/               # Images
│   └── templates/             # Templates HTML
│       ├── base.html          # Template de base
│       ├── index.html         # Page d'accueil
│       ├── create_exercise.html # Formulaire de création
│       ├── edit_exercise.html # Formulaire d'édition
│       ├── export.html        # Page d'exportation
│       └── manage_metadata.html # Gestion des niveaux, thèmes et tags
├── migrations/                # Fichiers de migration de base de données
├── instance/                  # Données spécifiques à l'instance (BD SQLite)
├── requirements.txt           # Dépendances Python
└── README.md                  # Documentation du projet
```

## Installation

1. Cloner le dépôt :
   ```sh
   git clone https://github.com/olaurent/olaurent.github.io.git
   cd olaurent.github.io
   ```

2. Créer un environnement virtuel :
   ```sh
   python -m venv venv
   source venv/bin/activate  # Sur Windows : `venv\Scripts\activate`
   ```

3. Installer les packages requis :
   ```sh
   pip install -r requirements.txt
   ```

## Configuration de la Base de Données

1. La base de données SQLite est configurée par défaut dans `src/config.py`
2. Exécuter les migrations pour créer le schéma de la base de données :
   ```sh
   export FLASK_APP=src
   flask db upgrade
   ```

3. Initialiser la base de données (si nécessaire) :
   ```sh
   python -c "from src import create_app; from src.extensions import db; app = create_app(); app.app_context().push(); db.create_all()"
   ```

## Remplissage de la Base de Données

Vous pouvez peupler la base de données de différentes manières :

1. Utiliser le script fourni :
   ```sh
   python src/scripts/populate_db.py
   ```

2. Manuellement via le shell Flask :
   ```sh
   export FLASK_APP=src
   flask shell
   >>> from src.models.entities import Exercice, Level, Theme, Tag, db
   >>> # Créer et ajouter des exemples
   >>> level = Level(name="Terminale")
   >>> db.session.add(level)
   >>> db.session.commit()
   ```

3. Importer depuis un JSON :
   ```sh
   python src/scripts/import_data.py --file path/to/exercises.json
   ```

## Exécution de l'Application

Pour démarrer l'application Flask, exécutez :
```sh
python wsgi.py
```

L'application sera accessible à l'adresse `http://127.0.0.1:5000`.

## Architecture et Blueprints

L'application utilise le modèle de conception Factory Pattern avec des blueprints pour une meilleure organisation :

- **main_bp** : Routes principales et gestion des métadonnées
- **exercise_bp** : Routes pour créer, modifier et supprimer des exercices
- **export_bp** : Routes pour l'exportation des exercices sélectionnés

Cette architecture permet une meilleure séparation des préoccupations et facilite les tests.

## Fonctionnalités Principales

- **Gestion des exercices** : Création, modification et suppression
- **Gestion des métadonnées** : Organisation par niveaux, thèmes et tags
- **Exportation** : Génération de documents LaTeX et DOCX à partir des exercices sélectionnés
- **Interface utilisateur intuitive** : Interface basée sur Bulma CSS, avec des formulaires faciles à utiliser

## Conversion LaTeX vers SVG

Pour convertir du LaTeX en SVG, vous pouvez utiliser le workflow suivant :

1. Utiliser la commande `dvisvgm` pour convertir le fichier DVI en SVG :
   ```sh
   dvisvgm --libgs=/opt/local/lib/libgs.dylib SVGFilename.dvi
   ```

2. Modifier le fichier SVG généré pour le centrer sur la page en ajoutant l'attribut de style suivant :
   ```html
   <svg style="display: block; margin: 0 auto;">
   ```

3. Remplacer la couleur `#000` par `#3e8ed0` dans le fichier SVG.

4. Supprimer les éléments `<path>` avec `fill='#fff'`.

5. Ajouter `fill:#3e8ed0;` aux données de texte dans le fichier SVG.

## Développement et Contribution

Pour contribuer au projet :

1. Créez une branche pour vos modifications
2. Assurez-vous que les tests passent
3. Soumettez une pull request

## Gestion des Erreurs Courantes

- **Erreur de template non trouvé** : Vérifiez les chemins dans `src/__init__.py`
- **Erreur de construction d'URL** : Utilisez le format `blueprint_name.route_name` dans vos appels à `url_for()`
- **Erreur de base de données** : Assurez-vous que les migrations sont à jour avec `flask db upgrade`

## Licence

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.