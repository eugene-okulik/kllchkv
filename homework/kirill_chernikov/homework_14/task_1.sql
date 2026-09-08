-- student

INSERT INTO students (name, second_name)
VALUES ('Kirill', 'Chernikov');

-- books

INSERT INTO books (title, taken_by_student_id)
VALUES (
    'Алгоритмы',
    (
        SELECT id
        FROM students
        WHERE name = 'Kirill'
          AND second_name = 'Chernikov'
    )
);

INSERT INTO books (title, taken_by_student_id)
VALUES (
    'Алгоритмы ч. 2',
    (
        SELECT id
        FROM students
        WHERE name = 'Kirill'
          AND second_name = 'Chernikov'
    )
);

INSERT INTO books (title, taken_by_student_id)
VALUES (
    'Алгоритмы ч. 3',
    (
        SELECT id
        FROM students
        WHERE name = 'Kirill'
          AND second_name = 'Chernikov'
    )
);

-- subjects

INSERT INTO subjects (title)
VALUES ('Базы Данных и SQL');

INSERT INTO subjects (title)
VALUES ('Базы Данных и SQL ч. 2');

INSERT INTO subjects (title)
VALUES ('Базы Данных и SQL ч. 3');

-- groups

INSERT INTO `groups` (title, start_date, end_date)
VALUES ('AQA Python Class K', 'July 2026', 'December 2026');

UPDATE students
SET group_id = (
    SELECT id
    FROM `groups`
    WHERE title = 'AQA Python Class K'
)
WHERE name = 'Kirill'
  AND second_name = 'Chernikov';

-- lessons

INSERT INTO lessons (title, subject_id)
VALUES (
    'Введение в SQL ч.1',
    (
        SELECT id
        FROM subjects
        WHERE title = 'Базы Данных и SQL'
    )
);

INSERT INTO lessons (title, subject_id)
VALUES (
    'Введение в SQL ч.2',
    (
        SELECT id
        FROM subjects
        WHERE title = 'Базы Данных и SQL'
    )
);

INSERT INTO lessons (title, subject_id)
VALUES (
    'SQL - средний уровень ч. 1',
    (
        SELECT id
        FROM subjects
        WHERE title = 'Базы Данных и SQL ч. 2'
    )
);

INSERT INTO lessons (title, subject_id)
VALUES (
    'SQL - средний уровень ч. 2',
    (
        SELECT id
        FROM subjects
        WHERE title = 'Базы Данных и SQL ч. 2'
    )
);

INSERT INTO lessons (title, subject_id)
VALUES (
    'SQL - продвинутый уровень ч. 1',
    (
        SELECT id
        FROM subjects
        WHERE title = 'Базы Данных и SQL ч. 3'
    )
);

INSERT INTO lessons (title, subject_id)
VALUES (
    'SQL - продвинутый уровень ч. 2',
    (
        SELECT id
        FROM subjects
        WHERE title = 'Базы Данных и SQL ч. 3'
    )
);

-- marks

INSERT INTO marks (value, lesson_id, student_id)
VALUES (
    5,
    (
        SELECT id
        FROM lessons
        WHERE title = 'Введение в SQL ч.1'
    ),
    (
        SELECT id
        FROM students
        WHERE name = 'Kirill'
          AND second_name = 'Chernikov'
    )
);

INSERT INTO marks (value, lesson_id, student_id)
VALUES (
    5,
    (
        SELECT id
        FROM lessons
        WHERE title = 'Введение в SQL ч.2'
    ),
    (
        SELECT id
        FROM students
        WHERE name = 'Kirill'
          AND second_name = 'Chernikov'
    )
);

INSERT INTO marks (value, lesson_id, student_id)
VALUES (
    4,
    (
        SELECT id
        FROM lessons
        WHERE title = 'SQL - средний уровень ч. 1'
    ),
    (
        SELECT id
        FROM students
        WHERE name = 'Kirill'
          AND second_name = 'Chernikov'
    )
);

INSERT INTO marks (value, lesson_id, student_id)
VALUES (
    5,
    (
        SELECT id
        FROM lessons
        WHERE title = 'SQL - средний уровень ч. 2'
    ),
    (
        SELECT id
        FROM students
        WHERE name = 'Kirill'
          AND second_name = 'Chernikov'
    )
);

INSERT INTO marks (value, lesson_id, student_id)
VALUES (
    3,
    (
        SELECT id
        FROM lessons
        WHERE title = 'SQL - продвинутый уровень ч. 1'
    ),
    (
        SELECT id
        FROM students
        WHERE name = 'Kirill'
          AND second_name = 'Chernikov'
    )
);

INSERT INTO marks (value, lesson_id, student_id)
VALUES (
    4,
    (
        SELECT id
        FROM lessons
        WHERE title = 'SQL - продвинутый уровень ч. 2'
    ),
    (
        SELECT id
        FROM students
        WHERE name = 'Kirill'
          AND second_name = 'Chernikov'
    )
);

-- selects

SELECT
    m.value,
    l.title
FROM marks m
JOIN lessons l ON l.id = m.lesson_id
JOIN students s ON s.id = m.student_id
WHERE s.name = 'Kirill'
  AND s.second_name = 'Chernikov'
ORDER BY title;

SELECT b.title
FROM books b
JOIN students s ON s.id = b.taken_by_student_id
WHERE s.name = 'Kirill'
  AND s.second_name = 'Chernikov';

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
WHERE s.name = 'Kirill'
  AND s.second_name = 'Chernikov';