Table: Departments

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| name          | varchar |
+---------------+---------+
In SQL, id is the primary key of this table.
The table has information about the id of each department of a university.
 

Table: Students

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| name          | varchar |
| department_id | int     |
+---------------+---------+
In SQL, id is the primary key of this table.
The table has information about the id of each student at a university and the id of the department he/she studies at.
 

Find the id and the name of all students who are enrolled in departments that no longer exist.

Return the result table in any order.



1.
SELECT id, name FROM Students WHERE department_id NOT IN 
(SELECT id FROM Departments);