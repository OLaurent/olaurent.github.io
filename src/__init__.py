from flask import Flask
from .extensions import db, migrate
from .config import Config

def create_app(test_config=None):
    """
    Factory function qui crée et configure l'application Flask.
    """
    app = Flask(__name__)
    
    # Utiliser la configuration de test si elle est fournie, sinon utiliser Config
    if test_config:
        app.config.from_mapping(test_config)
    else:
        app.config.from_object(Config)
    
    # Initialiser les extensions
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Enregistrer les blueprints
    from .routes.main_routes import main_bp
    from .routes.exercise_routes import exercise_bp
    from .routes.export_routes import export_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(exercise_bp)
    app.register_blueprint(export_bp)
    
    return app