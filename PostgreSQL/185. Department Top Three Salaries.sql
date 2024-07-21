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
departmentId is a foreign key (reference column) of the ID from the Department table.
Each row of this table indicates the ID, name, and salary of an employee. It also contains the ID of their department.
 

Table: Department

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the ID of a department and its name.
 

--A company's executives are interested in seeing who earns the most money in each of the company's departments. A high earner in a department is an employee who has a salary in the top three unique salaries for that department.

Write a solution to find the employees who are high earners in each of the departments.



1.
WITH rank_salary AS
	(SELECT departmentId, id, name, salary, DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS rank_salary FROM Employee)
SELECT sub.name AS Department, main.name AS Employee, main.salary AS Salary
FROM rank_salary AS main
LEFT JOIN Department AS sub
ON main.departmentId = sub.id
WHERE main.rank_salary IN (1, 2, 3)
ORDER BY Salary DESC;
