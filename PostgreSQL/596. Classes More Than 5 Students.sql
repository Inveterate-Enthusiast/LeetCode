Table: Courses

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| student     | varchar |
| class       | varchar |
+-------------+---------+
(student, class) is the primary key (combination of columns with unique values) for this table.
Each row of this table indicates the name of a student and the class in which they are enrolled.
 

Write a solution to find all the classes that have at least five students.

Return the result table in any order.

1.
WITH
sub AS
(SELECT class, COUNT(student) AS our_count FROM Courses GROUP BY class)
SELECT class FROM sub WHERE our_count >= 5;
2.
SELECT class FROM Courses GROUP BY class HAVING COUNT(student) >= 5;