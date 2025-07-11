"""new fields in user model

Revision ID: ff0054a720dc
Revises: 3b279175b891
Create Date: 2025-02-17 17:47:24.136914

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ff0054a720dc'
down_revision = '3b279175b891'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=140), nullable=False),
    sa.Column('timestap', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_post_timestap'), ['timestap'], unique=False)
        batch_op.create_index(batch_op.f('ix_post_user_id'), ['user_id'], unique=False)

    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.drop_index('ix_posts_timestap')
        batch_op.drop_index('ix_posts_user_id')

    op.drop_table('posts')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('about_me', sa.String(length=140), nullable=True))
        batch_op.add_column(sa.Column('last_seen', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('last_seen')
        batch_op.drop_column('about_me')

    op.create_table('posts',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('body', sa.VARCHAR(length=140), nullable=False),
    sa.Column('timestap', sa.DATETIME(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.create_index('ix_posts_user_id', ['user_id'], unique=False)
        batch_op.create_index('ix_posts_timestap', ['timestap'], unique=False)

    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_post_user_id'))
        batch_op.drop_index(batch_op.f('ix_post_timestap'))

    op.drop_table('post')
    # ### end Alembic commands ###
