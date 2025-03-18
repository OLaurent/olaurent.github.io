"""
Tests pour le modèle Tag.
"""

def test_create_tag(session):
    """Test la création d'un tag."""
    from src.models.entities import Tag, Level
    
    # Créer un niveau (nécessaire pour le tag)
    level = Level(name="Terminale")
    session.add(level)
    session.commit()
    
    # Créer un tag
    tag = Tag(name="Intégration", level_id=level.id)
    session.add(tag)
    session.commit()
    
    # Vérifications
    assert tag.id is not None
    assert tag.name == "Intégration"
    assert tag.level_id == level.id
    
    # Vérifier la relation avec le niveau
    assert tag.level == level

def test_tag_exercices_relationship(session, sample_data):
    """Test la relation many-to-many entre tags et exercices."""
    tag = sample_data['tags'][0]  # "Équations"
    exercice = sample_data['exercices'][0]
    
    # Vérifier la relation existante
    assert exercice in tag.exercices
    assert tag in exercice.tags
    
    # Ajouter un nouveau tag à l'exercice
    new_tag = sample_data['tags'][1]  # "Fonctions"
    exercice.tags.append(new_tag)
    session.commit()
    
    # Vérifier la mise à jour de la relation
    assert new_tag in exercice.tags
    assert exercice in new_tag.exercices
    
    # Vérifier qu'on peut enlever un tag
    exercice.tags.remove(new_tag)
    session.commit()
    assert new_tag not in exercice.tags
    assert exercice not in new_tag.exercices