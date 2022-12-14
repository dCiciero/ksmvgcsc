"""added display_order to exco table

Revision ID: 5e202b2df526
Revises: 8d541b93f22b
Create Date: 2019-03-01 20:17:00.960258

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5e202b2df526'
down_revision = '8d541b93f22b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('executives', sa.Column('display_order', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('executives', 'display_order')
    # ### end Alembic commands ###
