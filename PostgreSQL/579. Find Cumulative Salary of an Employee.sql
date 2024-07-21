Table: Employee

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| month       | int  |
| salary      | int  |
+-------------+------+
(id, month) is the primary key (combination of columns with unique values) for this table.
Each row in the table indicates the salary of an employee in one month during the year 2020.
 

Write a solution to calculate the cumulative salary summary for every employee in a single unified table.

The cumulative salary summary for an employee can be calculated as follows:

For each month that the employee worked, sum up the salaries in that month and the previous two months. This is their 3-month sum for that month. If an employee did not work for the company in previous months, their effective salary for those months is 0.
Do not include the 3-month sum for the most recent month that the employee worked for in the summary.
Do not include the 3-month sum for any month the employee did not work.
Return the result table ordered by id in ascending order. In case of a tie, order it by month in descending order.

CREATE TABLE Employee (
	id INT NOT NULL,
	month INT NOT NULL,
	salary INT NOT NULL
);

\COPY Employee FROM 'C:\Users\User\Desktop\Python Books\Files\LeetCode\data\csvs\579. Find Cumulative Salary of an Employee.csv' DELIMITER ';' CSV HEADER;

DROP TABLE Employee;

1.
WITH RECURSIVE months AS
	(SELECT 1 AS month
	UNION ALL
	SELECT month + 1 AS month
	FROM months WHERE month < 12),
ids AS
	(SELECT DISTINCT id
	FROM Employee),
cross_merged AS
	(SELECT main.month, sub.id
	FROM months AS main
	CROSS JOIN
	ids AS sub),
NewEmployee AS
	(SELECT main.id, main.month, COALESCE(sub.salary, 0) AS salary
	FROM cross_merged AS main
	LEFT JOIN 
	Employee AS sub
	ON main.id = sub.id AND main.month = sub.month),
sub_ans AS
	(SELECT id, month, 
	SUM(salary) 
	OVER (PARTITION BY id ORDER BY month ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS Salary
	FROM NewEmployee)
SELECT main.id, main.month, sub.Salary
FROM Employee AS main
LEFT JOIN sub_ans AS sub
ON main.id = sub.id AND main.month = sub.month
WHERE main.month != 
	(SELECT MAX(month) 
	FROM Employee AS sub 
	WHERE main.id = sub.id)
ORDER BY id ASC, month DESC;

2.
WITH RECURSIVE months AS
	(SELECT 1 AS month, id, COALESCE((SELECT salary FROM Employee AS sub WHERE sub.id = main.id AND sub.month = 1), 0) AS salary
	FROM (SELECT DISTINCT id FROM Employee) AS main
	UNION ALL
	SELECT main.month + 1, main.id, COALESCE((SELECT salary FROM Employee AS sub WHERE sub.id = main.id AND sub.month = main.month + 1), 0) AS salary
	FROM months AS main
	WHERE main.month < 12),
window_sub AS
	(SELECT id, month, 
	SUM(salary) OVER (PARTITION BY id ORDER BY month ASC ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) 
	AS Salary
	FROM months)
SELECT * 
FROM window_sub AS main
WHERE main.month IN (SELECT month FROM Employee AS sub WHERE main.id = sub.id) 
AND main.month != (SELECT MAX(month) FROM Employee AS sub WHERE main.id = sub.id)
ORDER BY id ASC, month DESC;

3. -- моё окончательное решение
WITH RECURSIVE months AS
	(SELECT 1 AS month, id
	FROM (SELECT DISTINCT id FROM Employee) AS sub
	UNION ALL
	SELECT month + 1, id
	FROM months
	WHERE month < 12),
cross_merged AS
	(SELECT main.id, main.month, COALESCE(sub.salary, 0) AS salary
	FROM months AS main
	LEFT JOIN Employee AS sub
	ON main.id = sub.id AND main.month = sub.month),
window_sub AS
	(SELECT id, month,
	SUM(salary) OVER (PARTITION BY id ORDER BY month ASC ROWS BETWEEN 2 PRECEDING AND CURRENT ROW)
	AS salary
	FROM cross_merged)
SELECT *
FROM window_sub AS main
WHERE main.month IN (SELECT month FROM Employee AS sub WHERE sub.id = main.id)
AND main.month != (SELECT MAX(month) FROM Employee AS sub WHERE sub.id = main.id)
ORDER BY id ASC, month DESC;

4.
SELECT id, month, 
	(salary + 
	COALESCE((SELECT salary FROM Employee AS sub WHERE sub.id = main.id AND sub.month = (main.month - 1)), 0) + 
	COALESCE((SELECT salary FROM Employee AS sub WHERE sub.id = main.id AND sub.month = (main.month - 2)), 0))
	AS Salary
FROM Employee AS main
WHERE month != (SELECT MAX(month) FROM Employee AS sub WHERE main.id = sub.id)
ORDER BY id ASC, month DESC;