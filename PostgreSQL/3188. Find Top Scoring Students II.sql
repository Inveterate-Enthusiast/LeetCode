--Table: students
--
--+-------------+----------+
--| Column Name | Type     |
--+-------------+----------+
--| student_id  | int      |
--| name        | varchar  |
--| major       | varchar  |
--+-------------+----------+
--student_id is the primary key for this table.
--Each row contains the student ID, student name, and their major.
--Table: courses
--
--+-------------+-------------------+
--| Column Name | Type              |
--+-------------+-------------------+
--| course_id   | int               |
--| name        | varchar           |
--| credits     | int               |
--| major       | varchar           |
--| mandatory   | enum              |
--+-------------+-------------------+
--course_id is the primary key for this table.
--mandatory is an enum type of ('Yes', 'No').
--Each row contains the course ID, course name, credits, major it belongs to, and whether the course is mandatory.
--Table: enrollments
--
--+-------------+----------+
--| Column Name | Type     |
--+-------------+----------+
--| student_id  | int      |
--| course_id   | int      |
--| semester    | varchar  |
--| grade       | varchar  |
--| GPA         | decimal  |
--+-------------+----------+
--(student_id, course_id, semester) is the primary key (combination of columns with unique values) for this table.
--Each row contains the student ID, course ID, semester, and grade received.
--Write a solution to find the students who meet the following criteria:
--
--Have taken all mandatory courses and at least two elective courses offered in their major.
--Achieved a grade of A in all mandatory courses and at least B in elective courses.
--Maintained an average GPA of at least 2.5 across all their courses (including those outside their major).
--Return the result table ordered by student_id in ascending order.
--
--
--
--1.
WITH merged AS (
    SELECT
        s.student_id,
        (
            CASE
                WHEN c.mandatory = 'Yes' AND COALESCE(e.grade, 'F') > 'A' THEN 1
                ELSE 0
            END
        ) AS bool_mandatory,
        (
            CASE
                WHEN c.mandatory = 'No' AND COALESCE(e.grade, 'F') <= 'B' THEN 1
                ELSE 0
            END
        ) AS bool_elective
    FROM students AS s

    INNER JOIN courses AS c
        ON c.major = s.major

    LEFT JOIN enrollments AS e
        ON e.student_id = s.student_id
        AND e.course_id = c.course_id
),
our_window AS (
    SELECT
        student_id,
        SUM(bool_mandatory) OVER(PARTITION BY student_id) AS bool_mandatory,
        SUM(bool_elective) OVER(PARTITION BY student_id) AS bool_elective
    FROM merged
)
SELECT
    main.student_id
FROM (SELECT DISTINCT student_id FROM our_window WHERE bool_mandatory = 0 AND bool_elective >= 2) AS main

INNER JOIN enrollments AS sub
    ON sub.student_id = main.student_id

GROUP BY main.student_id
HAVING AVG(sub.GPA) >= 2.5

ORDER BY main.student_id ASC;