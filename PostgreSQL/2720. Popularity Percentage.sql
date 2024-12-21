--Table: Friends
--
--+-------------+------+
--| Column Name | Type |
--+-------------+------+
--| user1       | int  |
--| user2       | int  |
--+-------------+------+
--(user1, user2) is the primary key (combination of unique values) of this table.
--Each row contains information about friendship where user1 and user2 are friends.
--Write a solution to find the popularity percentage for each user on Meta/Facebook. The popularity percentage is defined as the total number of friends the user has divided by the total number of users on the platform, then converted into a percentage by multiplying by 100, rounded to 2 decimal places.
--
--Return the result table ordered by user1 in ascending order.


--1.
WITH unioned AS (
    SELECT
        user1,
        user2 AS friends
    FROM Friends

    UNION ALL

    SELECT
        user2 AS user1,
        user1 AS friends
    FROM Friends
)
SELECT
    main.user1,
    ROUND(COUNT(DISTINCT main.friends)::NUMERIC / MAX(sub.users)::NUMERIC * 100, 2) AS percentage_popularity
FROM unioned AS main

LEFT JOIN (SELECT COUNT(DISTINCT user1) AS users FROM unioned) AS sub
    ON TRUE
GROUP BY main.user1
ORDER BY main.user1 ASC;