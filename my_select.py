from sqlalchemy import func, desc, and_
from connection import session
from models import Grade, Teacher, Student, Group, Subject
from pprint import pprint

def select_1():
    """
    SELECT s.fullname, round(avg(g.grade), 2) AS avg_grade
    FROM grades g
    LEFT JOIN students s ON s.id = g.student_id
    GROUP BY s.id
    ORDER BY avg_grade DESC
    LIMIT 5;
    """
    result = session.query(Student.id, Student.full_name, func.round(func.avg(Grade.grade), 2).label('average_grade')) \
        .select_from(Grade).join(Student).group_by(Student.id).order_by(
        desc('average_grade')).limit(5).all()
    return result


def select_2():
    """
    SELECT
        s.id,
        s.fullname,
        ROUND(AVG(g.grade), 2) AS average_grade
    FROM grades g
    JOIN students s ON s.id = g.student_id
    where g.subject_id = 1
    GROUP BY s.id
    ORDER BY average_grade DESC
    LIMIT 1;
    """
    result = session.query(Student.id, Student.full_name, func.round(func.avg(Grade.grade), 2).label('average_grade')) \
        .select_from(Grade) \
        .join(Student).filter(Grade.subjects_id == 1) \
        .group_by(Student.id).order_by(desc('average_grade')).limit(1).all()
    return result


def select_3():
    """  SELECT groups.name AS group_name,
           round(AVG(grades.grade),2) AS average_grade
    FROM groups
    JOIN students ON groups.id = students.group_id
    JOIN grades ON students.id = grades.student_id
    JOIN subjects ON grades.subject_id = subjects.id
    WHERE subjects.name = 'chemistry'
    GROUP BY groups.id, groups.name
    ORDER BY average_grade DESC;"""
    result = session.query(Group.name.label('group_name'),
                           func.round(func.avg(Grade.grade), 2).label('average_grade')) \
        .join(Student, Group.id == Student.group_id) \
        .join(Grade, Student.id == Grade.student_id) \
        .join(Subject, Grade.subject_id == Subject.id) \
        .filter(Subject.name == 'nation') \
        .group_by(Group.id, Group.name) \
        .order_by(desc('average_grade')) \
        .all()
    return result


def select_4():
    """
    Знайти середній бал на потоці (по всій таблиці оцінок).

    SELECT ROUND(AVG(grades.grade),2) AS average_grade
    FROM grades;
    """
    result = session.query(func.round(func.avg(Grade.grade), 2).label('average_grade')).all()
    return result


def select_5():
    """
    Знайти які курси читає певний викладач.

    SELECT s.id AS subject_id, s.name AS subject_name
    FROM Subjects s
    JOIN Teachers t ON s.teacher_id = t.id
    WHERE t.full_name = 'Rebecca Nicholson';
    """
    result = session.query(Subject.id.label('subject_id'), Subject.name.label('subject_name')) \
        .join(Teacher, Subject.teacher_id == Teacher.id) \
        .filter(Teacher.full_name == 'Rebecca Nicholson') \
        .all()
    return result


def select_6():
    """
    Знайти список студентів у певній групі.

    SELECT s.full_name AS student_name
    FROM students s
    JOIN groups g ON s.group_id = g.id
    WHERE g.name = 'food';
    """
    result = session.query(Student.full_name.label('student_name')) \
        .join(Group, Student.group_id == Group.id) \
        .filter(Group.name == 'food') \
        .all()
    return result


def select_7():
    """
    Знайти оцінки студентів у окремій групі з певного предмета.

    SELECT
    stud.full_name AS student_name,
    grp.name AS group_name,
    sub.name AS subject_name,
    grd.grade

    FROM students stud

    JOIN grades grd ON stud.id = grd.student_id
    JOIN subjects sub ON grd.subject_id = sub.id
    JOIN groups grp ON stud.group_id = grp.id

    WHERE
    grp.name = 'food'
    AND sub.name = 'nation';
    """
    result = session.query(
        Student.full_name.label('student_name'),
        Group.name.label('group_name'),
        Subject.name.label('subject_name'),
        Grade.grade
    ) \
    .join(Grade, Student.id == Grade.student_id) \
    .join(Subject, Grade.subject_id == Subject.id) \
    .join(Group, Student.group_id == Group.id) \
    .filter(Group.name == 'food') \
    .filter(Subject.name == 'nation') \
    .all()
    return result


