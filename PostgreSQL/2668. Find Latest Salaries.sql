Table: Salary

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| emp_id        | int     |
| firstname     | varchar |
| lastname      | varchar |
| salary        | varchar |
| department_id | varchar |
+---------------+---------+
(emp_id, salary) is the primary key (combination of columns with unique values) for this table.
Each row contains employees details and their yearly salaries, however, some of the records are old and contain outdated salary information.
Write a solution to find the current salary of each employee assuming that salaries increase each year.
Output their emp_id, firstname, lastname, salary, and department_id.

Return the result table ordered by emp_id in ascending order.

1.
WITH ranked AS
    (SELECT *, DENSE_RANK() OVER(PARTITION BY emp_id ORDER BY salary DESC) AS our_rank
    FROM Salary)
SELECT emp_id, firstname, lastname, salary, department_id
FROM ranked
WHERE our_rank = 1
ORDER BY emp_id ASC;

2.
SELECT DISTINCT ON (emp_id) *
FROM Salary
ORDER BY emp_id ASC, salary DESC;