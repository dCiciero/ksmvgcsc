"""added state_of_origin to membership table

Revision ID: e1b1068e884f
Revises: 4d9b2aaa7408
Create Date: 2019-03-09 11:43:17.290670

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e1b1068e884f'
down_revision = '4d9b2aaa7408'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('memberships', sa.Column('state_of_origin', sa.String(length=20), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('memberships', 'state_of_origin')
    # ### end Alembic commands ###
