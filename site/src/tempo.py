# Script temporaire à exécuter dans un shell Flask
from app import app, db
from models import Exercice, Tag, Level

with app.app_context():
    # Vérifier les exercices sans level_id ou theme_id
    null_level_exercices = Exercice.query.filter(Exercice.level_id.is_(None)).all()
    print(f"Exercices sans level_id: {len(null_level_exercices)}")
    
    null_theme_exercices = Exercice.query.filter(Exercice.theme_id.is_(None)).all()
    print(f"Exercices sans theme_id: {len(null_theme_exercices)}")
    
    # Vérifier les tags sans level_id
    null_level_tags = Tag.query.filter(Tag.level_id.is_(None)).all()
    print(f"Tags sans level_id: {len(null_level_tags)}")
    
    # Si besoin, attribuer un niveau par défaut aux tags sans niveau
    if null_level_tags:
        default_level = Level.query.first()
        if default_level:
            for tag in null_level_tags:
                tag.level_id = default_level.id
            db.session.commit()
            print(f"Tags mis à jour avec le niveau par défaut: {default_level.name}")