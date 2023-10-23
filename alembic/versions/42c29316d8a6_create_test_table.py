"""create test table

Revision ID: 42c29316d8a6
Revises: 
Create Date: 2023-10-17 16:59:26.058678

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '42c29316d8a6'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'text',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(90), nullable=False)
    )


def downgrade() -> None:
    op.drop_table('text')
