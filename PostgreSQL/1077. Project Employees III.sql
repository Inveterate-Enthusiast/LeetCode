Table: Project

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| project_id  | int     |
| employee_id | int     |
+-------------+---------+
(project_id, employee_id) is the primary key (combination of columns with unique values) of this table.
employee_id is a foreign key (reference column) to Employee table.
Each row of this table indicates that the employee with employee_id is working on the project with project_id.


Table: Employee

+------------------+---------+
| Column Name      | Type    |
+------------------+---------+
| employee_id      | int     |
| name             | varchar |
| experience_years | int     |
+------------------+---------+
employee_id is the primary key (column with unique values) of this table.
Each row of this table contains information about one employee.


Write a solution to report the most experienced employees in each project. In case of a tie, report all employees with the maximum number of experience years.

Return the result table in any order.

1.
WITH merged AS
    (SELECT main.project_id, main.employee_id, sub.experience_years,
    RANK() OVER (PARTITION BY main.project_id ORDER BY sub.experience_years DESC) AS rank
    FROM Project AS main
    LEFT JOIN Employee AS sub
    ON main.employee_id = sub.employee_id)
SELECT project_id, employee_id
FROM merged
WHERE rank = 1;