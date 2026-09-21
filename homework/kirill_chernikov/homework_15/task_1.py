import mysql.connector as mysql
import random

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port='25060',
    database='st-onl',
    autocommit=True
)

cursor = db.cursor(dictionary=True)

create_student = """
INSERT INTO students (name, second_name)
VALUES (%s, %s);
"""
student = (f'Kirill{random.randint(1, 1000)}', f'Chernikov{random.randint(1, 1000)}')
cursor.execute(create_student, student)

student_id = cursor.lastrowid
print(f'Student_id: {student_id}')

create_book = """
INSERT INTO books (title, taken_by_student_id)
VALUES (%s,%s);
"""
books = [
    ('Алгоритмы 2026', student_id),
    ('Алгоритмы 2026 ч. 2', student_id),
    ('Алгоритмы 2026 ч. 3', student_id),
]
books_ids = {}

for book_tuple in books:
    cursor.execute(create_book, book_tuple)
    book_id = cursor.lastrowid
    books_ids[book_tuple[0]] = book_id

create_subject = """
INSERT INTO subjects (title)
VALUES (%s);
"""
subjects = [
    ('Базы Данных и SQL 2026',),
    ('Базы Данных и SQL 2026 ч. 2',),
    ('Базы Данных и SQL 2026 ч. 3',)
]
subject_ids = {}

for subject_tuple in subjects:
    cursor.execute(create_subject, subject_tuple)
    subject_id = cursor.lastrowid
    subject_ids[subject_tuple[0]] = subject_id

create_group = """
INSERT INTO `groups` (title, start_date, end_date)
VALUES (%s, %s, %s)
"""
group = ('AQA Python Class Kirill', 'Sept 2026', 'Dec 2026')
cursor.execute(create_group, group)

group_id = cursor.lastrowid

update_student = """
UPDATE students
SET group_id = %s
WHERE id = %s;
"""
update_data = (group_id, student_id)
cursor.execute(update_student, update_data)

create_lesson = """
INSERT INTO lessons (title, subject_id)
VALUES (%s, %s)
"""
lessons = [
    ('Введение в SQL 2026 ч.1', subject_ids['Базы Данных и SQL 2026']),
    ('Введение в SQL 2026 ч.2', subject_ids['Базы Данных и SQL 2026']),
    ('SQL - средний уровень 2026 ч. 1', subject_ids['Базы Данных и SQL 2026 ч. 2']),
    ('SQL - средний уровень 2026 ч. 2', subject_ids['Базы Данных и SQL 2026 ч. 2']),
    ('SQL - продвинутый уровень 2026 ч. 1', subject_ids['Базы Данных и SQL 2026 ч. 3']),
    ('SQL - продвинутый уровень 2026 ч. 2', subject_ids['Базы Данных и SQL 2026 ч. 3'])
]

lessons_ids = {}

for lesson_tuple in lessons:
    cursor.execute(create_lesson, lesson_tuple)
    lesson_id = cursor.lastrowid
    lessons_ids[lesson_tuple[0]] = lesson_id

create_mark = """
INSERT INTO marks (value, lesson_id, student_id)
VALUES (%s, %s,%s);
"""
marks = [
    (5, lessons_ids["Введение в SQL 2026 ч.1"], student_id),
    (5, lessons_ids["Введение в SQL 2026 ч.2"], student_id),
    (4, lessons_ids["SQL - средний уровень 2026 ч. 1"], student_id),
    (4, lessons_ids["SQL - средний уровень 2026 ч. 2"], student_id),
    (3, lessons_ids["SQL - продвинутый уровень 2026 ч. 1"], student_id),
    (5, lessons_ids["SQL - продвинутый уровень 2026 ч. 2"], student_id)
]
cursor.executemany(create_mark, marks)

print("----SELECT MARKS DATA-----")

select_marks = """
SELECT
    m.value,
    l.title
FROM marks m
JOIN lessons l ON l.id = m.lesson_id
JOIN students s ON s.id = m.student_id
WHERE s.id = %s
ORDER BY title;
"""
cursor.execute(select_marks, (student_id,))
student_marks = cursor.fetchall()

for mark in student_marks:
    print(mark)

print()
print("----SELECT BOOKS DATA-----")

select_books = """
SELECT b.title
FROM books b
JOIN students s ON s.id = b.taken_by_student_id
WHERE s.id = %s;
"""
cursor.execute(select_books, (student_id,))
student_books = cursor.fetchall()

for book in student_books:
    print(book)

print()
print("----SELECT STUDENT AGGREGATED DATA-----")

select_all_student_data = """
SELECT
    g.title AS group_name,
    b.title AS book_title,
    su.title AS subject,
    l.title AS lesson,
    m.value AS mark
FROM students s
JOIN `groups` g ON g.id = s.group_id
JOIN books b ON b.taken_by_student_id = s.id
JOIN marks m ON m.student_id = s.id
JOIN lessons l ON l.id = m.lesson_id
JOIN subjects su ON su.id = l.subject_id
WHERE s.id = %s;
"""
cursor.execute(select_all_student_data, (student_id,))
student_data = cursor.fetchall()

for row in student_data:
    print(row)

db.close()
