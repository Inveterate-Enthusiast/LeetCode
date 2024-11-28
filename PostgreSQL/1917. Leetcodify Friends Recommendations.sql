Table: Listens

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| user_id     | int     |
| song_id     | int     |
| day         | date    |
+-------------+---------+
This table may contain duplicates (In other words, there is no primary key for this table in SQL).
Each row of this table indicates that the user user_id listened to the song song_id on the day day.


Table: Friendship

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user1_id      | int     |
| user2_id      | int     |
+---------------+---------+
In SQL,(user1_id, user2_id) is the primary key for this table.
Each row of this table indicates that the users user1_id and user2_id are friends.
Note that user1_id < user2_id.


Recommend friends to Leetcodify users. We recommend user x to user y if:

Users x and y are not friends, and
Users x and y listened to the same three or more different songs on the same day.
Note that friend recommendations are unidirectional, meaning if user x and user y should be recommended to each other,
the result table should have both user x recommended to user y and user y recommended to user x.
Also, note that the result table should not contain duplicates (i.e., user y should not be recommended to user x multiple times.).

Return the result table in any order.


1.
SELECT DISTINCT
    main.user_id AS user_id,
    sub.user_id AS recommended_id
FROM Listens AS main

INNER JOIN Listens AS sub
    ON sub.song_id = main.song_id
    AND sub.day = main.day

LEFT JOIN (
    SELECT user1_id, user2_id
    FROM Friendship

    UNION ALL

    SELECT user2_id AS user1_id, user1_id AS user2_id
    FROM Friendship
) AS fri
    ON fri.user1_id = main.user_id
    AND fri.user2_id = sub.user_id

WHERE fri.user1_id IS NULL AND fri.user2_id IS NULL
AND NOT main.user_id = sub.user_id

GROUP BY main.user_id, sub.user_id, main.day
HAVING COUNT(DISTINCT main.song_id) >= 3;