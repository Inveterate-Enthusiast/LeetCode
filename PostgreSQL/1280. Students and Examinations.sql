Table: Students

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| student_id    | int     |
| student_name  | varchar |
+---------------+---------+
student_id is the primary key (column with unique values) for this table.
Each row of this table contains the ID and the name of one student in the school.
 

Table: Subjects

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| subject_name | varchar |
+--------------+---------+
subject_name is the primary key (column with unique values) for this table.
Each row of this table contains the name of one subject in the school.
 

Table: Examinations

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| student_id   | int     |
| subject_name | varchar |
+--------------+---------+
There is no primary key (column with unique values) for this table. It may contain duplicates.
Each student from the Students table takes every course from the Subjects table.
Each row of this table indicates that a student with ID student_id attended the exam of subject_name.
 

Write a solution to find the number of times each student attended each exam.

Return the result table ordered by student_id and subject_name.




1.
WITH grouped AS
(SELECT main.student_id, main.student_name, sub.subject_name FROM Students AS main CROSS JOIN Subjects AS sub)
SELECT main.student_id, main.student_name, main.subject_name, COUNT(sub.student_id) AS attended_exams FROM grouped AS main LEFT JOIN Examinations AS sub
ON main.student_id = sub.student_id AND main.subject_name = sub.subject_name
GROUP BY main.student_id, main.student_name, main.subject_name
ORDER BY main.student_id, main.subject_name;