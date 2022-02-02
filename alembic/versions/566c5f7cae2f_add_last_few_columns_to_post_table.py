"""add last few columns to post table

Revision ID: 566c5f7cae2f
Revises: 466801cc5685
Create Date: 2022-02-02 11:32:58.710678

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '566c5f7cae2f'
down_revision = '466801cc5685'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable = False, server_default='TRUE'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable = False, server_default=sa.text('NOW()')))
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
