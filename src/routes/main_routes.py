from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from ..extensions import db
from ..models.entities import Exercice, Tag, Level, Theme

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():  
    exercices = Exercice.query.all()
    selected_exercises = [ex.id for ex in Exercice.query.filter_by(selected=True).all()]
    levels = Level.query.order_by(Level.name).all()
    return render_template('index.html', exercices=exercices, selected_exercises=selected_exercises, levels=levels)

@main_bp.route('/manage_metadata', methods=['GET', 'POST'])
def manage_metadata():
    # Récupération de tous les niveaux
    levels = Level.query.order_by(Level.name).all()
    
    if request.method == 'POST':
        action = request.form.get('action')
        
        # Ajout d'un nouveau niveau
        if action == 'add_level':
            level_name = request.form.get('level_name')
            if level_name and not Level.query.filter_by(name=level_name).first():
                new_level = Level(name=level_name)
                db.session.add(new_level)
                db.session.commit()
        
        # Ajout d'un nouveau thème
        elif action == 'add_theme':
            theme_name = request.form.get('theme_name')
            level_id = request.form.get('level_id')
            if theme_name and level_id:
                # Vérifier si le thème existe déjà pour ce niveau
                existing_theme = Theme.query.filter_by(name=theme_name, level_id=level_id).first()
                if not existing_theme:
                    new_theme = Theme(name=theme_name, level_id=level_id)
                    db.session.add(new_theme)
                    db.session.commit()
        
        # Ajout d'un nouveau tag
        elif action == 'add_tag':
            tag_name = request.form.get('tag_name')
            level_id = request.form.get('level_id')
            if tag_name and level_id:
                # Vérifier si le tag existe déjà pour ce niveau
                existing_tag = Tag.query.filter_by(name=tag_name, level_id=level_id).first()
                if not existing_tag:
                    new_tag = Tag(name=tag_name, level_id=level_id)
                    db.session.add(new_tag)
                    db.session.commit()
        
        # Suppression d'un thème
        elif action == 'delete_theme':
            theme_id = request.form.get('theme_id')
            if theme_id:
                theme_to_delete = Theme.query.get(theme_id)
                if theme_to_delete:
                    # Vérifier si ce thème est utilisé par des exercices
                    exercises_with_theme = Exercice.query.filter_by(theme_id=theme_id).count()
                    if exercises_with_theme == 0:
                        db.session.delete(theme_to_delete)
                        db.session.commit()
                        flash('Thème supprimé avec succès.', 'success')
                    else:
                        flash(f'Impossible de supprimer ce thème car il est utilisé par {exercises_with_theme} exercice(s).', 'danger')
        
        # Suppression d'un tag
        elif action == 'delete_tag':
            tag_id = request.form.get('tag_id')
            if tag_id:
                tag_to_delete = Tag.query.get(tag_id)
                if tag_to_delete:
                    # Vérifier d'abord si le tag est associé à des exercices
                    if not tag_to_delete.exercices:
                        # Le tag n'est pas utilisé, on peut le supprimer
                        db.session.delete(tag_to_delete)
                        db.session.commit()
                        flash('Tag supprimé avec succès.', 'success')
                    else:
                        # Option 1: Ne pas supprimer et afficher un message
                        flash(f'Impossible de supprimer ce tag car il est utilisé par {len(tag_to_delete.exercices)} exercice(s).', 'danger')
                        
                        # Option 2: Détacher le tag des exercices puis le supprimer
                        # force_delete = request.form.get('force_delete') == 'true'
                        # if force_delete:
                        #     for exercice in list(tag_to_delete.exercices):
                        #         exercice.tags.remove(tag_to_delete)
                        #     db.session.delete(tag_to_delete)
                        #     db.session.commit()
                        #     flash('Tag détaché des exercices et supprimé avec succès.', 'success')
        
        # Redirection pour éviter de resoumettre le formulaire lors d'un rafraîchissement
        return redirect(url_for('main.manage_metadata'))
    
    # Récupération des thèmes et tags par niveau pour l'affichage
    level_data = {}
    for level in levels:
        level_data[level.id] = {
            'name': level.name,
            'themes': Theme.query.filter_by(level_id=level.id).order_by(Theme.name).all(),
            'tags': Tag.query.filter_by(level_id=level.id).order_by(Tag.name).all()
        }
    
    return render_template('manage_metadata.html', levels=levels, level_data=level_data)