from flask_sqlalchemy import SQLAlchemy
from app import db


class Tag(db.Model):
    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)

    def __repr__(self):
        return f'<Tag {self.name}>'

# Table d'association many-to-many
exercice_tags = db.Table('exercice_tags',
    db.Column('exercice_id', db.Integer, db.ForeignKey('exercices.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'), primary_key=True)
)

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
    tags = db.relationship('Tag', secondary=exercice_tags, lazy='subquery',
                           backref=db.backref('exercices', lazy=True))

    def __repr__(self):
        return f'<Exercice {self.id} - {self.theme}>'