Table: Sessions

+---------------------+---------+
| Column Name         | Type    |
+---------------------+---------+
| session_id          | int     |
| duration            | int     |
+---------------------+---------+
session_id is the column of unique values for this table.
duration is the time in seconds that a user has visited the application.
 

You want to know how long a user visits your application. You decided to create bins of "[0-5>", "[5-10>", "[10-15>", and "15 minutes or more" and count the number of sessions on it.

Write a solution to report the (bin, total).

Return the result table in any order.



1.
WITH our_table AS
	(SELECT '[0-5>' AS bin, 0 AS min, 5 AS max
	UNION ALL 
	SELECT '[5-10>', 5, 10
	UNION ALL
	SELECT '[10-15>', 10, 15
	UNION ALL
	SELECT '15 or more', 15, NULL)
SELECT sub.bin, COUNT(main.duration) AS total
FROM Sessions AS main
RIGHT JOIN our_table AS sub
ON (main.duration/60) >= sub.min AND 
(sub.max IS NULL OR (main.duration/60) < sub.max)
GROUP BY sub.bin;