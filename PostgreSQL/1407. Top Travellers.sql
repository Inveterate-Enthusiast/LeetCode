Table: Users

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| name          | varchar |
+---------------+---------+
id is the column with unique values for this table.
name is the name of the user.
 

Table: Rides

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| user_id       | int     |
| distance      | int     |
+---------------+---------+
id is the column with unique values for this table.
user_id is the id of the user who traveled the distance "distance".
 

Write a solution to report the distance traveled by each user.

Return the result table ordered by travelled_distance in descending order, if two or more users traveled the same distance, order them by their name in ascending order.



1.
WITH grouped AS
	(SELECT user_id AS id, SUM(distance) AS travelled_distance FROM Rides GROUP BY user_id)
SELECT sub.name, COALESCE(main.travelled_distance, 0) AS travelled_distance
FROM grouped AS main 
RIGHT JOIN Users AS sub 
ON main.id = sub.id
ORDER BY travelled_distance DESC, name ASC;