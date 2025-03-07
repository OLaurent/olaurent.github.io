from flask_sqlalchemy import SQLAlchemy
from app import db


class Exercice(db.Model):
    __tablename__ = 'exercices'

    id = db.Column(db.String, primary_key=True)
    level = db.Column(db.String, nullable=False)
    theme = db.Column(db.String, nullable=False)
    selected = db.Column(db.Boolean, default=False)
    content = db.Column(db.Text, nullable=False)
    latex_code = db.Column(db.Text, nullable=False)
    correction = db.Column(db.Text, nullable=False)
    latex_correction = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Exercice {self.id} - {self.theme}>'