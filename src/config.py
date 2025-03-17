"""
Configuration pour l'application Flask.
"""
import os

class Config:
    # Configuration de base
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
    base_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    db_path = os.path.join(base_dir, 'instance', 'exercices.db')
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{db_path}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True