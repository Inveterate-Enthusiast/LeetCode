Table: Employees

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| employee_id   | int     |
| employee_name | varchar |
| manager_id    | int     |
+---------------+---------+
employee_id is the column of unique values for this table.
Each row of this table indicates that the employee with ID employee_id and name employee_name reports his work to his/her direct manager with manager_id
The head of the company is the employee with employee_id = 1.


Write a solution to find employee_id of all employees that directly or indirectly report their work to the head of the company.

The indirect relation between managers will not exceed three managers as the company is small.

Return the result table in any order.


1.
WITH RECURSIVE unioned AS
    (SELECT employee_id, manager_id, 1 AS num
    FROM Employees
    WHERE manager_id = 1 AND employee_id != 1

    UNION ALL

    SELECT sub.employee_id, sub.manager_id, (main.num + 1) AS num
    FROM unioned AS main
    INNER JOIN
    Employees AS sub
    ON main.employee_id = sub.manager_id
    WHERE main.num + 1 <= 3)
SELECT DISTINCT employee_id
FROM unioned;