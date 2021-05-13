"""empty message

Revision ID: f0013206627c
Revises: 3e4037af4ab1
Create Date: 2021-05-13 12:03:57.953956

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f0013206627c'
down_revision = '3e4037af4ab1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('juices', sa.Column('toys', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('juices', 'toys')
    # ### end Alembic commands ###
