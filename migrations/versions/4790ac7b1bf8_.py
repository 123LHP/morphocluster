"""empty message

Revision ID: 4790ac7b1bf8
Revises: db2a7b29511b
Create Date: 2018-07-26 09:07:40.249272

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4790ac7b1bf8'
down_revision = 'db2a7b29511b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_nodes_objects_node_id'), 'nodes_objects', ['node_id'], unique=False)
    op.create_index(op.f('ix_nodes_objects_project_id'), 'nodes_objects', ['project_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_nodes_objects_project_id'), table_name='nodes_objects')
    op.drop_index(op.f('ix_nodes_objects_node_id'), table_name='nodes_objects')
    # ### end Alembic commands ###
