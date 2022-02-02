"""add user table

Revision ID: 1389e5cbbb45
Revises: 4f3903c7e4a0
Create Date: 2022-02-02 11:22:20.376892

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1389e5cbbb45'
down_revision = '4f3903c7e4a0'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('password', sa.String(), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True),
            server_default=sa.text('now()'),nullable = False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )
    pass


def downgrade():
    op.drop_table('users')
    pass
