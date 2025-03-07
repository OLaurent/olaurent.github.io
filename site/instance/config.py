from os import environ

class Config:
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL') or 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = environ.get('SECRET_KEY') or 'your_secret_key'