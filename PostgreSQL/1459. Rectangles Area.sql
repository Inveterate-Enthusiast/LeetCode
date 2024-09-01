Table: Points

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| x_value       | int     |
| y_value       | int     |
+---------------+---------+
id is the column with unique values for this table.
Each point is represented as a 2D coordinate (x_value, y_value).


Write a solution to report all possible axis-aligned rectangles with a non-zero area that can be formed by any two points from the Points table.

Each row in the result should contain three columns (p1, p2, area) where:

--p1 and p2 are the id's of the two points that determine the opposite corners of a rectangle.
area is the area of the rectangle and must be non-zero.
Return the result table ordered by area in descending order.
If there is a tie, order them by p1 in ascending order. If there is still a tie, order them by p2 in ascending order.



1.
SELECT main.id AS p1, sub.id AS p2,
(ABS(main.x_value - sub.x_value) * ABS(main.y_value - sub.y_value)) AS area
FROM Points AS main
INNER JOIN
Points AS sub
ON main.id < sub.id
AND main.x_value != sub.x_value
AND main.y_value != sub.y_value
ORDER BY area DESC, p1 ASC, p2 ASC;