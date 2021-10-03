"""moves table

Revision ID: 5af82f2dbe81
Revises:
Create Date: 2021-10-02 11:40:27.139442

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID, JSON
import uuid

from sqlalchemy.sql.schema import ForeignKeyConstraint

# revision identifiers, used by Alembic.
revision = '5af82f2dbe81'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'moves',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('reference', UUID(as_uuid=True), unique=True,
                  index=True, default=uuid.uuid4, nullable=False),
        sa.Column('previousMove', UUID(as_uuid=True), nullable=True),
        sa.Column('payload', JSON, nullable=False),
        sa.Column('step_number', sa.Integer, nullable=False)
    )
    op.create_foreign_key(None, 'moves', 'moves', ['previousMove'], [
                          'reference'], ondelete='SET NULL')


def downgrade():
    op.drop_table('moves')
