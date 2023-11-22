"""added color column

Revision ID: bcd6ca828095
Revises: 07f1321fbdaf
Create Date: 2023-11-22 18:27:24.689673

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bcd6ca828095'
down_revision = '07f1321fbdaf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('puppies', schema=None) as batch_op:
        batch_op.add_column(sa.Column('color', sa.Text(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('puppies', schema=None) as batch_op:
        batch_op.drop_column('color')

    # ### end Alembic commands ###
