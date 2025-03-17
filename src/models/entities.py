from flask_sqlalchemy import SQLAlchemy
from ..extensions import db


class Level(db.Model):
    """Modèle pour les niveaux scolaires"""
    __tablename__ = 'levels'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    
    # Relations
    themes = db.relationship('Theme', backref='level', lazy=True)
    tags = db.relationship('Tag', backref='level', lazy=True)
    exercices = db.relationship('Exercice', backref='level_rel', lazy=True)

    def __repr__(self):
        return f'<Level {self.name}>'


class Theme(db.Model):
    """Modèle pour les thèmes, spécifiques à un niveau"""
    __tablename__ = 'themes'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    level_id = db.Column(db.Integer, db.ForeignKey('levels.id', name='fk_theme_level'), nullable=False)
    
    # Relation avec les exercices
    exercices = db.relationship('Exercice', backref='theme_rel', lazy=True)
    
    # Contrainte d'unicité: un thème doit être unique pour un niveau donné
    __table_args__ = (db.UniqueConstraint('name', 'level_id', name='uq_theme_name_level'),)
    
    def __repr__(self):
        return f'<Theme {self.name} (Level {self.level_id})>'


class Tag(db.Model):
    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    level_id = db.Column(db.Integer, db.ForeignKey('levels.id', name='fk_tag_level'), nullable=False)  # Maintenant non nullable
    
    # Nouvelle contrainte d'unicité: un tag doit être unique pour un niveau donné
    __table_args__ = (db.UniqueConstraint('name', 'level_id', name='uq_tag_name_level'),)  # Modifié
    
    def __repr__(self):
        return f'<Tag {self.name} (Level {self.level_id})>'


# Table d'association many-to-many
exercice_tags = db.Table('exercice_tags',
    db.Column('exercice_id', db.String, db.ForeignKey('exercices.id', name='fk_exercice_tag'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id', name='fk_tag_exercice'), primary_key=True)
)

class Exercice(db.Model):

    # Alias pour compatibilité
    @property
    def level(self):
        return self.level_rel
    
    @property
    def theme(self):
        return self.theme_rel
    
    __tablename__ = 'exercices'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    level_id = db.Column(db.Integer, db.ForeignKey('levels.id', name='fk_exercice_level'), nullable=False)  # Maintenant non nullable
    theme_id = db.Column(db.Integer, db.ForeignKey('themes.id', name='fk_exercice_theme'), nullable=False)  # Maintenant non nullable
    selected = db.Column(db.Boolean, default=False)
    content = db.Column(db.Text, nullable=False)
    latex_code = db.Column(db.Text, nullable=False)
    correction = db.Column(db.Text, nullable=False)
    latex_correction = db.Column(db.Text, nullable=False)
    tags = db.relationship('Tag', secondary=exercice_tags, lazy='subquery',
                           backref=db.backref('exercices', lazy=True))
    
    # Colonnes level et theme supprimées
    
    def __repr__(self):
        return f'<Exercice {self.id}>'