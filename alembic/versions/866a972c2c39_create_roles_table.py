"""create roles table

Revision ID: 866a972c2c39
Revises: 42c29316d8a6
Create Date: 2023-11-06 15:51:31.029721

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '866a972c2c39'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'roles',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(64), nullable=False)
    )


def downgrade() -> None:
    op.drop_table('roles')
