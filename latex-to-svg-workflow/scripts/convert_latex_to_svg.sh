#!/bin/bash

# Définir les chemins des répertoires
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
INPUT_DIR="$PROJECT_DIR/input"
OUTPUT_DIR="$PROJECT_DIR/output"

# Vérifier si un fichier est spécifié
if [ $# -eq 0 ]; then
    # Si aucun fichier n'est spécifié, utiliser tous les fichiers .tex dans le répertoire d'entrée
    FILES="$INPUT_DIR/*.tex"
else
    # Sinon, utiliser le fichier spécifié
    FILES="$INPUT_DIR/$1"
fi

echo "$FILES"
# Créer le répertoire de sortie s'il n'existe pas
mkdir -p "$OUTPUT_DIR"

# Traitement des fichiers
for FILE in "$FILES"; do
    echo "$FILE"
    if [ -f "$FILE" ]; then
        # Extraire le nom de base du fichier sans l'extension
        BASENAME=$(basename "$FILE" .tex | sed 's/ /_/g')
        echo "BASENAME"
        echo "$BASENAME"
        
        echo "Traitement de $BASENAME.tex"
        
        # Copier le fichier dans un répertoire temporaire pour éviter les conflits
        TMP_DIR="$(mktemp -d)"
        cp "$FILE" "$TMP_DIR/$BASENAME.tex"
        
        # Se déplacer dans le répertoire temporaire
        cd "$TMP_DIR"
        
        # Compiler le fichier LaTeX en DVI
        latex "$BASENAME.tex"
        
        # Convertir le fichier DVI en SVG
        dvisvgm --libgs=/opt/local/lib/libgs.dylib "$BASENAME.dvi"
        
        # Appliquer les modifications au fichier SVG avec Python
        python3 "$SCRIPT_DIR/modify_svg.py" "$BASENAME.svg"
        
        # Déplacer le fichier SVG modifié vers le répertoire de sortie
        mv "$BASENAME.svg" "$OUTPUT_DIR/"
        
        # Nettoyer les fichiers temporaires
        cd "$PROJECT_DIR"
        rm -rf "$TMP_DIR"
        
        echo "Le fichier $BASENAME.svg a été créé avec succès dans le répertoire output"
    fi
done