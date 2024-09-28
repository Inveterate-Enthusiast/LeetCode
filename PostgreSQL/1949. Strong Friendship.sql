Table: Friendship

+-------------+------+
| Column Name | Type |
+-------------+------+
| user1_id    | int  |
| user2_id    | int  |
+-------------+------+
(user1_id, user2_id) is the primary key (combination of columns with unique values) for this table.
Each row of this table indicates that the users user1_id and user2_id are friends.
Note that user1_id < user2_id.


A friendship between a pair of friends x and y is strong if x and y have at least three common friends.

Write a solution to find all the strong friendships.

Note that the result table should not contain duplicates with user1_id < user2_id.

Return the result table in any order.



1.
WITH crossed AS
    (
    SELECT user1_id AS id, user2_id AS friend
    FROM Friendship

    UNION ALL

    SELECT user2_id AS id, user1_id AS friend
    FROM Friendship
    ),
common AS
    (
    SELECT main.id AS user1_id, main.friend, sub.id AS user2_id
    FROM crossed AS main
    INNER JOIN
    crossed AS sub
    ON main.id < sub.id AND main.friend = sub.friend
    INNER JOIN crossed AS subsub
    ON main.id = subsub.id AND sub.id = subsub.friend
    )
SELECT user1_id, user2_id, COUNT(*) AS common_friend
FROM common
GROUP BY user1_id, user2_id
HAVING COUNT(*) >= 3;