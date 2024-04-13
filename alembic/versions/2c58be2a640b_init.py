"""Init

Revision ID: 2c58be2a640b
Revises: 
Create Date: 2024-04-13 18:40:40.870160

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2c58be2a640b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Groups',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Teachers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_name', sa.String(length=150), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Students',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_name', sa.String(length=150), nullable=False),
    sa.Column('group_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['group_id'], ['Groups.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Subjects',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=175), nullable=False),
    sa.Column('teacher_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['teacher_id'], ['Teachers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Grades',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('subject_id', sa.Integer(), nullable=False),
    sa.Column('grade', sa.Integer(), nullable=False),
    sa.Column('grade_date', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['student_id'], ['Students.id'], ),
    sa.ForeignKeyConstraint(['subject_id'], ['Subjects.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('teachers')
    op.drop_table('grades')
    op.drop_table('subjects')
    op.drop_table('groups')
    op.drop_table('students')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('students',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('students_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('full_name', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.Column('group_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['group_id'], ['groups.id'], name='students_group_id_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name='students_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('groups',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('groups_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='groups_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('subjects',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('subjects_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=175), autoincrement=False, nullable=False),
    sa.Column('teacher_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['teacher_id'], ['teachers.id'], name='subjects_teacher_id_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name='subjects_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('grades',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('student_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('subject_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('grade', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('grade_date', sa.DATE(), autoincrement=False, nullable=False),
    sa.CheckConstraint('grade >= 0 AND grade <= 100', name='grades_grade_check'),
    sa.ForeignKeyConstraint(['student_id'], ['students.id'], name='grades_student_id_fkey', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['subject_id'], ['subjects.id'], name='grades_subject_id_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name='grades_pkey')
    )
    op.create_table('teachers',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('full_name', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='teachers_pkey')
    )
    op.drop_table('Grades')
    op.drop_table('Subjects')
    op.drop_table('Students')
    op.drop_table('Teachers')
    op.drop_table('Groups')
    # ### end Alembic commands ###
