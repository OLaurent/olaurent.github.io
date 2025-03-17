"""Fix id auto-increment

Revision ID: c73c656d57a0
Revises: e96650e38ae5
Create Date: 2025-03-17 21:17:44.401382

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c73c656d57a0'
down_revision = 'e96650e38ae5'
branch_labels = None
depends_on = None


def upgrade():
    # Utiliser une approche complète de reconstruction de table au lieu d'alter column
    
    # 1. Création d'une table temporaire avec la nouvelle structure
    op.execute("""
    CREATE TABLE exercices_new (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        level_id INTEGER NOT NULL,
        theme_id INTEGER NOT NULL,
        selected BOOLEAN,
        content TEXT NOT NULL,
        latex_code TEXT,
        correction TEXT,
        latex_correction TEXT,
        FOREIGN KEY (level_id) REFERENCES levels (id),
        FOREIGN KEY (theme_id) REFERENCES themes (id)
    )
    """)
    
    # 2. Copier les données, mais en ignorant l'ID (laissant SQLite générer de nouveaux IDs)
    op.execute("""
    INSERT INTO exercices_new (level_id, theme_id, selected, content, latex_code, correction, latex_correction)
    SELECT level_id, theme_id, selected, content, latex_code, correction, latex_correction
    FROM exercices
    """)
    
    # 3. Créer une table de correspondance pour mapper les anciens IDs aux nouveaux IDs
    op.execute("CREATE TABLE id_mapping (old_id VARCHAR, new_id INTEGER)")
    
    # 4. Remplir cette table de correspondance
    op.execute("""
    INSERT INTO id_mapping (old_id, new_id)
    SELECT e.id, en.id
    FROM exercices e
    JOIN exercices_new en ON 
        e.level_id = en.level_id AND 
        e.theme_id = en.theme_id AND 
        e.content = en.content
    """)
    
    # 5. Créer une table temporaire pour exercice_tags
    op.execute("CREATE TABLE exercice_tags_new (exercice_id INTEGER, tag_id INTEGER)")
    
    # 6. Copier les relations tag avec les nouveaux IDs
    op.execute("""
    INSERT INTO exercice_tags_new (exercice_id, tag_id)
    SELECT m.new_id, et.tag_id
    FROM exercice_tags et
    JOIN id_mapping m ON et.exercice_id = m.old_id
    """)
    
    # 7. Supprimer les anciennes tables
    op.execute("DROP TABLE exercice_tags")
    op.execute("DROP TABLE exercices")
    
    # 8. Renommer les nouvelles tables
    op.execute("ALTER TABLE exercices_new RENAME TO exercices")
    op.execute("ALTER TABLE exercice_tags_new RENAME TO exercice_tags")
    
    # 9. Ajouter les contraintes nécessaires sur exercice_tags
    op.execute("""
    CREATE INDEX ix_exercice_tags_exercice_id ON exercice_tags (exercice_id)
    """)
    op.execute("""
    CREATE INDEX ix_exercice_tags_tag_id ON exercice_tags (tag_id)
    """)
    
    # 10. Nettoyer la table de mapping temporaire
    op.execute("DROP TABLE id_mapping")


def downgrade():
    # Le downgrade n'est pas possible de manière sûre car nous avons réassigné des IDs
    # Mais on peut fournir une structure de base
    op.execute("""
    CREATE TABLE exercices_old (
        id VARCHAR PRIMARY KEY,
        level_id INTEGER NOT NULL,
        theme_id INTEGER NOT NULL,
        selected BOOLEAN,
        content TEXT NOT NULL,
        latex_code TEXT,
        correction TEXT,
        latex_correction TEXT
    )
    """)
    
    op.execute("""
    INSERT INTO exercices_old (id, level_id, theme_id, selected, content, latex_code, correction, latex_correction)
    SELECT CAST(id AS VARCHAR), level_id, theme_id, selected, content, latex_code, correction, latex_correction
    FROM exercices
    """)
    
    op.execute("DROP TABLE exercices")
    op.execute("ALTER TABLE exercices_old RENAME TO exercices")