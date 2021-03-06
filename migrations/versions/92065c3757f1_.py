"""empty message

Revision ID: 92065c3757f1
Revises: 8a467c1ab9b5
Create Date: 2018-05-24 12:46:46.098126

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92065c3757f1'
down_revision = '8a467c1ab9b5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('nodes', sa.Column('cache_depth', sa.Integer(), server_default='0', nullable=False))
    op.drop_column('nodes', 'valid')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('nodes', sa.Column('valid', sa.BOOLEAN(), server_default=sa.text('false'), autoincrement=False, nullable=False))
    op.drop_column('nodes', 'cache_depth')
    # ### end Alembic commands ###
