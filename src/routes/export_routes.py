from flask import render_template, request, redirect, url_for, flash, session, send_file, Blueprint
from ..extensions import db  # Import relatif vers les extensions
import json
import os
from ..models.entities import Exercice  # Import relatif vers les modèles
from ..exporters.latex_exporter import LatexExporter  # Import relatif vers les exporters
from ..exporters.docx_exporter import DocxExporter

export_bp = Blueprint('export', __name__, url_prefix='/export')

# Modifié: utiliser le blueprint au lieu de app
@export_bp.route('/select', methods=['POST'])  # URL sera /export/select
def select():
    exercice_id = request.form.get('id')
    print('Exercice sélectionné:', exercice_id)
    selected_exercises = session.get('selected_exercises', [])
    if exercice_id in selected_exercises:
        selected_exercises.remove(exercice_id)
    else:
        selected_exercises.append(exercice_id)
    session['selected_exercises'] = selected_exercises

    print('Exercices sélectionnés:', selected_exercises)
    return redirect(url_for('main.home'))  # Notez le 'main.home' pour référencer la route du blueprint main

@export_bp.route('/menu')  # URL sera /export/menu
def menu():
    selected_exercises = session.get('selected_exercises', [])
    if not selected_exercises:
        return "Aucun exercice sélectionné", 400

    exercices = Exercice.query.filter(Exercice.id.in_(selected_exercises)).all()
    return render_template('export.html', exercices=exercices)

@export_bp.route('/exercises')  # URL sera /export/exercises
def exercises():
    selected_exercises = session.get('selected_exercises', [])
    if not selected_exercises:
        return "Aucun exercice sélectionné", 400

    # Récupérer les exercices sélectionnés avec leurs relations
    exercices = Exercice.query.filter(Exercice.id.in_(selected_exercises)).all()
    
    # Préparer les données pour l'exportation en utilisant les relations correctes
    exercices_data = [
        {
            'id': exercice.id,
            'level': exercice.level,  # Assurez-vous que c'est le bon nom de relation
            'theme': exercice.theme,  # Assurez-vous que c'est le bon nom de relation
            'content': exercice.content,
            'latex_code': exercice.latex_code,
            'correction': exercice.correction,
            'latex_correction': exercice.latex_correction,
            'tags': exercice.tags  # Liste d'objets Tag
        }
        for exercice in exercices
    ]

    export_format = request.args.get('format', 'json')
    include_corrections = request.args.get('include_corrections', 'true').lower() == 'true'
    
    # Exporter selon le format demandé
    if export_format == 'tex':
        export_file_path = '/tmp/selected_exercises.tex'
        exporter = LatexExporter(exercices_data)
        exporter.export(export_file_path, include_corrections=include_corrections)
    elif export_format == 'docx':
        export_file_path = '/tmp/selected_exercises.docx'
        exporter = DocxExporter(exercices_data)
        exporter.export(export_file_path, include_corrections=include_corrections)
    else:  # Format JSON par défaut
        export_file_path = '/tmp/selected_exercises.json'
        # Pour JSON, convertir les objets en dictionnaires
        json_data = [
            {
                'id': ex['id'],
                'level': ex['level'].name,
                'level_id': ex['level'].id,
                'theme': ex['theme'].name,
                'theme_id': ex['theme'].id,
                'content': ex['content'],
                'latex_code': ex['latex_code'],
                'correction': ex['correction'],
                'latex_correction': ex['latex_correction'],
                'tags': [{'id': tag.id, 'name': tag.name} for tag in ex['tags']]
            }
            for ex in exercices_data
        ]
        with open(export_file_path, 'w', encoding='utf-8') as export_file:
            json.dump(json_data, export_file, ensure_ascii=False, indent=2)

    return send_file(export_file_path, as_attachment=True, download_name=f'selected_exercises.{export_format}')