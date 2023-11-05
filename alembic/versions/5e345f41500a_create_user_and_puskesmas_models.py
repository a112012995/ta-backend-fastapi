"""create user and puskesmas models

Revision ID: 5e345f41500a
Revises: 
Create Date: 2023-11-05 01:54:48.367726

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5e345f41500a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('puskesmas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_puskesmas_id'), 'puskesmas', ['id'], unique=False)
    op.create_index(op.f('ix_puskesmas_name'), 'puskesmas', ['name'], unique=True)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=False),
    sa.Column('hashed_password', sa.String(length=255), nullable=False),
    sa.Column('is_super', sa.Boolean(), nullable=True),
    sa.Column('puskesmas_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['puskesmas_id'], ['puskesmas.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_puskesmas_name'), table_name='puskesmas')
    op.drop_index(op.f('ix_puskesmas_id'), table_name='puskesmas')
    op.drop_table('puskesmas')
    # ### end Alembic commands ###