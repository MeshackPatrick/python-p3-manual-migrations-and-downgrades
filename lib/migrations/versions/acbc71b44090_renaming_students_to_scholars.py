"""Renaming students to scholars

Revision ID: acbc71b44090
Revises: 791279dd0760
Create Date: 2023-08-31 16:07:24.550619

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'acbc71b44090'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
