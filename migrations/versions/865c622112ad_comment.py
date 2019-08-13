"""comment

Revision ID: 865c622112ad
Revises: cc862bfe95d2
Create Date: 2019-08-12 12:59:13.834624

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '865c622112ad'
down_revision = 'cc862bfe95d2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'cars', ['id'])
    op.add_column('users', sa.Column('api_token_expiration', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_users_api_token'), 'users', ['api_token'], unique=True)
    op.drop_constraint('users_api_token_key', 'users', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('users_api_token_key', 'users', ['api_token'])
    op.drop_index(op.f('ix_users_api_token'), table_name='users')
    op.drop_column('users', 'api_token_expiration')
    op.drop_constraint(None, 'cars', type_='unique')
    # ### end Alembic commands ###
