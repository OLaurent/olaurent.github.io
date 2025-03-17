from flask import Flask, render_template, request, redirect, url_for, session, send_file, flash
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
import os
import json
import uuid

app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///exercices.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'  # Nécessaire pour utiliser flash messages
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Exercice, Tag, Level, Theme
from docx_exporter import DocxExporter

@app.route('/')
def home():  

    exercices = Exercice.query.all()
    selected_exercises = [ex.id for ex in Exercice.query.filter_by(selected=True).all()]
    levels = Level.query.order_by(Level.name).all()
    return render_template('index.html', exercices=exercices, selected_exercises=selected_exercises, levels=levels)


@app.route('/edit_exercise', methods=['GET', 'POST'])
def edit_exercise():
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
            return redirect(url_for('home'))
    else:
        exercice_id = request.args.get('id')
        exercice = Exercice.query.get(exercice_id)
        if not exercice:
            return redirect(url_for('home'))
        
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


@app.route('/select_exercise', methods=['POST'])
def select_exercise():
    exercice_id = request.form.get('id')
    print('Exercice sélectionné:', exercice_id)
    selected_exercises = session.get('selected_exercises', [])
    if exercice_id in selected_exercises:
        selected_exercises.remove(exercice_id)
    else:
        selected_exercises.append(exercice_id)
    session['selected_exercises'] = selected_exercises

    print('Exercices sélectionnés:', selected_exercises)
    return redirect(url_for('home'))


@app.route('/export_menu')
def export_menu():
    selected_exercises = session.get('selected_exercises', [])
    if not selected_exercises:
        return "Aucun exercice sélectionné", 400

    exercices = Exercice.query.filter(Exercice.id.in_(selected_exercises)).all()
    return render_template('export.html', exercices=exercices)

@app.route('/export_exercises', methods=['GET'])
def export_exercises():
    selected_exercises = session.get('selected_exercises', [])
    if not selected_exercises:
        return "Aucun exercice sélectionné", 400

    exercices = Exercice.query.filter(Exercice.id.in_(selected_exercises)).all()
    exercices_data = [
        {
            'id': exercice.id,
            'level': exercice.level,
            'theme': exercice.theme,
            'content': exercice.content,
            'latex_code': exercice.latex_code,
            'correction': exercice.correction,
            'latex_correction': exercice.latex_correction
        }
        for exercice in exercices
    ]

    export_format = request.args.get('format', 'json')
    if export_format == 'tex':
        export_file_path = '/tmp/selected_exercises.tex'
        with open(export_file_path, 'w') as export_file:
            for exercice in exercices_data:
                export_file.write(f"\\section*{{{exercice['level']} - {exercice['theme']}}}\n")
                export_file.write(f"{exercice['content']}\n\n")
                export_file.write(f"\\subsection*{{Correction}}\n")
                export_file.write(f"{exercice['correction']}\n\n")
    elif export_format == 'docx':
        export_file_path = '/tmp/selected_exercises.docx'
        exporter = DocxExporter(exercices_data)
        exporter.export(export_file_path)
    else:
        export_file_path = '/tmp/selected_exercises.json'
        with open(export_file_path, 'w') as export_file:
            json.dump(exercices_data, export_file)

    return send_file(export_file_path, as_attachment=True, download_name=f'selected_exercises.{export_format}')


@app.route('/delete_exercise', methods=['POST'])
def delete_exercise():
    exercice_id = request.form.get('id')
    exercice = Exercice.query.get(exercice_id)
    if exercice:
        db.session.delete(exercice)
        db.session.commit()
        print(f'Exercice {exercice_id} supprimé.')
    else:
        print(f'Exercice {exercice_id} non trouvé.')
    return redirect(url_for('home'))


@app.route('/create_exercise', methods=['GET', 'POST'])
def create_exercise():
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
        return redirect(url_for('home'))

    # Pour la méthode GET, afficher le formulaire
    levels = Level.query.order_by(Level.name).all()
    themes = Theme.query.order_by(Theme.name).all()
    all_tags = Tag.query.order_by(Tag.name).all()
    
    return render_template('create_exercise.html', levels=levels, themes=themes, all_tags=all_tags)

@app.route('/manage_metadata', methods=['GET', 'POST'])
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
        return redirect(url_for('manage_metadata'))
    
    # Récupération des thèmes et tags par niveau pour l'affichage
    level_data = {}
    for level in levels:
        level_data[level.id] = {
            'name': level.name,
            'themes': Theme.query.filter_by(level_id=level.id).order_by(Theme.name).all(),
            'tags': Tag.query.filter_by(level_id=level.id).order_by(Tag.name).all()
        }
    
    return render_template('manage_metadata.html', levels=levels, level_data=level_data)

if __name__ == '__main__':
    app.run(debug=True)