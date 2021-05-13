"""empty message

Revision ID: 7114f8ce85ec
Revises: f0013206627c
Create Date: 2021-05-13 12:07:11.903960

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7114f8ce85ec'
down_revision = 'f0013206627c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('juices')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('juices',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('energy', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('activities', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('toys', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='juices_pkey')
    )
    # ### end Alembic commands ###