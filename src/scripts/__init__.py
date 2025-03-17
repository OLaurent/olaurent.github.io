# Définir le chemin vers le répertoire parent pour les imports
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))