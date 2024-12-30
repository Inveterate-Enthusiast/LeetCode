--Table: Employees
--
--+---------------+---------+
--| Column Name   | Type    |
--+---------------+---------+
--| employee_id   | int     |
--| employee_name | varchar |
--| manager_id    | int     |
--| salary        | int     |
--+---------------+---------+
--employee_id is the unique identifier for this table.
--manager_id is the employee_id of the employee's manager. The CEO has a NULL manager_id.
--Write a solution to find subordinates of the CEO (both direct and indirect), along with their level in the hierarchy and their salary difference from the CEO.
--
--The result should have the following columns:
--
--The query result format is in the following example.
--
--subordinate_id: The employee_id of the subordinate
--subordinate_name: The name of the subordinate
--hierarchy_level: The level of the subordinate in the hierarchy (1 for direct reports, 2 for their direct reports, and so on)
--salary_difference: The difference between the subordinate's salary and the CEO's salary
--Return the result table ordered by hierarchy_level ascending, and then by subordinate_id ascending.



1.
WITH RECURSIVE ceo AS (
    SELECT
        *
    FROM Employees
    WHERE manager_id IS NULL
),
unioned AS (
    SELECT
        employee_id AS subordinate_id,
        employee_name AS subordinate_name,
        0 AS hierarchy_level,
        0 AS salary_difference
    FROM ceo

    UNION ALL

    SELECT
        Employees.employee_id AS subordinate_id,
        Employees.employee_name AS subordinate_name,
        unioned.hierarchy_level + 1 AS hierarchy_level,
        (Employees.salary - (SELECT salary FROM ceo)) AS salary_difference
    FROM Employees

    INNER JOIN unioned
        ON unioned.subordinate_id = Employees.manager_id
)
SELECT
    *
FROM unioned

WHERE hierarchy_level > 0

ORDER BY hierarchy_level ASC, subordinate_id ASC;