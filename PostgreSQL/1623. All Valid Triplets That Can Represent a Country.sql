Table: SchoolA

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| student_id    | int     |
| student_name  | varchar |
+---------------+---------+
student_id is the column with unique values for this table.
Each row of this table contains the name and the id of a student in school A.
All student_name are distinct.
 

Table: SchoolB

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| student_id    | int     |
| student_name  | varchar |
+---------------+---------+
student_id is the column with unique values for this table.
Each row of this table contains the name and the id of a student in school B.
All student_name are distinct.
 

Table: SchoolC

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| student_id    | int     |
| student_name  | varchar |
+---------------+---------+
student_id is the column with unique values for this table.
Each row of this table contains the name and the id of a student in school C.
All student_name are distinct.
 

There is a country with three schools, where each student is enrolled in exactly one school. The country is joining a competition and wants to select one student from each school to represent the country such that:

member_A is selected from SchoolA,
member_B is selected from SchoolB,
member_C is selected from SchoolC, and
---The selected students' names and IDs are pairwise distinct (i.e. no two students share the same name, and no two students share the same ID).
Write a solution to find all the possible triplets representing the country under the given constraints.

Return the result table in any order.


1.
SELECT a.student_name AS member_A,
b.student_name AS member_B,
c.student_name AS member_C
FROM SchoolA AS a

INNER JOIN

SchoolB AS b
ON a.student_name != b.student_name 
AND a.student_id != b.student_id

INNER JOIN

SchoolC AS c
ON a.student_name != c.student_name 
AND b.student_name != c.student_name 
AND a.student_id != c.student_id 
AND b.student_id != c.student_id;