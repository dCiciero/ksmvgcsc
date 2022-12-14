"""migrate data to postgres

Revision ID: 43e692adb8d7
Revises: 
Create Date: 2019-03-05 17:47:46.885231

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '43e692adb8d7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('access',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_access_email'), 'access', ['email'], unique=True)
    op.create_index(op.f('ix_access_username'), 'access', ['username'], unique=True)
    op.create_table('carousel',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('caption', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('executives',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('post', sa.String(length=50), nullable=False),
    sa.Column('elected_date', sa.Date(), nullable=True),
    sa.Column('where', sa.String(length=5), nullable=False),
    sa.Column('alias', sa.String(length=10), nullable=False),
    sa.Column('display_order', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_executives_elected_date'), 'executives', ['elected_date'], unique=False)
    op.create_table('memberships',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=False),
    sa.Column('last_name', sa.String(length=50), nullable=False),
    sa.Column('other_names', sa.String(length=75), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('address', sa.String(length=200), nullable=False),
    sa.Column('birth_date', sa.Date(), nullable=True),
    sa.Column('initiation_date', sa.Date(), nullable=True),
    sa.Column('investiture_date', sa.Date(), nullable=True),
    sa.Column('home_town', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_memberships_birth_date'), 'memberships', ['birth_date'], unique=False)
    op.create_index(op.f('ix_memberships_initiation_date'), 'memberships', ['initiation_date'], unique=False)
    op.create_index(op.f('ix_memberships_investiture_date'), 'memberships', ['investiture_date'], unique=False)
    op.create_table('pastexecutives',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('post', sa.String(length=50), nullable=False),
    sa.Column('start_date', sa.Date(), nullable=True),
    sa.Column('end_date', sa.Date(), nullable=True),
    sa.Column('where', sa.String(length=5), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_pastexecutives_end_date'), 'pastexecutives', ['end_date'], unique=False)
    op.create_index(op.f('ix_pastexecutives_start_date'), 'pastexecutives', ['start_date'], unique=False)
    op.create_table('profiles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=False),
    sa.Column('last_name', sa.String(length=50), nullable=False),
    sa.Column('other_names', sa.String(length=75), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('address', sa.String(length=200), nullable=False),
    sa.Column('phone1', sa.String(length=20), nullable=False),
    sa.Column('phone2', sa.String(length=20), nullable=True),
    sa.Column('occupation', sa.String(length=150), nullable=True),
    sa.Column('work_place', sa.String(length=150), nullable=True),
    sa.Column('work_address', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('news',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('topic', sa.String(length=120), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('date_created', sa.Date(), nullable=True),
    sa.Column('posted_by', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['posted_by'], ['access.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_news_date_created'), 'news', ['date_created'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_news_date_created'), table_name='news')
    op.drop_table('news')
    op.drop_table('profiles')
    op.drop_index(op.f('ix_pastexecutives_start_date'), table_name='pastexecutives')
    op.drop_index(op.f('ix_pastexecutives_end_date'), table_name='pastexecutives')
    op.drop_table('pastexecutives')
    op.drop_index(op.f('ix_memberships_investiture_date'), table_name='memberships')
    op.drop_index(op.f('ix_memberships_initiation_date'), table_name='memberships')
    op.drop_index(op.f('ix_memberships_birth_date'), table_name='memberships')
    op.drop_table('memberships')
    op.drop_index(op.f('ix_executives_elected_date'), table_name='executives')
    op.drop_table('executives')
    op.drop_table('carousel')
    op.drop_index(op.f('ix_access_username'), table_name='access')
    op.drop_index(op.f('ix_access_email'), table_name='access')
    op.drop_table('access')
    # ### end Alembic commands ###
