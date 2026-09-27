import csv
import os
import mysql.connector as my_sql
from dotenv import load_dotenv

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
csv_file_path = os.path.join(homework_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')

load_dotenv()

db = my_sql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

cursor = db.cursor()

db_data_query = """SELECT
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
WHERE s.name = %s
  AND s.second_name = %s
  AND g.title = %s
  AND b.title = %s
  AND su.title = %s
  AND l.title = %s
  AND m.value = %s
"""

with open(csv_file_path, newline='') as csv_file:
    data = csv.DictReader(csv_file)

    for row in data:
        # name,second_name,group_title,book_title,subject_title,lesson_title,mark_value - имена столбцов из csv
        name, second_name, group_title, book_title, subject_title, lesson_title, mark_value = row.values()

        values = (name, second_name, group_title, book_title, subject_title, lesson_title, mark_value)

        cursor.execute(db_data_query, values)
        db_data = cursor.fetchall()

        if not db_data:
            print(f'Following data missing in DB: {row}')

db.close()
