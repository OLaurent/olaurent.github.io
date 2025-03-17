from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from ..extensions import db
from ..models.entities import Exercice, Tag, Level, Theme

exercise_bp = Blueprint('exercise', __name__, url_prefix='/exercise')

@exercise_bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        # Récupération des données du formulaire
        level_id = request.form.get('level_id')
        theme_id = request.form.get('theme_id')
        content = request.form.get('content')
        latex_code = request.form.get('latex_code')
        correction = request.form.get('correction')
        latex_correction = request.form.get('latex_correction')
        tag_ids = request.form.getlist('tags')
        
        # Créer le nouvel exercice
        new_exercise = Exercice(
            level_id=level_id,
            theme_id=theme_id,
            content=content,
            latex_code=latex_code,
            correction=correction,
            latex_correction=latex_correction
        )
        
        db.session.add(new_exercise)
        db.session.commit()
        
        # Ajouter les tags à l'exercice
        for tag_id in tag_ids:
            tag = Tag.query.get(tag_id)
            if tag:
                new_exercise.tags.append(tag)
        
        db.session.commit()
        flash('Exercice créé avec succès!', 'success')
        return redirect(url_for('main.home'))

    # Pour la méthode GET, afficher le formulaire
    levels = Level.query.order_by(Level.name).all()
    themes = Theme.query.order_by(Theme.name).all()
    all_tags = Tag.query.order_by(Tag.name).all()
    
    return render_template('create_exercise.html', levels=levels, themes=themes, all_tags=all_tags)

@exercise_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    if request.method == 'POST':
        # Récupération des données du formulaire
        exercice_id = request.form.get('id')
        level_id = request.form.get('level_id')
        theme_id = request.form.get('theme_id')
        content = request.form.get('content')
        latex_code = request.form.get('latex_code')
        correction = request.form.get('correction')
        latex_correction = request.form.get('latex_correction')
        tag_ids = request.form.getlist('tags')
        
        # Mise à jour de l'exercice
        exercice = Exercice.query.get(exercice_id)
        if exercice:
            exercice.level_id = level_id
            exercice.theme_id = theme_id
            exercice.content = content
            exercice.latex_code = latex_code
            exercice.correction = correction
            exercice.latex_correction = latex_correction
            
            # Mise à jour des tags
            exercice.tags.clear()
            for tag_id in tag_ids:
                tag = Tag.query.get(tag_id)
                if tag:
                    exercice.tags.append(tag)
            
            db.session.commit()
            return redirect(url_for('main.home'))
    else:
        exercice_id = request.args.get('id')
        exercice = Exercice.query.get(exercice_id)
        if not exercice:
            return redirect(url_for('main.home'))
        
        levels = Level.query.all()
        themes = Theme.query.all()
        all_tags = Tag.query.all()
        exercice_tag_ids = [tag.id for tag in exercice.tags]
        
        return render_template('edit_exercise.html', 
                               exercice=exercice, 
                               levels=levels, 
                               themes=themes, 
                               all_tags=all_tags,
                               exercice_tag_ids=exercice_tag_ids)

@exercise_bp.route('/delete_exercise', methods=['POST'])
def delete_exercise():
    exercice_id = request.form.get('id')
    exercice = Exercice.query.get(exercice_id)
    if exercice:
        db.session.delete(exercice)
        db.session.commit()
        print(f'Exercice {exercice_id} supprimé.')
    else:
        print(f'Exercice {exercice_id} non trouvé.')
    return redirect(url_for('main.home'))


# Autres routes liées aux exercices...