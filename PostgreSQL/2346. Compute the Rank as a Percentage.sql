Table: Students

+---------------+------+
| Column Name   | Type |
+---------------+------+
| student_id    | int  |
| department_id | int  |
| mark          | int  |
+---------------+------+
student_id contains unique values.
Each row of this table indicates a student's ID, the ID of the department in which the student enrolled, and their mark in the exam.


Write a solution to report the rank of each student in their department as a percentage, where the rank as a percentage
is computed using the following formula: (student_rank_in_the_department - 1) * 100 / (the_number_of_students_in_the_department - 1).
The percentage should be rounded to 2 decimal places. student_rank_in_the_department is determined by descending mark,
such that the student with the highest mark is rank 1. If two students get the same mark, they also get the same rank.

Return the result table in any order.


1.
WITH ranking AS (
    SELECT
        *,
        RANK() OVER(PARTITION BY department_id ORDER BY mark DESC) AS our_rank,
        COUNT(student_id) OVER(PARTITION BY department_id) AS num
    FROM Students
),
pers AS (
    SELECT
        *,
        COALESCE(
            (CASE
                WHEN (num - 1) > 0 THEN ROUND((our_rank - 1)::NUMERIC * 100 / (num - 1)::NUMERIC, 2)
                ELSE 0
            END),
            0
        )AS percentage
    FROM ranking
)
SELECT
    student_id,
    department_id,
    percentage
FROM pers
ORDER BY department_id ASC, percentage DESC;