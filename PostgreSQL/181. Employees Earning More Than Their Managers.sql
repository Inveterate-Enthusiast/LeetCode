Table: Employee

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| salary      | int     |
| managerId   | int     |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the ID of an employee, their name, salary, and the ID of their manager.
 

Write a solution to find the employees who earn more than their managers.

Return the result table in any order.

!!!SOLUTION

1.
SELECT name AS Employee FROM Employee main WHERE salary > (SELECT salary FROM Employee WHERE id = main.managerId);
2.
SELECT E1.name AS Employee FROM Employee AS E1 JOIN Employee AS E2 ON E1.managerId = E2.id WHERE E1.salary > E2.salary;