"""empty message

Revision ID: 39025902cf5d
Revises: 72319c9ee122
Create Date: 2019-09-02 01:22:30.516902

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '39025902cf5d'
down_revision = '72319c9ee122'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('location', sa.Column('nlcd_class_id', sa.Integer(), nullable=True))
    op.drop_constraint('location_nlcd_class_fkey', 'location', type_='foreignkey')
    op.create_foreign_key(None, 'location', 'nlcd_class', ['nlcd_class_id'], ['id'])
    op.drop_column('location', 'nlcd_class')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('location', sa.Column('nlcd_class', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'location', type_='foreignkey')
    op.create_foreign_key('location_nlcd_class_fkey', 'location', 'nlcd_class', ['nlcd_class'], ['id'])
    op.drop_column('location', 'nlcd_class_id')
    # ### end Alembic commands ###
