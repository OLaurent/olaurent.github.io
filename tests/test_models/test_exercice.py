"""
Tests pour le modèle Exercice.
"""

def test_create_exercice(session):
    """Test la création d'un exercice."""
    from src.models.entities import Exercice, Level, Theme
    
    # Créer les objets nécessaires
    level = Level(name="Terminale")
    session.add(level)
    session.commit()
    
    theme = Theme(name="Analyse", level_id=level.id)
    session.add(theme)
    session.commit()
    
    # Créer un exercice
    exercice = Exercice(
        level_id=level.id,
        theme_id=theme.id,
        content="<p>Test</p>",
        latex_code="Test",
        correction="<p>Correction</p>",
        latex_correction="Correction"
    )
    session.add(exercice)
    session.commit()
    
    # Vérifications
    assert exercice.id is not None
    assert exercice.level_id == level.id
    assert exercice.theme_id == theme.id
    assert exercice.content == "<p>Test</p>"
    
    # Vérifier les relations
    assert exercice.level == level
    assert exercice.theme == theme

def test_exercice_tags_relationship(session, sample_data):
    """Test la relation many-to-many entre exercices et tags."""
    from src.models.entities import Exercice, Tag
    
    # Récupérer un exercice et un tag des données d'exemple
    exercice = sample_data['exercices'][0]
    tag = sample_data['tags'][1]  # tag2 ("Fonctions")
    
    # Associer le tag à l'exercice
    exercice.tags.append(tag)
    session.commit()
    
    # Vérifier la relation
    assert tag in exercice.tags
    assert exercice in tag.exercices
    
    # Vérifier qu'on peut enlever un tag
    exercice.tags.remove(tag)
    session.commit()
    assert tag not in exercice.tags