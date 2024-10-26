Table: Employees

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| emp_id      | int     |
| emp_name    | varchar |
| dep_id      | int     |
| position    | varchar |
+-------------+---------+
emp_id is column of unique values for this table.
This table contains emp_id, emp_name, dep_id, and position.
Write a solution to find the name of the manager from the largest department.
There may be multiple largest departments when the number of employees in those departments is the same.

Return the result table sorted by dep_id in ascending order.

1.
WITH grouped AS (
    SELECT
        dep_id,
        COUNT(emp_id) AS count
    FROM Employees
    GROUP BY dep_id
)
SELECT
    sub.emp_name AS manager_name,
    main.dep_id
FROM grouped AS main
LEFT JOIN (SELECT * FROM Employees WHERE position = 'Manager') AS sub
ON sub.dep_id = main.dep_id
WHERE main.count = (SELECT MAX(count) FROM grouped)
ORDER BY main.dep_id ASC;