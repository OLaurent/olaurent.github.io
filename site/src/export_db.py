from app import app
from models import Exercice
import json

# Créez un contexte d'application
with app.app_context():
    # Récupérez tous les exercices de la base de données
    exercices = Exercice.query.all()

    # Convertissez les exercices en une liste de dictionnaires
    exercices_data = []
    for exercice in exercices:
        exercice_data = {
            "id": exercice.id,
            "level": exercice.level,
            "theme": exercice.theme,
            "selected": exercice.selected,
            "content": exercice.content,
            "latex_code": exercice.latex_code,
            "correction": exercice.correction,
            "latex_correction": exercice.latex_correction
        }
        exercices_data.append(exercice_data)

    # Écrivez les données dans un fichier JSON
    with open('exercices.json', 'w') as json_file:
        json.dump(exercices_data, json_file, indent=4)

    print("Base de données exportée avec succès dans exercices.json !")