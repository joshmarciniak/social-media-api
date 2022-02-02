"""adding content column to posts table

Revision ID: 4f3903c7e4a0
Revises: 1a95be5fc694
Create Date: 2022-02-02 11:17:52.608951

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4f3903c7e4a0'
down_revision = '1a95be5fc694'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass

def downgrade():
    op.drop_column('posts', 'content')
    pass