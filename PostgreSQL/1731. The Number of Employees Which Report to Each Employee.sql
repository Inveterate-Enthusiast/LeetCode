Table: Employees

+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| employee_id | int      |
| name        | varchar  |
| reports_to  | int      |
| age         | int      |
+-------------+----------+
employee_id is the column with unique values for this table.
This table contains information about the employees and the id of the manager they report to. Some employees do not report to anyone (reports_to is null). 
 

For this problem, we will consider a manager an employee who has at least 1 other employee reporting to them.

Write a solution to report the ids and the names of all managers, the number of employees who report directly to them, and the average age of the reports rounded to the nearest integer.

Return the result table ordered by employee_id.


1.
WITH merged AS
	(SELECT reports_to AS employee_id, COUNT(DISTINCT employee_id) AS reports_count, ROUND(AVG(age), 0) AS average_age
	FROM Employees
	WHERE reports_to IS NOT NULL
	GROUP BY reports_to)
SELECT main.employee_id, sub.name, main.reports_count, main.average_age
FROM merged AS main
LEFT JOIN
Employees AS sub
ON main.employee_id = sub.employee_id
ORDER BY main.employee_id ASC;