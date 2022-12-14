"""added access.id to membership table

Revision ID: 4d9b2aaa7408
Revises: 43e692adb8d7
Create Date: 2019-03-07 01:04:52.472184

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4d9b2aaa7408'
down_revision = '43e692adb8d7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('memberships', sa.Column('access_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'memberships', 'access', ['access_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'memberships', type_='foreignkey')
    op.drop_column('memberships', 'access_id')
    # ### end Alembic commands ###
