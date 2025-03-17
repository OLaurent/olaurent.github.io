from flask import Flask, render_template, request, redirect, url_for, session, send_file, flash
import sys
import os

# Ajouter le répertoire courant au chemin Python
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

"""
This module defines the main routes for the Flask web application.
Routes:
    - /: Home page that displays all exercises and selected exercises.
    - /edit_exercise: Route to edit an existing exercise. Supports GET and POST methods.
    - /select_exercise: Route to select or deselect an exercise. Supports POST method.
    - /export_menu: Route to display the export menu for selected exercises.
    - /export_exercises: Route to export selected exercises in JSON or LaTeX format. Supports GET method.
    - /create_exercise: Route to create a new exercise. Supports GET and POST methods.
"""
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Configuration
app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///exercices.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'  # Nécessaire pour utiliser flash messages

# Initialiser la base de données
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Importer les modèles après la création de db
from models.entities import Exercice, Tag, Level, Theme

# Importer les routes
from routes.main_routes import *
from routes.exercise_routes import *
from routes.export_routes import *

if __name__ == '__main__':
    app.run(debug=True)