def select_8():
    """
    Знайти середній бал, який ставить певний викладач зі своїх предметів.

    SELECT
    t.full_name AS teacher_name,
    sub.name AS subject_name,
    ROUND(AVG(gr.grade), 2) AS average_grade

    FROM teachers t

    JOIN subjects sub ON t.id = sub.teacher_id
    JOIN grades gr ON sub.id = gr.subject_id

    GROUP BY t.full_name, sub.name;
    """
    result = session.query(
        Teacher.full_name.label('teacher_name'),
        Subject.name.label('subject_name'),
        func.round(func.avg(Grade.grade), 2).label('average_grade')
    ) \
    .join(Subject, Teacher.id == Subject.teacher_id) \
    .join(Grade, Subject.id == Grade.subject_id) \
    .group_by(Teacher.full_name, Subject.name) \
    .all()
    return result


def select_9():
    """
    Знайти список курсів, які відвідує певний студент.
    SELECT DISTINCT subj.name AS subject

    FROM subjects subj

    JOIN grades g ON subj.id = g.subject_id
    JOIN students st ON g.student_id = st.id

    WHERE st.full_name = 'Gloria Rodriguez';

    """
    result = session.query(Subject.name.label('subject')) \
    .join(Grade, Subject.id == Grade.subject_id) \
    .join(Student, Grade.student_id == Student.id) \
    .filter(Student.full_name == 'Gloria Rodriguez') \
    .distinct() \
    .all()
    return result


def select_10():
    """
    Список курсів, які певному студенту читає певний викладач.

    SELECT
        st.full_name AS student,
        t.full_name AS responsible_teacher,
        subj.name AS subject

    FROM subjects subj

    JOIN grades grd ON subj.id = grd.subject_id
    JOIN students st ON grd.student_id = st.id
    JOIN teachers t ON subj.teacher_id = t.id

    WHERE
        st.full_name = 'Brandon Torres'
        AND t.full_name = 'James Harris';
    """
    result = session.query(Student.full_name.label('student'),
                           Teacher.full_name.label('responsible_teacher'),
                           Subject.name.label('subject')) \
    .join(Grade, Subject.id == Grade.subject_id) \
    .join(Student, Grade.student_id == Student.id) \
    .join(Teacher, Subject.teacher_id == Teacher.id) \
    .filter(Student.full_name == 'Brandon Torres') \
    .filter(Teacher.full_name == 'James Harris') \
    .all()
    return result


def select_11():
    """
    Середній бал, який певний викладач ставить певному студентові.

    SELECT
        t.full_name AS teacher,
        st.full_name AS student,
        ROUND(AVG(grade), 2)

    FROM grades grd

    JOIN subjects subj ON grd.subject_id = subj.id
    JOIN teachers t ON subj.teacher_id = t.id
    JOIN students st ON grd.student_id = st.id

    WHERE
        st.full_name = 'Sandra Cox'
        AND t.full_name = 'Brian Brown'

    GROUP BY
        t.full_name, st.full_name;
    """
    result = session.query(Teacher.full_name.label('teacher'),
                           Student.full_name.label('student'),
                           func.round(func.avg(Grade.grade), 2).label('average_grade')) \
    .join(Subject, Grade.subject_id == Subject.id) \
    .join(Teacher, Subject.teacher_id == Teacher.id) \
    .join(Student, Grade.student_id == Student.id) \
    .filter(Student.full_name == 'Sandra Cox') \
    .filter(Teacher.full_name == 'Brian Brown') \
    .group_by(Teacher.full_name, Student.full_name) \
    .all()
    return result


def select_12():
    """
    Оцінки студентів у певній групі з певного предмета на останньому занятті.

    SELECT max(grade_date)
    FROM grades g
    JOIN students s on s.id = g.student_id
    WHERE g.subject_id = 2 and s.group_id  =3;

    SELECT s.id, s.fullname, g.grade, g.grade_date
    FROM grades g
    JOIN students s on g.student_id = s.id
    WHERE g.subject_id = 2 and s.group_id = 3 and g.grade_date = (
        SELECT max(grade_date)
        FROM grades g2
        JOIN students s2 on s2.id=g2.student_id
        WHERE g2.subject_id = 2 and s2.group_id = 3
    );
    """
    subquery = session.query(func.max(Grade.grade_date)) \
        .join(Student, Student.id == Grade.student_id) \
        .filter(Grade.subject_id == 2, Student.group_id == 3) \
        .subquery()

    result = session.query(
        Student.id,
        Student.full_name,
        Grade.grade,
        Grade.grade_date
    ).join(
        Grade,
        Grade.student_id == Student.id
    ).filter(
        Grade.subject_id == 2,
        Student.group_id == 3,
        Grade.grade_date == subquery
    ).all()
    return result

if __name__ == '__main__':
    #pprint(select_1())
    #pprint(select_2())
    #pprint(select_3())
    #pprint(select_4())
    #pprint(select_5())
    #pprint(select_6())
    #pprint(select_7())
    #pprint(select_8())
    #pprint(select_9())
    #pprint(select_10())
    #pprint(select_11())
    pprint(select_12())

