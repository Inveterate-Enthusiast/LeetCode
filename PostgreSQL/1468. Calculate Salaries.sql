Table Salaries:

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| company_id    | int     |
| employee_id   | int     |
| employee_name | varchar |
| salary        | int     |
+---------------+---------+
In SQL,(company_id, employee_id) is the primary key for this table.
This table contains the company id, the id, the name, and the salary for an employee.


Find the salaries of the employees after applying taxes. Round the salary to the nearest integer.

The tax rate is calculated for each company based on the following criteria:

0% If the max salary of any employee in the company is less than $1000.
24% If the max salary of any employee in the company is in the range [1000, 10000] inclusive.
49% If the max salary of any employee in the company is greater than $10000.
Return the result table in any order.



1.
WITH taxes AS
    (SELECT company_id,
    (CASE
        WHEN MAX(salary) < 1000 THEN 0
        WHEN MAX(salary) > 10000 THEN 49
        ELSE 24
    END) AS tax
    FROM Salaries
    GROUP BY company_id)
SELECT main.company_id, main.employee_id, main.employee_name, ROUND((main.salary - (main.salary::NUMERIC * sub.tax::NUMERIC / 100))::NUMERIC, 0) AS salary
FROM Salaries AS main
LEFT JOIN
taxes AS sub
ON main.company_id = sub.company_id;