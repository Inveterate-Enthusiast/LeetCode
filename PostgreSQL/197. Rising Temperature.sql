Table: Weather

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| recordDate    | date    |
| temperature   | int     |
+---------------+---------+
id is the column with unique values for this table.
There are no different rows with the same recordDate.
This table contains information about the temperature on a certain day.
 

Write a solution to find all dates Id with higher temperatures compared to its previous dates (yesterday).

Return the result table in any order.

!!!SOLUTION

1.
SELECT main.id FROM Weather AS main JOIN Weather AS sub ON sub.recordDate = (main.recordDate - INTERVAL '1 DAY') AND main.temperature > sub.temperature;
2.
SELECT main.id FROM Weather AS main, Weather AS sub WHERE AGE(main.recordDate, sub.recordDate) = '1 DAY' AND main.temperature > sub.temperature;
3. - неправильный, требуется доработка
SELECT main.id FROM weather AS main
LEFT JOIN (
	SELECT sub1.id, sub1.recordDate, sub1.temperature, MAX(sub2.recordDate) AS prevRecordDate FROM weather AS sub1 LEFT JOIN weather AS sub2 ON sub1.recordDate > sub2.recordDate GROUP BY sub1.id, sub1.recordDate, sub1.temperature
) AS prev
ON main.recordDate = prev.recordDate WHERE prev.prevRecordDate IS NOT NULL AND main.temperature > (
	SELECT temperature FROM weather WHERE recordDate = prev.prevRecordDate
);