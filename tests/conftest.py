import os
import pytest
import sys

# Ajouter le répertoire parent au sys.path pour permettre d'importer les modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src import create_app
from src.extensions import db as _db
from src.models.entities import Exercice, Level, Theme, Tag

@pytest.fixture(scope="session")
def app():
    """Create and configure a Flask app for testing."""
    # Configuration de test explicite avec SECRET_KEY pour les sessions
    test_config = {
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:',
        'SQLALCHEMY_TRACK_MODIFICATIONS': False,
        'WTF_CSRF_ENABLED': False,
        'SECRET_KEY': 'test_secret_key',  # Ajout de la clé secrète
        'SERVER_NAME': 'localhost.localdomain'  # Pour permettre d'accéder aux URL
    }
    
    test_app = create_app(test_config)
    
    # Établir le contexte d'application pour les tests
    with test_app.app_context():
        # Créer les tables avant de commencer les tests
        _db.create_all()
        yield test_app
        # Nettoyer après les tests
        _db.session.remove()
        _db.drop_all()

@pytest.fixture(scope="function")
def db(app):
    """Fournit une interface à la base de données de test."""
    return _db

@pytest.fixture(scope="function")
def session(db):
    """Create a new database session for a test."""
    connection = db.engine.connect()
    transaction = connection.begin()
    
    # Options qui assurent que les sessions sont scoped au test
    options = dict(bind=connection, binds={})
    session = db._make_scoped_session(options=options)
    
    # Remplacer la session de db par notre session de test
    old_session = db.session
    db.session = session
    
    yield session
    
    # Nettoyer après le test
    transaction.rollback()
    connection.close()
    session.remove()
    db.session = old_session

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

@pytest.fixture
def sample_data(session):
    """Insert sample data for testing."""
    # Nettoyage plus complet incluant les associations many-to-many
    try:
        # Nettoyer les relations many-to-many d'abord
        session.execute(Exercice.__table__.delete())
        association_table = Exercice.tags.prop.secondary
        session.execute(association_table.delete())
        session.execute(Tag.__table__.delete())
        session.execute(Theme.__table__.delete())
        session.execute(Level.__table__.delete())
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Erreur lors du nettoyage des données: {e}")

    # Créer des niveaux
    level1 = Level(name="Seconde")
    level2 = Level(name="Première")
    session.add_all([level1, level2])
    session.flush()
    
    # Créer des thèmes
    theme1 = Theme(name="Algèbre", level_id=level1.id)
    theme2 = Theme(name="Géométrie", level_id=level1.id)
    theme3 = Theme(name="Probabilités", level_id=level2.id)
    session.add_all([theme1, theme2, theme3])
    session.flush()
    
    # Créer des tags
    tag1 = Tag(name="Équations", level_id=level1.id)
    tag2 = Tag(name="Fonctions", level_id=level1.id)
    tag3 = Tag(name="Vecteurs", level_id=level2.id)
    session.add_all([tag1, tag2, tag3])
    session.flush()
    
    # Créer des exercices
    exercice1 = Exercice(
        level_id=level1.id,
        theme_id=theme1.id,
        content="<p>Résoudre l'équation suivante: $x^2-4=0$</p>",
        latex_code="Résoudre l'équation suivante: $x^2-4=0$",
        correction="<p>Les solutions sont $x=2$ et $x=-2$</p>",
        latex_correction="Les solutions sont $x=2$ et $x=-2$"
    )
    
    exercice2 = Exercice(
        level_id=level2.id,
        theme_id=theme3.id,
        content="<p>Calculer la probabilité de l'événement A.</p>",
        latex_code="Calculer la probabilité de l'événement A.",
        correction="<p>La probabilité de A est 0.5</p>",
        latex_correction="La probabilité de A est 0.5"
    )
    
    # Ajouter les exercices à la base de données d'abord
    session.add_all([exercice1, exercice2])
    session.flush()
    
    # Puis ajouter les relations tags APRÈS le flush
    exercice1.tags.append(tag1)
    exercice2.tags.append(tag3)
    
    session.commit()
    
    return {
        'levels': [level1, level2],
        'themes': [theme1, theme2, theme3],
        'tags': [tag1, tag2, tag3],
        'exercices': [exercice1, exercice2]
    }

@pytest.fixture
def captured_templates(app):
    """Capture les templates rendus par Flask pendant les tests."""
    recorded = []
    
    def record(sender, template, context, **extra):
        recorded.append((template, context))
    
    from flask import template_rendered
    template_rendered.connect(record, app)
    
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)

@pytest.fixture
def session_with_exercises(client, sample_data):
    """Initialise une session avec des exercices sélectionnés."""
    with client.session_transaction() as sess:
        sess['selected_exercises'] = [str(sample_data['exercices'][0].id)]
    return client