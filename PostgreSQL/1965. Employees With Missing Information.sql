Table: Employees

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| employee_id | int     |
| name        | varchar |
+-------------+---------+
employee_id is the column with unique values for this table.
Each row of this table indicates the name of the employee whose ID is employee_id.


Table: Salaries

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| employee_id | int     |
| salary      | int     |
+-------------+---------+
employee_id is the column with unique values for this table.
Each row of this table indicates the salary of the employee whose ID is employee_id.


Write a solution to report the IDs of all the employees with missing information. The information of an employee is missing if:

--The employee's name is missing, or
--The employee's salary is missing.
Return the result table ordered by employee_id in ascending order.


1.
SELECT employee_id
FROM (
    SELECT COALESCE(main.employee_id, sub.employee_id) AS employee_id, main.name, sub.salary
    FROM Employees AS main
    FULL OUTER JOIN
    Salaries AS sub
    ON main.employee_id = sub.employee_id
)
WHERE name IS NULL OR salary IS NULL
ORDER BY employee_id ASC;