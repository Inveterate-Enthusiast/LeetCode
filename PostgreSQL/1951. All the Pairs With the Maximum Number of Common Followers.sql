Table: Relations

+-------------+------+
| Column Name | Type |
+-------------+------+
| user_id     | int  |
| follower_id | int  |
+-------------+------+
(user_id, follower_id) is the primary key (combination of columns with unique values) for this table.
Each row of this table indicates that the user with ID follower_id is following the user with ID user_id.


Write a solution to find all the pairs of users with the maximum number of common followers.
In other words, if the maximum number of common followers between any two users is maxCommon,
then you have to return all pairs of users that have maxCommon common followers.

The result table should contain the pairs user1_id and user2_id where user1_id < user2_id.

Return the result table in any order.


1.
WITH merged AS
    (
    SELECT main.user_id AS user1_id, sub.user_id AS user2_id, main.follower_id
    FROM Relations AS main
    INNER JOIN
    Relations AS sub
    ON main.follower_id = sub.follower_id AND main.user_id < sub.user_id
    ),
grouped AS
    (
    SELECT user1_id, user2_id, COUNT(*) AS count
    FROM merged
    GROUP BY user1_id, user2_id
    )
SELECT user1_id, user2_id
FROM grouped
WHERE count = (SELECT MAX(count) FROM grouped);