Table: Employee

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| department  | varchar |
| managerId   | int     |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the name of an employee, their department, and the id of their manager.
If managerId is null, then the employee does not have a manager.
No employee will be the manager of themself.
 

Write a solution to find managers with at least five direct reports.

Return the result table in any order.



1.
WITH grouped AS
	(SELECT managerId
	FROM Employee
	GROUP BY managerId
	HAVING COUNT(DISTINCT id) >= 5)
SELECT sub.name
FROM grouped AS main
INNER JOIN 
Employee AS sub
ON main.managerId = sub.id;