"""initial  migrations

Revision ID: 85c69a727b4d
Revises: 
Create Date: 2024-05-27 11:18:11.392090

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '85c69a727b4d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('annee',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('libelle', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('filiere',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('libelle', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('libelle', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('utilisateur',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=200), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('nom', sa.String(length=200), nullable=False),
    sa.Column('prenoms', sa.String(length=200), nullable=False),
    sa.Column('bio', sa.String(length=255), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('created', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('enseignants',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('matricule', sa.String(length=200), nullable=False),
    sa.Column('slug', sa.String(), nullable=True),
    sa.Column('grade', sa.String(length=200), nullable=False),
    sa.Column('specialite', sa.String(length=200), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('filiere_id', sa.Integer(), nullable=True),
    sa.Column('annee_id', sa.Integer(), nullable=True),
    sa.Column('created', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['annee_id'], ['annee.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['filiere_id'], ['filiere.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['utilisateur.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('matricule')
    )
    op.create_table('etudiants',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('matricule', sa.String(length=200), nullable=False),
    sa.Column('slug', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('filiere_id', sa.Integer(), nullable=True),
    sa.Column('annee_id', sa.Integer(), nullable=True),
    sa.Column('created', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['annee_id'], ['annee.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['filiere_id'], ['filiere.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['utilisateur.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('matricule')
    )
    op.create_table('utilisateur_images',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('photo', sa.String(), nullable=True),
    sa.Column('utilisateur_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['utilisateur_id'], ['utilisateur.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('utilisateur_images')
    op.drop_table('etudiants')
    op.drop_table('enseignants')
    op.drop_table('utilisateur')
    op.drop_table('role')
    op.drop_table('filiere')
    op.drop_table('annee')
    # ### end Alembic commands ###
