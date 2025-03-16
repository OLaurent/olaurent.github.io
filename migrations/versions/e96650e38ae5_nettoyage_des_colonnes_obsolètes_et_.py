"""Nettoyage des colonnes obsolètes et modification des contraintes

Revision ID: e96650e38ae5
Revises: 1ffa50539758
Create Date: 2025-03-16 15:44:24.304725

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e96650e38ae5'
down_revision = '1ffa50539758'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('exercices', schema=None) as batch_op:
        batch_op.alter_column('level_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('theme_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.drop_column('level')
        batch_op.drop_column('theme')

    with op.batch_alter_table('tags', schema=None) as batch_op:
        batch_op.alter_column('level_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.drop_constraint('uq_tag_name', type_='unique')
        batch_op.create_unique_constraint('uq_tag_name_level', ['name', 'level_id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tags', schema=None) as batch_op:
        batch_op.drop_constraint('uq_tag_name_level', type_='unique')
        batch_op.create_unique_constraint('uq_tag_name', ['name'])
        batch_op.alter_column('level_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    with op.batch_alter_table('exercices', schema=None) as batch_op:
        batch_op.add_column(sa.Column('theme', sa.VARCHAR(), nullable=True))
        batch_op.add_column(sa.Column('level', sa.VARCHAR(), nullable=True))
        batch_op.alter_column('theme_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('level_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###
