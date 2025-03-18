"""
Tests pour les routes d'exportation d'exercices.
"""
import json
import pytest

def test_select_exercise_route(client, sample_data):
    """Test la sélection/désélection d'un exercice."""
    exercice = sample_data['exercices'][0]
    
    # Tester la sélection d'un exercice
    response = client.post('/export/select', data={
        'id': str(exercice.id)
    }, follow_redirects=True)
    
    # Vérifier que la réponse est OK
    assert response.status_code == 200
    
    # Vérifier que l'exercice est maintenant dans la session
    with client.session_transaction() as session:
        selected = session.get('selected_exercises', [])
        assert str(exercice.id) in selected
    
    # Tester la désélection de l'exercice (deuxième appel)
    response = client.post('/export/select', data={
        'id': str(exercice.id)
    }, follow_redirects=True)
    
    # Vérifier que la réponse est OK
    assert response.status_code == 200
    
    # Vérifier que l'exercice n'est plus dans la session
    with client.session_transaction() as session:
        selected = session.get('selected_exercises', [])
        assert str(exercice.id) not in selected

def test_export_menu_route_no_selection(client):
    """Test que le menu d'export affiche un message quand aucun exercice n'est sélectionné."""
    # Initialiser une session vide
    with client.session_transaction() as sess:
        sess['selected_exercises'] = []
    
    response = client.get('/export/menu')
    assert response.status_code == 400
    assert b"Aucun exercice s\xc3\xa9lectionn\xc3\xa9" in response.data  # "Aucun exercice sélectionné" en UTF-8

def test_export_menu_route_with_selection(session_with_exercises):
    """Test que le menu d'export affiche le formulaire quand des exercices sont sélectionnés."""
    response = session_with_exercises.get('/export/menu')
    assert response.status_code == 200
    assert b"export.html" in response.data or b"format" in response.data  # Vérifie que le template ou un élément du template est présent

def test_export_exercises_route_no_selection(client):
    """Test l'export sans exercices sélectionnés."""
    # Initialiser une session vide
    with client.session_transaction() as sess:
        sess['selected_exercises'] = []
    
    response = client.get('/export/exercises')
    assert response.status_code == 400
    assert b"Aucun exercice s\xc3\xa9lectionn\xc3\xa9" in response.data

def test_export_exercises_route_with_selection(session_with_exercises):
    """Test l'export avec des exercices sélectionnés."""
    response = session_with_exercises.get('/export/exercises')
    assert response.status_code == 200
    # Vérifier qu'il s'agit d'un téléchargement
    assert response.headers['Content-Disposition'].startswith('attachment; filename=')

def test_export_exercises_json(client, sample_data):
    """Test l'exportation des exercices au format JSON."""
    exercice = sample_data['exercices'][0]
    
    # Sélectionner un exercice
    with client.session_transaction() as session:
        session['selected_exercises'] = [str(exercice.id)]
    
    response = client.get('/export/exercises?format=json')
    
    # Vérifier que la réponse a le bon type de contenu
    assert response.headers['Content-Type'] == 'application/json'
    assert 'attachment; filename=selected_exercises.json' in response.headers['Content-Disposition']
    
    # Essayer de charger le JSON
    content = response.data.decode('utf-8')
    data = json.loads(content)
    
    # Vérifier que le JSON contient les données de l'exercice
    assert len(data) == 1
    assert data[0]['id'] == exercice.id
    assert data[0]['content'] == exercice.content