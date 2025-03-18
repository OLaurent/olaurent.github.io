"""
Tests pour la classe LatexExporter.
"""
import os
import tempfile

def test_latex_exporter_init(sample_data):
    """Test l'initialisation de l'exportateur LaTeX."""
    from src.exporters.latex_exporter import LatexExporter
    
    # Préparer les données
    exercices_data = [
        {
            'id': exercice.id,
            'level': exercice.level,
            'theme': exercice.theme,
            'content': exercice.content,
            'latex_code': exercice.latex_code,
            'correction': exercice.correction,
            'latex_correction': exercice.latex_correction,
            'tags': exercice.tags
        }
        for exercice in sample_data['exercices']
    ]
    
    # Créer l'exportateur
    exporter = LatexExporter(exercices_data)
    
    # Vérifier que l'exportateur contient les exercices
    assert exporter.exercises == exercices_data
    assert len(exporter.exercises) == len(sample_data['exercices'])

def test_latex_exporter_export(sample_data):
    """Test l'exportation LaTeX."""
    from src.exporters.latex_exporter import LatexExporter
    
    # Préparer les données
    exercices_data = [
        {
            'id': exercice.id,
            'level': exercice.level,
            'theme': exercice.theme,
            'content': exercice.content,
            'latex_code': exercice.latex_code,
            'correction': exercice.correction,
            'latex_correction': exercice.latex_correction,
            'tags': exercice.tags
        }
        for exercice in sample_data['exercices']
    ]
    
    # Créer un fichier temporaire pour le test
    with tempfile.NamedTemporaryFile(suffix='.tex', delete=False) as temp_file:
        temp_path = temp_file.name
    
    try:
        # Exporter les exercices
        exporter = LatexExporter(exercices_data)
        exporter.export(temp_path, include_corrections=True)
        
        # Vérifier que le fichier a été créé
        assert os.path.exists(temp_path)
        
        # Vérifier le contenu du fichier
        with open(temp_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
            # Vérifier la structure LaTeX
            assert '\\documentclass' in content
            assert '\\begin{document}' in content
            assert '\\end{document}' in content
            
            # Vérifier que les exercices sont présents
            for exercice in sample_data['exercices']:
                # On vérifie soit le contenu LaTeX si disponible, soit un extrait du contenu HTML
                if exercice.latex_code and exercice.latex_code.strip():
                    assert exercice.latex_code in content
                else:
                    # Vérifier au moins que le texte principal est présent
                    plaintext = exercice.content.replace('<p>', '').replace('</p>', '')
                    assert plaintext in content or exporter._clean_latex(plaintext) in content
                
            # Vérifier que les corrections sont présentes
            assert '\\section{Corrections}' in content
            
    finally:
        # Nettoyer le fichier temporaire
        if os.path.exists(temp_path):
            os.unlink(temp_path)