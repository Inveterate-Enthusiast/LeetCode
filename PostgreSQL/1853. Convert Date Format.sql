Table: Days

+-------------+------+
| Column Name | Type |
+-------------+------+
| day         | date |
+-------------+------+
day is the column with unique values for this table.


Write a solution to convert each date in Days into a string formatted as "day_name, month_name day, year".

Return the result table in any order.

1.
SELECT (
TO_CHAR(day, 'FMDay, FMMonth FMDD, YYYY')
)
AS day
FROM Days;