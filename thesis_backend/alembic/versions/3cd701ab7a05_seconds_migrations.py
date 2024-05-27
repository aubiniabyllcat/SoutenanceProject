"""seconds  migrations

Revision ID: 3cd701ab7a05
Revises: 51ae781bded8
Create Date: 2024-05-27 11:50:27.020458

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3cd701ab7a05'
down_revision = '51ae781bded8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('utilisateur_image',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('photo', sa.String(), nullable=True),
    sa.Column('utilisateur_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['utilisateur_id'], ['utilisateur.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('utilisateur_images')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('utilisateur_images',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('photo', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('utilisateur_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['utilisateur_id'], ['utilisateur.id'], name='utilisateur_images_utilisateur_id_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name='utilisateur_images_pkey')
    )
    op.drop_table('utilisateur_image')
    # ### end Alembic commands ###
