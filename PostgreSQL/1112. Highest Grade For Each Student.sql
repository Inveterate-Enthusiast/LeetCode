Table: Enrollments

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| student_id    | int     |
| course_id     | int     |
| grade         | int     |
+---------------+---------+
(student_id, course_id) is the primary key (combination of columns with unique values) of this table.
grade is never NULL.


Write a solution to find the highest grade with its corresponding course for each student.
In case of a tie, you should find the course with the smallest course_id.

Return the result table ordered by student_id in ascending order.

1.
WITH ranked AS
    (SELECT *, DENSE_RANK() OVER(PARTITION BY student_id ORDER BY grade DESC, course_id ASC) AS our_rank
    FROM Enrollments)
SELECT student_id, course_id, grade
FROM ranked
WHERE our_rank = 1
ORDER BY student_id ASC;