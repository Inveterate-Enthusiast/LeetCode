Table: Friendship

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user1_id      | int     |
| user2_id      | int     |
+---------------+---------+
(user1_id, user2_id) is the primary key (combination of columns with unique values) for this table.
Each row of this table indicates that the users user1_id and user2_id are friends.


Table: Likes

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| user_id     | int     |
| page_id     | int     |
+-------------+---------+
(user_id, page_id) is the primary key (combination of columns with unique values) for this table.
Each row of this table indicates that user_id likes page_id.


You are implementing a page recommendation system for a social media website.
Your system will recommend a page to user_id if the page is liked by at least one friend of user_id and is not liked by user_id.

Write a solution to find all the possible page recommendations for every user.
Each recommendation should appear as a row in the result table with these columns:

user_id: The ID of the user that your system is making the recommendation to.
page_id: The ID of the page that will be recommended to user_id.
friends_likes: The number of the friends of user_id that like page_id.
Return the result table in any order.


1.
WITH concated AS (
    SELECT
        main.user1_id AS user_id,
        main.user2_id AS friend,
        sub.page_id,
        (CASE WHEN sub_1.page_id IS NULL THEN 1 ELSE 0 END) AS our_bool
    FROM Friendship AS main

    INNER JOIN Likes AS sub
        ON sub.user_id = main.user2_id

    LEFT JOIN Likes AS sub_1
        ON sub_1.user_id = main.user1_id
        AND sub_1.page_id = sub.page_id

    UNION ALL

    SELECT
        main.user2_id AS user_id,
        main.user1_id AS friend,
        sub.page_id,
        (CASE WHEN sub_1.page_id IS NULL THEN 1 ELSE 0 END) AS our_bool
    FROM Friendship AS main

    INNER JOIN Likes AS sub
        ON sub.user_id = main.user1_id

    LEFT JOIN Likes AS sub_1
        ON sub_1.user_id = main.user2_id
        AND sub_1.page_id = sub.page_id
)
SELECT
    user_id,
    page_id,
    COUNT(DISTINCT friend) AS friends_likes
FROM concated

WHERE our_bool = 1
GROUP BY user_id, page_id;