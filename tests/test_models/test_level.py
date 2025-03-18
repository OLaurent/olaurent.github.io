"""
Tests pour le modèle Level.
"""

def test_create_level(session):
    """Test la création d'un niveau."""
    from src.models.entities import Level
    
    # Créer un niveau
    level = Level(name="Terminale")
    session.add(level)
    session.commit()
    
    # Vérifications
    assert level.id is not None
    assert level.name == "Terminale"
    
    # Vérifier qu'on peut récupérer le niveau depuis la base de données
    level_from_db = session.query(Level).filter_by(name="Terminale").first()
    assert level_from_db is not None
    assert level_from_db.id == level.id

def test_level_themes_relationship(session, sample_data):
    """Test la relation one-to-many entre niveaux et thèmes."""
    level = sample_data['levels'][0]  # "Seconde"
    themes = [t for t in sample_data['themes'] if t.level_id == level.id]
    
    # Vérifier qu'il y a des thèmes associés au niveau
    assert len(themes) > 0
    
    # Vérifier la relation
    for theme in themes:
        assert theme in level.themes
        assert theme.level == level

def test_level_tags_relationship(session, sample_data):
    """Test la relation one-to-many entre niveaux et tags."""
    level = sample_data['levels'][0]  # "Seconde"
    tags = [t for t in sample_data['tags'] if t.level_id == level.id]
    
    # Vérifier qu'il y a des tags associés au niveau
    assert len(tags) > 0
    
    # Vérifier la relation
    for tag in tags:
        assert tag in level.tags
        assert tag.level == level

def test_level_exercices_relationship(session, sample_data):
    """Test la relation indirecte entre niveaux et exercices."""
    level = sample_data['levels'][0]  # "Seconde"
    exercices = [e for e in sample_data['exercices'] if e.level_id == level.id]
    
    # Vérifier qu'il y a des exercices associés au niveau
    assert len(exercices) > 0
    
    # Vérifier la relation
    for exercice in exercices:
        assert exercice.level == level