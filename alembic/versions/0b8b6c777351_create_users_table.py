"""create users table

Revision ID: 0b8b6c777351
Revises: 866a972c2c39
Create Date: 2023-11-06 15:53:46.293021

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import datetime

# revision identifiers, used by Alembic.
revision: str = '0b8b6c777351'
down_revision: Union[str, None] = '866a972c2c39'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('name', sa.String(256)),
        sa.Column('password', sa.String(128)),
        sa.Column('email', sa.String(128), unique=True),
        sa.Column('jwt_token', sa.String(256)),
        sa.Column('author_id', sa.Integer, sa.ForeignKey("roles.id")),
        sa.Column('created_at', sa.DateTime, default=datetime.datetime.utcnow),
        sa.Column('updated_at', sa.DateTime, onupdate=datetime.datetime.utcnow)
    )

# Видалення таблиці у зворотньому напрямку
def downgrade():
    op.drop_table('users')
