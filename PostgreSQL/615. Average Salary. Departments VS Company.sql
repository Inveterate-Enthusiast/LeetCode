Table: Salary

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| employee_id | int  |
| amount      | int  |
| pay_date    | date |
+-------------+------+
In SQL, id is the primary key column for this table.
Each row of this table indicates the salary of an employee in one month.
employee_id is a foreign key (reference column) from the Employee table.


Table: Employee

+---------------+------+
| Column Name   | Type |
+---------------+------+
| employee_id   | int  |
| department_id | int  |
+---------------+------+
In SQL, employee_id is the primary key column for this table.
Each row of this table indicates the department of an employee.


--Find the comparison result (higher/lower/same) of the average salary of employees in a department to the company's average salary.

Return the result table in any order.

1.
WITH avg_comp AS
    (SELECT TO_CHAR(pay_date, 'YYYY-MM') AS pay_month, AVG(amount) AS avg_comp
    FROM Salary
    GROUP BY TO_CHAR(pay_date, 'YYYY-MM')),
grouped AS
    (SELECT TO_CHAR(main.pay_date, 'YYYY-MM') AS pay_month,
            sub.department_id,
            AVG(main.amount) AS avg
    FROM Salary AS main
    LEFT JOIN
    Employee AS sub
    ON main.employee_id = sub.employee_id
    GROUP BY TO_CHAR(main.pay_date, 'YYYY-MM'), sub.department_id)
SELECT pay_month, department_id,
(CASE
    WHEN main.avg > (SELECT avg_comp FROM avg_comp AS sub WHERE sub.pay_month = main.pay_month) THEN 'higher'
    WHEN main.avg < (SELECT avg_comp FROM avg_comp AS sub WHERE sub.pay_month = main.pay_month) THEN 'lower'
    ELSE 'same'
    END) AS comparison
FROM grouped AS main;


2.
WITH avg_comp AS
    (SELECT TO_CHAR(pay_date, 'YYYY-MM') AS pay_month, AVG(amount) AS avg_comp
    FROM Salary
    GROUP BY TO_CHAR(pay_date, 'YYYY-MM')),
grouped AS
    (SELECT TO_CHAR(main.pay_date, 'YYYY-MM') AS pay_month,
            sub.department_id,
            AVG(main.amount) AS avg
    FROM Salary AS main
    LEFT JOIN
    Employee AS sub
    ON main.employee_id = sub.employee_id
    GROUP BY TO_CHAR(main.pay_date, 'YYYY-MM'), sub.department_id)
SELECT main.pay_month, main.department_id,
(CASE
    WHEN main.avg > sub.avg_comp THEN 'higher'
    WHEN main.avg < sub.avg_comp THEN 'lower'
    ELSE 'same'

END) AS comparison
FROM grouped AS main
INNER JOIN
avg_comp AS sub
USING(pay_month);