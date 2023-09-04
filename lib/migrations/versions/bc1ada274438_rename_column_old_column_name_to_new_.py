"""Rename column old_column_name to new_column_name

Revision ID: bc1ada274438
Revises: acbc71b44090
Create Date: 2023-09-04 10:54:10.077338

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc1ada274438'
down_revision = 'acbc71b44090'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_column('Colunm(String)', 'Column(Integer)')


def downgrade() -> None:
    pass
