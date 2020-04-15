"""added more fields to membership table

Revision ID: 0312bd0a3452
Revises: 21631e11f7d1
Create Date: 2020-03-05 23:24:28.788038

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0312bd0a3452'
down_revision = '21631e11f7d1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('memberships', sa.Column('occupation', sa.String(length=150), nullable=True))
    op.add_column('memberships', sa.Column('phone2', sa.String(length=20), nullable=True))
    op.add_column('memberships', sa.Column('work_address', sa.String(length=200), nullable=True))
    op.add_column('memberships', sa.Column('work_place', sa.String(length=150), nullable=True))
    op.add_column('memberships', sa.Column('work_title', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('memberships', 'work_title')
    op.drop_column('memberships', 'work_place')
    op.drop_column('memberships', 'work_address')
    op.drop_column('memberships', 'phone2')
    op.drop_column('memberships', 'occupation')
    # ### end Alembic commands ###