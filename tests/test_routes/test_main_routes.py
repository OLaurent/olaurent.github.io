"""
Tests pour les routes principales de l'application.
"""

def test_home_route(client):
    """Test que la page d'accueil s'affiche correctement."""
    response = client.get('/')
    
    # Vérifier que la réponse est OK
    assert response.status_code == 200
    
    # Vérifier que le contenu HTML contient des éléments attendus
    html_content = response.data.decode('utf-8')


    # Remplacer les entités HTML pour l'apostrophe
    html_content = html_content.replace('&#39;', '&#x27;')

    assert "Accueil" in html_content

def test_home_route_with_data(client, sample_data):
    """Test que la page d'accueil affiche les données correctement."""
    response = client.get('/')
    
    # Vérifier que la réponse est OK
    assert response.status_code == 200
    
    # Vérifier que le contenu HTML contient les exercices
    html_content = response.data.decode('utf-8')
    for exercice in sample_data['exercices']:
        # Les données de l'exercice devraient être dans le HTML d'une façon ou d'une autre
        assert exercice.content.replace('<p>', '').replace('</p>', '') in html_content or \
               str(exercice.id) in html_content

def test_manage_metadata_route(client):
    """Test que la page de gestion des métadonnées s'affiche correctement."""
    response = client.get('/manage_metadata')
    
    # Vérifier que la réponse est OK
    assert response.status_code == 200
    
    # Vérifier que le contenu HTML contient des éléments attendus
    html_content = response.data.decode('utf-8')


    # Remplacer les entités HTML pour l'apostrophe
    html_content = html_content.replace('&#39;', '&#x27;')

    assert "Gestion des métadonnées" in html_content
    
def test_manage_metadata_add_level(client):
    """Test l'ajout d'un niveau via le formulaire."""
    response = client.post('/manage_metadata', data={
        'action': 'add_level',
        'level_name': 'Nouveau Niveau Test'
    }, follow_redirects=True)
    
    # Vérifier que la réponse est OK
    assert response.status_code == 200
    
    # Vérifier que le nouveau niveau apparaît dans la page
    html_content = response.data.decode('utf-8')
    assert 'Nouveau Niveau Test' in html_content