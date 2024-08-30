Table: Sales

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| sale_date     | date    |
| fruit         | enum    |
| sold_num      | int     |
+---------------+---------+
(sale_date, fruit) is the primary key (combination of columns with unique values) of this table.
This table contains the sales of "apples" and "oranges" sold each day.


Write a solution to report the difference between the number of apples and oranges sold each day.

Return the result table ordered by sale_date.



1.
SELECT COALESCE(main.sale_date, sub.sale_date) AS sale_date,
(COALESCE(main.sold_num, 0) - COALESCE(sub.sold_num, 0)) AS diff
FROM (SELECT * FROM Sales WHERE fruit = 'apples') AS main
FULL OUTER JOIN
(SELECT * FROM Sales WHERE fruit = 'oranges') AS sub
ON main.sale_date = sub.sale_date
ORDER BY sale_date ASC;