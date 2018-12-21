"""empty message

Revision ID: 115ec8f90dd4
Revises: 
Create Date: 2018-12-21 21:55:19.941638

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '115ec8f90dd4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('badges',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('badge_image_sm', sa.String(length=200), nullable=True),
    sa.Column('badge_image_md', sa.String(length=200), nullable=True),
    sa.Column('badge_image_lg', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('breweries',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('label', sa.String(length=200), nullable=True),
    sa.Column('country', sa.String(length=80), nullable=True),
    sa.Column('city', sa.String(length=80), nullable=True),
    sa.Column('state', sa.String(length=80), nullable=True),
    sa.Column('latitude', sa.Float(), nullable=True),
    sa.Column('longitude', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_name', sa.String(length=80), nullable=True),
    sa.Column('first_name', sa.String(length=80), nullable=True),
    sa.Column('last_name', sa.String(length=80), nullable=True),
    sa.Column('avatar', sa.String(length=200), nullable=True),
    sa.Column('avatar_hd', sa.String(length=200), nullable=True),
    sa.Column('total_badges', sa.Integer(), nullable=True),
    sa.Column('total_friends', sa.Integer(), nullable=True),
    sa.Column('total_checkins', sa.Integer(), nullable=True),
    sa.Column('total_beers', sa.Integer(), nullable=True),
    sa.Column('access_token', sa.String(length=200), nullable=True),
    sa.Column('api_request_count', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_name')
    )
    op.create_table('venues',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('country', sa.String(length=80), nullable=True),
    sa.Column('city', sa.String(length=80), nullable=True),
    sa.Column('state', sa.String(length=80), nullable=True),
    sa.Column('latitude', sa.Float(), nullable=True),
    sa.Column('longitude', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('beers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('label', sa.String(length=200), nullable=True),
    sa.Column('rating', sa.Float(), nullable=True),
    sa.Column('abv', sa.Float(), nullable=True),
    sa.Column('brewery_id', sa.Integer(), nullable=False),
    sa.Column('style', sa.String(length=80), nullable=True),
    sa.ForeignKeyConstraint(['brewery_id'], ['breweries.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('checkins',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('beer_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('count', sa.Integer(), nullable=True),
    sa.Column('rating', sa.Float(), nullable=True),
    sa.Column('first_had', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['beer_id'], ['beers.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('checkins')
    op.drop_table('beers')
    op.drop_table('venues')
    op.drop_table('users')
    op.drop_table('breweries')
    op.drop_table('badges')
    # ### end Alembic commands ###
