Table: Employee

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.
 

Write a solution to find the second highest salary from the Employee table. If there is no second highest salary, return null (return None in Pandas).

CREATE TABLE Employee (
		id INT NOT NULL,
		salary INT NOT NULL
);

\COPY Employee FROM 'C:\Users\User\Desktop\Python Books\Files\LeetCode\data\csvs\176. Second Highest Salary.csv' DELIMITER ';' CSV HEADER;

DROP TABLE Employee;

1.
SELECT MAX(sub.salary) AS SecondHighestSalary FROM Employee AS main INNER JOIN Employee AS sub ON main.salary > sub.salary;

2.
WITH grouped AS
(SELECT DISTINCT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS rank FROM Employee)
SELECT (SELECT salary FROM grouped WHERE rank = 2) AS SecondHighestSalary;

