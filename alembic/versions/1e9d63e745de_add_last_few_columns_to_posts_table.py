"""add last few columns to posts table

Revision ID: 1e9d63e745de
Revises: 41a6a2e5743f
Create Date: 2023-07-03 10:19:49.404159

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1e9d63e745de'
down_revision = '41a6a2e5743f'
branch_labels = None
depends_on = None


def upgrade() :
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
