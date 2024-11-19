Table: employees

+------------------+---------+
| Column Name      | Type    |
+------------------+---------+
| emp_id           | int     |
| salary           | int     |
| dept             | varchar |
+------------------+---------+
emp_id is the unique key for this table.
Each row of this table contains information about an employee including their ID, salary, and department.
Write a solution to find the employees who earn the second-highest salary in each department.
If multiple employees have the second-highest salary, include all employees with that salary.

Return the result table ordered by emp_id in ascending order.


1.
WITH ranked AS (
    SELECT
        *,
        DENSE_RANK() OVER(PARTITION BY dept ORDER BY salary DESC) AS our_rank
    FROM employees
)
SELECT
    emp_id,
    dept
FROM ranked
WHERE our_rank = 2
ORDER BY emp_id ASC;