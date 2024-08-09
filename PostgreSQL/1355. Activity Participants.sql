Table: Friends

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| name          | varchar |
| activity      | varchar |
+---------------+---------+
id is the id of the friend and the primary key for this table in SQL.
name is the name of the friend.
activity is the name of the activity which the friend takes part in.


Table: Activities

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| name          | varchar |
+---------------+---------+
In SQL, id is the primary key for this table.
name is the name of the activity.


Find the names of all the activities with neither the maximum nor the minimum number of participants.

Each activity in the Activities table is performed by any person in the table Friends.

Return the result table in any order.



1.
WITH grouped AS
    (SELECT activity, COUNT(id) AS our_count
    FROM Friends
    GROUP BY activity),
merged AS
    (SELECT main.name AS activity, COALESCE(sub.our_count, 0) AS our_count
    FROM Activities AS main
    LEFT JOIN
    grouped AS sub
    ON main.name = sub.activity)
SELECT activity
FROM merged
WHERE our_count != (SELECT MIN(our_count) FROM merged)
AND our_count != (SELECT MAX(our_count) FROM merged);