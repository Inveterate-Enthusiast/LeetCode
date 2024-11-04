Table: Friends

+-------------+------+
| Column Name | Type |
+-------------+------+
| user_id1    | int  |
| user_id2    | int  |
+-------------+------+
(user_id1, user_id2) is the primary key (combination of columns with unique values) for this table.
Each row contains user id1, user id2, both of whom are friends with each other.
Write a solution to find all pairs of users who are friends with each other and have no mutual friends.

Return the result table ordered by user_id1, user_id2 in ascending order.


1.
WITH concated AS (
    SELECT
        user_id1 AS user_id,
        user_id2 AS friends
    FROM Friends

    UNION ALL

    SELECT
        user_id2 AS user_id,
        user_id1 AS friends
    FROM Friends
),
merged AS (
    SELECT
        user_id1,
        user_id2,
        (CASE WHEN sub1.friends = sub2.friends THEN 1 ELSE 0 END) AS our_check
    FROM Friends AS main

    LEFT JOIN concated AS sub1
        ON sub1.user_id = main.user_id1

    LEFT JOIN concated AS sub2
        ON sub2.user_id = main.user_id2
)
SELECT
    user_id1,
    user_id2
FROM merged
GROUP BY user_id1, user_id2
HAVING SUM(our_check) = 0
ORDER BY user_id1 ASC, user_id2 ASC;