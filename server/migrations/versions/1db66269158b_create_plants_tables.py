"""Create plants tables

Revision ID: 1db66269158b
Revises: 67f5d67aea55
Create Date: 2023-09-23 10:08:35.142557

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1db66269158b'
down_revision = '67f5d67aea55'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('plants',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('plants')
    # ### end Alembic commands ###
