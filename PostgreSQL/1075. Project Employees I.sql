Table: Project

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| project_id  | int     |
| employee_id | int     |
+-------------+---------+
(project_id, employee_id) is the primary key of this table.
employee_id is a foreign key to Employee table.
Each row of this table indicates that the employee with employee_id is working on the project with project_id.

Table: Employee

+------------------+---------+
| Column Name      | Type    |
+------------------+---------+
| employee_id      | int     |
| name             | varchar |
| experience_years | int     |
+------------------+---------+
--employee_id is the primary key of this table. It's guaranteed that experience_years is not NULL.
Each row of this table contains information about one employee.
 

Write an SQL query that reports the average experience years of all the employees for each project, rounded to 2 digits.

Return the result table in any order.


1.
WITH merged AS
(SELECT pro.project_id, emp.experience_years FROM Project AS pro LEFT JOIN Employee AS emp ON pro.employee_id = emp.employee_id)
SELECT project_id, ROUND(AVG(experience_years), 2) AS average_years FROM merged GROUP BY project_id;

2.
SELECT pro.project_id AS project_id, ROUND(AVG(emp.experience_years)::NUMERIC, 2) AS average_years FROM Project AS pro 
LEFT JOIN Employee AS emp 
ON pro.employee_id = emp.employee_id
GROUP BY pro.project_id ORDER BY pro.project_id ASC;