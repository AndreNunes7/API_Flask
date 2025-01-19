"""empty message

Revision ID: ea8187dc8771
Revises: ac2e5ff6c108
Create Date: 2024-08-16 14:37:04.228303

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea8187dc8771'
down_revision = 'ac2e5ff6c108'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('curso', schema=None) as batch_op:
        batch_op.add_column(sa.Column('formacao_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'formacao', ['formacao_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('curso', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('formacao_id')

    # ### end Alembic commands ###
