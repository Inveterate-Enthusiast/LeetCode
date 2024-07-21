Table: Point

+-------------+------+
| Column Name | Type |
+-------------+------+
| x           | int  |
+-------------+------+
In SQL, x is the primary key column for this table.
Each row of this table indicates the position of a point on the X-axis.
 

Find the shortest distance between any two points from the Point table.

The result format is in the following example.

1.
WITH sub AS
(SELECT x FROM Point ORDER BY x ASC),
short_sub AS
(SELECT x, x - LAG(x, 1) OVER() AS shortest FROM sub)
SELECT DISTINCT shortest FROM short_sub ORDER BY shortest ASC LIMIT 1;
2.
SELECT x - LAG(x, 1) OVER(ORDER BY x ASC) AS shortest FROM Point ORDER BY shortest ASC LIMIT 1;
3.
SELECT MIN(main.x - sub.x) AS shortest FROM Point AS main INNER JOIN Point AS sub ON main.x <> sub.x WHERE main.x > sub.x;
4.
SELECT MIN(ABS(main.x - sub.x)) AS shortest FROM Point AS main INNER JOIN Point AS sub ON main.x != sub.x;