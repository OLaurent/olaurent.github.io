"""
Tests pour les routes de gestion des exercices.
"""

import html

def test_create_exercise_route_get(client, sample_data):
    """Test que la page de création d'exercice s'affiche correctement."""
    response = client.get('/exercise/create')
    
    # Vérifier que la réponse est OK
    assert response.status_code == 200
    
    # Vérifier que le contenu HTML contient des éléments attendus
    html_content = response.data.decode('utf-8')
    assert "Créer un exercice" in html_content
    
    # Vérifier que les listes déroulantes contiennent les données
    level_name = sample_data['levels'][0].name
    theme_name = sample_data['themes'][0].name
    assert level_name in html_content
    assert theme_name in html_content

def test_create_exercise_route_post(client, sample_data):
    """Test la création d'un exercice via le formulaire."""
    level = sample_data['levels'][0]
    theme = sample_data['themes'][0]
    tag = sample_data['tags'][0]
    
    response = client.post('/exercise/create', data={
        'level_id': level.id,
        'theme_id': theme.id,
        'content': '<p>Exercice de test</p>',
        'latex_code': 'Exercice de test',
        'correction': '<p>Correction de test</p>',
        'latex_correction': 'Correction de test',
        'tags': [tag.id]
    }, follow_redirects=True)
    
    # Vérifier que la réponse est OK
    assert response.status_code == 200
    
    # Vérifier que l'exercice a été créé et apparaît sur la page d'accueil
    html_content = response.data.decode('utf-8')
    assert 'Exercice de test' in html_content
    assert 'Exercice créé avec succès' in html_content

def test_edit_exercise_route_get(client, sample_data):
    """Test que la page d'édition d'exercice s'affiche correctement."""
    exercice = sample_data['exercices'][0]
    
    response = client.get(f'/exercise/edit/{exercice.id}')
    
    # Vérifier que la réponse est OK
    assert response.status_code == 200

    # Vérifier que le contenu HTML contient les données de l'exercice
    html_content = response.data.decode('utf-8')
    
    # Remplacer les entités HTML pour l'apostrophe
    html_content = html_content.replace('&#39;', '&#x27;')
    
    assert html.escape(exercice.content).replace('<p>', '').replace('</p>', '') in html_content
    assert html.escape(exercice.latex_code) in html_content
    
    # Vérifier que les listes déroulantes contiennent les bonnes valeurs sélectionnées
    level_name = sample_data['levels'][0].name
    theme_name = sample_data['themes'][0].name
    assert f'value="{exercice.level_id}" selected' in html_content
    assert f'value="{exercice.theme_id}" selected' in html_content

def test_delete_exercise_route(client, sample_data, session):
    """Test la suppression d'un exercice."""
    exercice = sample_data['exercices'][0]
    
    response = client.post('/exercise/delete', data={
        'id': exercice.id
    }, follow_redirects=True)
    
    # Vérifier que la réponse est OK
    assert response.status_code == 200
    
    # Vérifier que l'exercice a été supprimé
    from src.models.entities import Exercice
    deleted_exercice = session.get(Exercice, exercice.id)
    assert deleted_exercice is None
    
    # Vérifier le message de confirmation
    html_content = response.data.decode('utf-8')

    # Remplacer les entités HTML pour l'apostrophe
    html_content = html_content.replace('&#39;', '&#x27;')

    print(html_content)
    assert 'Exercice supprimé avec succès' in html_content