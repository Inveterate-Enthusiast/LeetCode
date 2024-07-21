Table: Employee

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| employee_id   | int     |
| team_id       | int     |
+---------------+---------+
employee_id is the primary key (column with unique values) for this table.
Each row of this table contains the ID of each employee and their respective team.
 

Write a solution to find the team size of each of the employees.

Return the result table in any order.


1.
WITH grouped AS
(SELECT team_id, COUNT(employee_id) AS team_size FROM Employee GROUP BY team_id)
SELECT main.employee_id, sub.team_size FROM Employee AS main LEFT JOIN grouped AS sub ON main.team_id = sub.team_id ORDER BY main.employee_id ASC;


2.
SELECT employee_id, COUNT(employee_id) OVER (PARTITION BY team_id ORDER BY team_id ASC) AS team_size FROM Employee;