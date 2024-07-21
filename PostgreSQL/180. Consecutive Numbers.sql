Table: Logs

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| num         | varchar |
+-------------+---------+
In SQL, id is the primary key for this table.
id is an autoincrement column.
 

Find all numbers that appear at least three times consecutively.

Return the result table in any order.

1.
WITH RECURSIVE ranked AS -- хорошее решение, но в задаче сломан id, нужно работать по нему, а не по строкам
	(SELECT *,
	ROW_NUMBER() OVER (ORDER BY id ASC) AS row 
	FROM Logs),
recursion AS
	(SELECT id, num, row, 1 AS our_count
	FROM ranked
	WHERE row = 1
	
	UNION ALL
	
	SELECT sub.id, sub.num, sub.row, (CASE WHEN main.num = sub.num THEN main.our_count + 1 ELSE 1 END) AS our_count
	FROM recursion AS main
	INNER JOIN ranked AS sub
	ON sub.row = (main.row + 1))
SELECT num AS ConsecutiveNums
FROM recursion
GROUP BY num
HAVING MAX(our_count) >= 3;

2.
WITH RECURSIVE updated AS
	(SELECT id, num
	FROM Logs WHERE id = (SELECT MIN (id) FROM Logs)
	
	UNION ALL
	
	SELECT id + 1, COALESCE((SELECT num FROM Logs AS sub WHERE sub.id = main.id+1), NULL)
	FROM updated AS main
	WHERE id < (SELECT MAX(id) FROM Logs)),
recursion AS
	(SELECT id, num, 1 AS our_count
	FROM updated
	WHERE id = (SELECT MIN(id) FROM updated)
	
	UNION ALL
	
	SELECT sub.id, sub.num, 
	(CASE WHEN main.num = sub.num THEN main.our_count + 1 ELSE 1 END) AS our_count
	FROM recursion AS main
	INNER JOIN
	updated AS sub
	ON sub.id = (main.id + 1))
SELECT num AS ConsecutiveNums
FROM recursion
WHERE num IS NOT NULL
GROUP BY num
HAVING MAX(our_count) >= 3;