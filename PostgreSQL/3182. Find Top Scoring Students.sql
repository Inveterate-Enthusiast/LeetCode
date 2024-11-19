Table: students

+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| student_id  | int      |
| name        | varchar  |
| major       | varchar  |
+-------------+----------+
student_id is the primary key (combination of columns with unique values) for this table.
Each row of this table contains the student ID, student name, and their major.
Table: courses

+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| course_id   | int      |
| name        | varchar  |
| credits     | int      |
| major       | varchar  |
+-------------+----------+
course_id is the primary key (combination of columns with unique values) for this table.
Each row of this table contains the course ID, course name, the number of credits for the course, and the major it belongs to.
Table: enrollments

+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| student_id  | int      |
| course_id   | int      |
| semester    | varchar  |
| grade       | varchar  |
+-------------+----------+
(student_id, course_id, semester) is the primary key (combination of columns with unique values) for this table.
Each row of this table contains the student ID, course ID, semester, and grade received.
Write a solution to find the students who have taken all courses offered in their major and have achieved a grade of A in all these courses.

Return the result table ordered by student_id in ascending order.



1.
WITH merged AS (
    SELECT
        main.student_id,
        SUM(CASE WHEN sub_2.grade = 'A' THEN 0 ELSE 1 END) AS our_check
    FROM students AS main

    LEFT JOIN courses AS sub
        ON sub.major = main.major

    LEFT JOIN enrollments AS sub_2
        ON sub_2.student_id = main.student_id
        AND sub_2.course_id = sub.course_id

    GROUP BY main.student_id
)
SELECT
    student_id
FROM merged

WHERE our_check = 0
ORDER BY student_id ASC;