Table: Employees

+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| employee_id | int      |
| name        | varchar  |
| manager_id  | int      |
| salary      | int      |
+-------------+----------+
In SQL, employee_id is the primary key for this table.
This table contains information about the employees, their salary, and the ID of their manager. Some employees do not have a manager (manager_id is null).


Find the IDs of the employees whose salary is strictly less than $30000 and whose manager left the company.
When a manager leaves the company, their information is deleted from the Employees table, but the reports still have their manager_id set to the manager that left.

Return the result table ordered by employee_id.


1.
WITH sub AS
    (SELECT main.*, (CASE WHEN sub.employee_id IS NULL THEN 1 ELSE 0 END) AS bool
    FROM Employees AS main
    LEFT JOIN
    Employees AS sub
    ON main.manager_id = sub.employee_id
    WHERE main.salary < 30000
    AND main.manager_id IS NOT NULL)
SELECT employee_id
FROM sub
WHERE bool = 1
ORDER BY employee_id ASC;