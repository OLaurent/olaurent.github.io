"""
Initialisation des extensions Flask sans référence à l'application.
Les extensions sont initialisées ici sans app, puis attachées à l'application 
dans create_app() avec init_app().
"""
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()