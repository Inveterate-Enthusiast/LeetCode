--Table: Project
--
--+-------------+---------+
--| Column Name | Type    |
--+-------------+---------+
--| project_id  | int     |
--| employee_id | int     |
--| workload    | int     |
--+-------------+---------+
--employee_id is the primary key (column with unique values) of this table.
--employee_id is a foreign key (reference column) to Employee table.
--Each row of this table indicates that the employee with employee_id is working on the project with
--project_id and the workload of the project.
--Table: Employees
--
--+------------------+---------+
--| Column Name      | Type    |
--+------------------+---------+
--| employee_id      | int     |
--| name             | varchar |
--| team             | varchar |
--+------------------+---------+
--employee_id is the primary key (column with unique values) of this table.
--Each row of this table contains information about one employee.
--Write a solution to find the employees who are allocated to projects with a workload that exceeds the average workload
--of all employees for their respective teams
--
--Return the result table ordered by employee_id, project_id in ascending order.
--
--
--
--1.
WITH merged AS (
    SELECT
        main.*,
        sub.name,
        AVG(main.workload) OVER(PARTITION BY sub.team) AS our_avg
    FROM Project AS main

    LEFT JOIN Employees AS sub
        ON sub.employee_id = main.employee_id
)
SELECT
    employee_id,
    project_id,
    name AS employee_name,
    workload AS project_workload
FROM merged

WHERE workload > our_avg

ORDER BY employee_id ASC, project_id ASC;