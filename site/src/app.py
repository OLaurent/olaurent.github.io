from flask import Flask, render_template, request, redirect, url_for, session, send_file
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
import os
import json
import uuid

app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///exercices.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'  # Nécessaire pour utiliser flash messages
db = SQLAlchemy(app)

from models import Exercice

@app.route('/')
def home():
    exercices = Exercice.query.all()
    selected_exercises = session.get('selected_exercises', [])
    return render_template('index.html', exercices=exercices, selected_exercises=selected_exercises)


@app.route('/edit_exercise', methods=['GET', 'POST'])
def edit_exercise():
    if request.method == 'POST':
        # Traitement du formulaire
        exercice_id = request.form.get('id')
        exercice = Exercice.query.get(exercice_id)
        if exercice is None:
            print('Exercice non trouvé.')
            return redirect(url_for('home'))

        exercice.level = request.form.get('level')
        exercice.theme = request.form.get('theme')
        exercice.content = request.form.get('content')
        exercice.latex_code = request.form.get('latex_code')
        exercice.correction = request.form.get('correction')
        exercice.latex_correction = request.form.get('latex_correction')
        db.session.commit()
        return redirect(url_for('home'))
    else:
        exercice_id = request.args.get('id')
        exercice = Exercice.query.get(exercice_id)
        if exercice is None:
            return redirect(url_for('home'))
        return render_template('edit_exercise.html', exercice=exercice)


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
        # Création d'un nouvel exercice
        new_exercice = Exercice(
            id=str(uuid.uuid4()),
            level=request.form.get('level'),
            theme=request.form.get('theme'),
            content=request.form.get('content'),
            latex_code=request.form.get('latex_code', ''),
            correction=request.form.get('correction', ''),
            latex_correction=request.form.get('latex_correction', '')
        )
        db.session.add(new_exercice)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        # Récupérer tous les thèmes existants
        existing_themes = db.session.query(Exercice.theme).distinct().all()
        unique_themes = sorted([theme[0] for theme in existing_themes])
        
        # Afficher le formulaire de création
        return render_template('create_exercise.html', themes=unique_themes)

if __name__ == '__main__':
    app.run(debug=True)