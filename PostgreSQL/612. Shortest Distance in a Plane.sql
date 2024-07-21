Table: Point2D

+-------------+------+
| Column Name | Type |
+-------------+------+
| x           | int  |
| y           | int  |
+-------------+------+
(x, y) is the primary key column (combination of columns with unique values) for this table.
Each row of this table indicates the position of a point on the X-Y plane.


The distance between two points p1(x1, y1) and p2(x2, y2) is sqrt((x2 - x1)2 + (y2 - y1)2).

Write a solution to report the shortest distance between any two points from the Point2D table.
Round the distance to two decimal points.

1.
WITH merged AS
    (SELECT main.x AS left_x, main.y AS left_y, sub.x AS right_x, sub.y AS right_y
    FROM Point2D AS main
    CROSS JOIN
    Point2D AS sub),
filtered AS
    (SELECT *,
    (((right_x - left_x)^2 + (right_y - left_y)^2) ^ (1::NUMERIC/2::NUMERIC)) AS path
    FROM merged
    WHERE NOT (right_x = left_x
    AND right_y = left_y))
SELECT ROUND((SELECT MIN(path) FROM filtered)::NUMERIC, 2) AS shortest;


2.
WITH merged AS
    (SELECT (((sub.x - main.x)^2 + (sub.y - main.y)^2) ^ (1::NUMERIC/2::NUMERIC)) AS path
    FROM Point2D AS main, Point2D AS sub
    WHERE (main.x, main.y) != (sub.x, sub.y))
SELECT ROUND(MIN(path)::NUMERIC, 2) AS shortest FROM merged;