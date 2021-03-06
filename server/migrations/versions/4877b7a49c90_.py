"""empty message

Revision ID: 4877b7a49c90
Revises: 826505656e67
Create Date: 2016-03-20 08:23:30.639904

"""

# revision identifiers, used by Alembic.
revision = '4877b7a49c90'
down_revision = '826505656e67'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('articles', sa.Column('media', postgresql.ARRAY(sa.String()), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('articles', 'media')
    ### end Alembic commands ###
