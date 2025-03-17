import re
import html
from collections import defaultdict

# Imports relatifs si nécessaire
from ..models.entities import Exercice

class LatexExporter:
    """
    Classe pour exporter des exercices au format LaTeX.
    
    Attributs:
        exercises (list): Liste des exercices à exporter.
    """
    
    def __init__(self, exercises):
        """
        Initialise l'exportateur LaTeX avec une liste d'exercices.
        
        Args:
            exercises (list): Liste de dictionnaires contenant les données des exercices.
        """
        self.exercises = exercises
    
    def export(self, output_path, include_corrections=True):
        """
        Exporte les exercices dans un fichier LaTeX.
        
        Args:
            output_path (str): Chemin du fichier de sortie.
            include_corrections (bool): Indique si les corrections doivent être incluses.
        """
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(self._generate_latex_document(include_corrections))
    
    def _generate_latex_document(self, include_corrections):
        """
        Génère le contenu du document LaTeX.
        
        Args:
            include_corrections (bool): Indique si les corrections doivent être incluses.
            
        Returns:
            str: Contenu du document LaTeX.
        """
        # Organiser les exercices par niveau et thème
        exercises_by_level = defaultdict(lambda: defaultdict(list))
        
        for exercise in self.exercises:
            level_name = exercise['level'].name if hasattr(exercise['level'], 'name') else str(exercise['level'])
            theme_name = exercise['theme'].name if hasattr(exercise['theme'], 'name') else str(exercise['theme'])
            exercises_by_level[level_name][theme_name].append(exercise)
        
        # Générer le préambule LaTeX
        document = self._generate_preamble()
        
        # Générer la section des exercices
        document += "\\begin{document}\n\n"
        document += "\\title{Feuille d'exercices}\n"
        document += "\\author{Généré automatiquement}\n"
        document += "\\date{\\today}\n"
        document += "\\maketitle\n\n"
        
        
        for exercise in self.exercises:

            document += "\\begin{exercice}{}{0}"
            
            # Utiliser le code LaTeX s'il existe, sinon convertir le HTML
            if exercise.get('latex_code') and exercise['latex_code'].strip():
                document += self._clean_latex(exercise['latex_code'])
            else:
                document += self._convert_html_to_latex(exercise['content'])
            
            document += "\\end{exercice}\n\n"
        
        # Ajouter les corrections si demandé
        if include_corrections:
            document += "\\newpage\n"
            document += "\\section{Corrections}\n\n"
            
          
          
            for exercise in self.exercises:

                document += "\\begin{exercice}{}{0}"
                
                # Utiliser le code LaTeX s'il existe, sinon convertir le HTML
                if exercise.get('latex_correction') and exercise['latex_correction'].strip():
                    document += self._clean_latex(exercise['latex_correction'])
                elif exercise.get('correction'):
                    document += self._convert_html_to_latex(exercise['correction'])
                else:
                    document += "Pas de correction disponible."
                
                document += "\\end{exercice}\n\n"                    
        
        document += "\\end{document}"
        
        return document
    
    def _generate_preamble(self):
        """
        Génère le préambule du document LaTeX.
        
        Returns:
            str: Préambule LaTeX.
        """
        preamble = """\\documentclass[a4paper]{article}

% Packages essentiels


\\usepackage{math-vh2}

\\def\\classe{Ma Classe}
\\def\\lieu{Mon Lycée}

"""
        return preamble
    
    def _clean_latex(self, latex_code):
        """
        Nettoie le code LaTeX pour l'insérer dans le document.
        
        Args:
            latex_code (str): Code LaTeX à nettoyer.
            
        Returns:
            str: Code LaTeX nettoyé.
        """
        # Remplacer les sauts de ligne par des sauts de ligne LaTeX
        latex_code = latex_code.replace('\r\n', '\n')
        
        # Supprimer le préambule LaTeX et les commandes de document si présents
        latex_code = re.sub(r'\\documentclass.*?\\begin{document}', '', latex_code, flags=re.DOTALL)
        latex_code = re.sub(r'\\end{document}.*', '', latex_code, flags=re.DOTALL)
        
        # Retirer les espaces superflus
        latex_code = latex_code.strip()
        
        return latex_code
    
    def _convert_html_to_latex(self, html_content):
        """
        Convertit le contenu HTML en LaTeX.
        
        Args:
            html_content (str): Contenu HTML à convertir.
            
        Returns:
            str: Contenu converti en LaTeX.
        """
        if not html_content:
            return ""
        
        # Échapper les caractères spéciaux LaTeX
        latex_content = html_content
        
        # Convertir les balises HTML courantes en équivalents LaTeX
        
        # Paragraphes
        latex_content = re.sub(r'<p>(.*?)</p>', r'\1\n\n', latex_content, flags=re.DOTALL)
        
        # Listes
        latex_content = re.sub(r'<ol.*?>(.*?)</ol>', r'\\begin{enumerate}\1\\end{enumerate}', latex_content, flags=re.DOTALL)
        latex_content = re.sub(r'<ul.*?>(.*?)</ul>', r'\\begin{itemize}\1\\end{itemize}', latex_content, flags=re.DOTALL)
        latex_content = re.sub(r'<li.*?>(.*?)</li>', r'\\item \1', latex_content, flags=re.DOTALL)
        
        # Styles de texte
        latex_content = re.sub(r'<strong>(.*?)</strong>', r'\\textbf{\1}', latex_content)
        latex_content = re.sub(r'<em>(.*?)</em>', r'\\textit{\1}', latex_content)
        latex_content = re.sub(r'<u>(.*?)</u>', r'\\underline{\1}', latex_content)
        
        # Tables (conversion simple)
        latex_content = re.sub(r'<table.*?>(.*?)</table>', r'\\begin{tabular}{|c|c|}\n\\hline\1\\end{tabular}', latex_content, flags=re.DOTALL)
        latex_content = re.sub(r'<tr.*?>(.*?)</tr>', r'\1 \\\\ \\hline', latex_content, flags=re.DOTALL)
        latex_content = re.sub(r'<td.*?>(.*?)</td>', r'\1 & ', latex_content, flags=re.DOTALL)
        latex_content = latex_content.replace('& \\', '\\')
        
        # Supprimer les autres balises HTML
        latex_content = re.sub(r'<[^>]*>', '', latex_content)
        
        # Décoder les entités HTML courantes
        latex_content = html.unescape(latex_content)
        
        # Échapper les caractères spéciaux LaTeX
        special_chars = {
            '&': '\\&',
            '%': '\\%',
            '$': '\\$',
            '#': '\\#',
            '_': '\\_',
            '{': '\\{',
            '}': '\\}',
            '~': '\\textasciitilde{}',
            '^': '\\textasciicircum{}',
            '\\': '\\textbackslash{}'
        }
        
        # Ne pas remplacer à l'intérieur des formules mathématiques
        math_blocks = []
        
        def replace_math(match):
            math_blocks.append(match.group(1))
            return f"MATH_PLACEHOLDER_{len(math_blocks)-1}"
        
        # Extraire les formules mathématiques
        latex_content = re.sub(r'\$(.*?)\$', replace_math, latex_content)
        
        # Échapper les caractères spéciaux (sauf dans les formules mathématiques)
        for char, replacement in special_chars.items():
            latex_content = latex_content.replace(char, replacement)
        
        # Remettre les formules mathématiques
        for i, math in enumerate(math_blocks):
            latex_content = latex_content.replace(f"MATH_PLACEHOLDER_{i}", f"${math}$")
        
        # Nettoyer les espaces multiples et les sauts de ligne
        latex_content = re.sub(r'\n{3,}', '\n\n', latex_content)
        latex_content = re.sub(r' {2,}', ' ', latex_content)
        
        return latex_content.strip()
