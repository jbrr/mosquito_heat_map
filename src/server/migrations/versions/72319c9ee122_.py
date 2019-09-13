"""empty message

Revision ID: 72319c9ee122
Revises: 211cd82c440c
Create Date: 2019-09-01 23:58:13.676265

"""
from alembic import op
import sqlalchemy as sa
from geoalchemy2 import Geometry


# revision identifiers, used by Alembic.
revision = '72319c9ee122'
down_revision = '211cd82c440c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('nlcd_class',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # op.drop_table('spatial_ref_sys')
    op.add_column('location', sa.Column('county', sa.String(), nullable=True))
    op.add_column('location', sa.Column('elevation', sa.Float(), nullable=True))
    op.add_column('location', sa.Column('nlcd_class', sa.Integer(), nullable=True))
    op.add_column('location', sa.Column('point', Geometry(geometry_type='POINT', srid=4326), nullable=True))
    op.create_foreign_key(None, 'location', 'nlcd_class', ['nlcd_class'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'location', type_='foreignkey')
    op.drop_column('location', 'point')
    op.drop_column('location', 'nlcd_class')
    op.drop_column('location', 'elevation')
    op.drop_column('location', 'county')
    op.create_table('spatial_ref_sys',
    sa.Column('srid', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('auth_name', sa.VARCHAR(length=256), autoincrement=False, nullable=True),
    sa.Column('auth_srid', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('srtext', sa.VARCHAR(length=2048), autoincrement=False, nullable=True),
    sa.Column('proj4text', sa.VARCHAR(length=2048), autoincrement=False, nullable=True),
    sa.CheckConstraint('(srid > 0) AND (srid <= 998999)', name='spatial_ref_sys_srid_check'),
    sa.PrimaryKeyConstraint('srid', name='spatial_ref_sys_pkey')
    )
    op.drop_table('nlcd_class')
    # ### end Alembic commands ###