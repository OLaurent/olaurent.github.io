from app import app, db
from models import Level, Theme, Tag, Exercice

def migrate_data():
    with app.app_context():
        print("Début de la migration des données...")
        
        # 1. Créer des niveaux à partir des valeurs existantes
        unique_levels = db.session.query(Exercice.level).distinct().all()
        level_mapping = {}  # {nom_niveau: objet_niveau}
        
        print(f"Création de {len(unique_levels)} niveaux...")
        for level_name in [l[0] for l in unique_levels if l[0]]:
            new_level = Level(name=level_name)
            db.session.add(new_level)
        
        # Commit pour obtenir les IDs des niveaux
        db.session.flush()
        
        # Créer le mapping des niveaux pour une référence facile
        for level in Level.query.all():
            level_mapping[level.name] = level
        
        # 2. Créer des thèmes par niveau
        print("Création des thèmes...")
        theme_mapping = {}  # {(nom_niveau, nom_theme): objet_theme}
        
        # Trouver les combinaisons uniques (niveau, thème)
        unique_level_themes = db.session.query(Exercice.level, Exercice.theme).distinct().all()
        
        for level_name, theme_name in unique_level_themes:
            if level_name and theme_name and level_name in level_mapping:
                level_obj = level_mapping[level_name]
                new_theme = Theme(name=theme_name, level_id=level_obj.id)
                db.session.add(new_theme)
                
        # Commit pour obtenir les IDs des thèmes
        db.session.flush()
        
        # Créer le mapping des thèmes
        for theme in Theme.query.all():
            level_name = Level.query.get(theme.level_id).name
            theme_mapping[(level_name, theme.name)] = theme
        
        # 3. Migrer les tags vers les niveaux
        print("Migration des tags...")
        
        # Pour chaque tag, nous devons décider quel niveau lui attribuer
        # Approche: assigner le niveau le plus courant parmi les exercices associés
        all_tags = Tag.query.all()
        for tag in all_tags:
            if not tag.exercices:  # Si le tag n'est associé à aucun exercice
                continue
                
            # Compter les occurrences de chaque niveau
            level_counts = {}
            for exercice in tag.exercices:
                if exercice.level:
                    level_counts[exercice.level] = level_counts.get(exercice.level, 0) + 1
            
            # Trouver le niveau le plus fréquent
            if level_counts:
                most_common_level = max(level_counts, key=level_counts.get)
                if most_common_level in level_mapping:
                    tag.level_id = level_mapping[most_common_level].id
        
        # 4. Mettre à jour les exercices avec les nouvelles relations
        print("Mise à jour des exercices...")
        for exercice in Exercice.query.all():
            if exercice.level and exercice.theme:
                key = (exercice.level, exercice.theme)
                if key in theme_mapping:
                    theme_obj = theme_mapping[key]
                    exercice.level_id = theme_obj.level_id
                    exercice.theme_id = theme_obj.id
        
        # Commit final
        db.session.commit()
        print("Migration des données terminée avec succès!")

if __name__ == "__main__":
    migrate_data()