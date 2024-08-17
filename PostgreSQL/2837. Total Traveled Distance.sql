Table: Users

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| user_id     | int     |
| name        | varchar |
+-------------+---------+
user_id is the column with unique values for this table.
Each row of this table contains user id and name.
Table: Rides

+--------------+------+
| Column Name  | Type |
+--------------+------+
| ride_id      | int  |
| user_id      | int  |
| distance     | int  |
+--------------+------+
ride_id is the column of unique values for this table.
Each row of this table contains ride id, user id, and traveled distance.
Write a solution to calculate the distance traveled by each user.
--If there is a user who hasn't completed any rides, then their distance should be considered as 0.
Output the user_id, name and total traveled distance.

Return the result table ordered by user_id in ascending order.


1.
WITH grouped AS
    (SELECT user_id, SUM(distance) AS distance
    FROM Rides
    GROUP BY user_id)
SELECT main.user_id, main.name, COALESCE(sub.distance, 0) AS "traveled distance"
FROM Users AS main
LEFT JOIN
grouped AS sub
ON main.user_id = sub.user_id
ORDER BY main.user_id ASC;