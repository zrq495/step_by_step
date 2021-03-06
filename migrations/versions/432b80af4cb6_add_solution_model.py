"""add solution model

Revision ID: 432b80af4cb6
Revises: 56d33d6c723f
Create Date: 2015-08-08 16:39:34.818412

"""

# revision identifiers, used by Alembic.
revision = '432b80af4cb6'
down_revision = '56d33d6c723f'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('solution',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('problem_id', sa.Integer(), nullable=False),
    sa.Column('language', sa.String(length=64), nullable=True),
    sa.Column('date_submit', sa.DateTime(), server_default=sa.text(u'CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('date_created', sa.DateTime(), server_default=sa.text(u'CURRENT_TIMESTAMP'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_solution_date_created'), 'solution', ['date_created'], unique=False)
    op.create_index(op.f('ix_solution_date_submit'), 'solution', ['date_submit'], unique=False)
    op.create_index(op.f('ix_solution_problem_id'), 'solution', ['problem_id'], unique=False)
    op.create_index(op.f('ix_solution_user_id'), 'solution', ['user_id'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_solution_user_id'), table_name='solution')
    op.drop_index(op.f('ix_solution_problem_id'), table_name='solution')
    op.drop_index(op.f('ix_solution_date_submit'), table_name='solution')
    op.drop_index(op.f('ix_solution_date_created'), table_name='solution')
    op.drop_table('solution')
    ### end Alembic commands ###
