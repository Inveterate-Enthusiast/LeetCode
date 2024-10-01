Table: Data

+-------------+------+
| Column Name | Type |
+-------------+------+
| first_col   | int  |
| second_col  | int  |
+-------------+------+
This table may contain duplicate rows.


Write a solution to independently:

order first_col in ascending order.
order second_col in descending order.





1.
SELECT f.first_col, s.second_col
FROM
(SELECT first_col, ROW_NUMBER() OVER(ORDER BY first_col ASC) AS num FROM Data) AS f
LEFT JOIN
(SELECT second_col, ROW_NUMBER() OVER(ORDER BY second_col DESC) AS num FROM Data) AS s
ON f.num = s.num