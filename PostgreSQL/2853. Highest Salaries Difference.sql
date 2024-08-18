Table: Salaries

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| emp_name    | varchar |
| department  | varchar |
| salary      | int     |
+-------------+---------+
(emp_name, department) is the primary key (combination of unique values) for this table.
Each row of this table contains emp_name, department and salary. There will be at least one entry for the engineering and marketing departments.
Write a solution to calculate the difference between the highest salaries in the marketing and engineering department. Output the absolute difference in salaries.

Return the result table.


1.
SELECT ROUND(ABS((SELECT MAX(salary) FROM Salaries WHERE department = 'Marketing') - (SELECT MAX(salary) FROM Salaries WHERE department = 'Engineering')), 0) AS salary_difference