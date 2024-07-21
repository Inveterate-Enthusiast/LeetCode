Table: Employee

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| id           | int     |
| name         | varchar |
| salary       | int     |
| departmentId | int     |
+--------------+---------+
id is the primary key (column with unique values) for this table.
departmentId is a foreign key (reference columns) of the ID from the Department table.
Each row of this table indicates the ID, name, and salary of an employee. It also contains the ID of their department.
 

Table: Department

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table. It is guaranteed that department name is not NULL.
Each row of this table indicates the ID of a department and its name.
 

Write a solution to find employees who have the highest salary in each of the departments.

Return the result table in any order.


1.
WITH ranked AS
	(SELECT *, 
	DENSE_RANK() 
	OVER(PARTITION BY departmentId ORDER BY salary ASC) AS our_rank 
	FROM Employee)
SELECT sub.name AS Department, main.name AS Employee, main.salary AS Salary
FROM ranked AS main
LEFT JOIN Department AS sub
ON main.departmentId = sub.id
WHERE main.our_rank = (SELECT MAX(our_rank) 
						FROM ranked AS sub 
						WHERE sub.departmentId = main.departmentId);