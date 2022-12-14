"""created office table

Revision ID: 21631e11f7d1
Revises: 37bbe1755ba8
Create Date: 2020-02-25 23:32:29.997229

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '21631e11f7d1'
down_revision = '37bbe1755ba8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('offices',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('post', sa.String(length=120), nullable=True),
    sa.Column('alias', sa.String(length=20), nullable=True),
    sa.Column('arm', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('offices')
    # ### end Alembic commands ###
