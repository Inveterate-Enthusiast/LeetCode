Table: Project

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| project_id  | int     |
| employee_id | int     |
+-------------+---------+
(project_id, employee_id) is the primary key (combination of columns with unique values) of this table.
employee_id is a foreign key (reference column) to Employee table.
Each row of this table indicates that the employee with employee_id is working on the project with project_id.
 

Table: Employee

+------------------+---------+
| Column Name      | Type    |
+------------------+---------+
| employee_id      | int     |
| name             | varchar |
| experience_years | int     |
+------------------+---------+
employee_id is the primary key (column with unique values) of this table.
Each row of this table contains information about one employee.

Write a solution to report all the projects that have the most employees.

Return the result table in any order.


1.
WITH grouped AS
(SELECT project_id, COUNT(employee_id) AS our_count FROM Project GROUP BY project_id)
SELECT project_id FROM grouped WHERE our_count = (SELECT MAX(our_count) FROM grouped);