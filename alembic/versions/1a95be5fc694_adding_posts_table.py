"""adding posts table

Revision ID: 1a95be5fc694
Revises: 
Create Date: 2022-02-02 11:16:34.911884

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a95be5fc694'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer, nullable = False, primary_key = True), sa.Column('title', sa.String, nullable = False))
    pass


def downgrade():
    op.drop_table('posts')
    pass