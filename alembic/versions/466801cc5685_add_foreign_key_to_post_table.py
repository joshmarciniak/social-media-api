"""add foreign key to post table

Revision ID: 466801cc5685
Revises: 1389e5cbbb45
Create Date: 2022-02-02 11:29:22.321834

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '466801cc5685'
down_revision = '1389e5cbbb45'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable = False))
    op.create_foreign_key('posts_users_fk', source_table='posts', referent_table='users', 
        local_cols=['owner_id'], remote_cols=['id'], ondelete = "CASCADE")
    pass


def downgrade():
    op.drop_constraint('posts_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
