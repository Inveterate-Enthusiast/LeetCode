Table: Student

+---------------------+---------+
| Column Name         | Type    |
+---------------------+---------+
| student_id          | int     |
| student_name        | varchar |
+---------------------+---------+
student_id is the primary key (column with unique values) for this table.
student_name is the name of the student.


Table: Exam

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| exam_id       | int     |
| student_id    | int     |
| score         | int     |
+---------------+---------+
(exam_id, student_id) is the primary key (combination of columns with unique values) for this table.
Each row of this table indicates that the student with student_id had a score points in the exam with id exam_id.


A quiet student is the one who took at least one exam and did not score the highest or the lowest score.

Write a solution to report the students (student_id, student_name) being quiet in all exams. Do not return the student who has never taken any exam.

Return the result table ordered by student_id.



1.
WITH merged AS (
    SELECT
        main.student_id,
        main.student_name,
        sub.score,
        MIN(sub.score) OVER(PARTITION BY sub.exam_id) AS our_min,
        MAX(sub.score) OVER(PARTITION BY sub.exam_id) AS our_max
    FROM Student AS main

    INNER JOIN Exam AS sub
        ON main.student_id = sub.student_id
),
bool AS (
    SELECT
        student_id,
        student_name,
        (CASE WHEN (score > our_min) AND (score < our_max) THEN 0 ELSE 1 END) AS bool
    FROM merged
)
SELECT
    student_id,
    student_name
FROM bool
GROUP BY student_id, student_name
HAVING SUM(bool) = 0
ORDER BY student_id ASC;