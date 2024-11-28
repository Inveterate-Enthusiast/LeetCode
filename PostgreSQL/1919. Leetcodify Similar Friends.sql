Table: Listens

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| user_id     | int     |
| song_id     | int     |
| day         | date    |
+-------------+---------+
This table may contain duplicate rows.
Each row of this table indicates that the user user_id listened to the song song_id on the day day.


Table: Friendship

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user1_id      | int     |
| user2_id      | int     |
+---------------+---------+
(user1_id, user2_id) is the primary key (combination of columns with unique values) for this table.
Each row of this table indicates that the users user1_id and user2_id are friends.
Note that user1_id < user2_id.


Write a solution to report the similar friends of Leetcodify users. A user x and user y are similar friends if:

Users x and y are friends, and
Users x and y listened to the same three or more different songs on the same day.
Return the result table in any order. Note that you must return the similar pairs of friends the same way
they were represented in the input (i.e., always user1_id < user2_id).


1.
SELECT DISTINCT
    main.user_id AS user1_id,
    sub.user_id AS user2_id
FROM Listens AS main

INNER JOIN Listens AS sub
    ON sub.song_id = main.song_id
    AND sub.day = main.day

INNER JOIN (
    SELECT user1_id, user2_id
    FROM Friendship

    UNION ALL

    SELECT user2_id AS user1_id, user1_id AS user2_id
    FROM Friendship
) AS fri
    ON fri.user1_id = main.user_id
    AND fri.user2_id = sub.user_id

WHERE main.user_id < sub.user_id

GROUP BY main.user_id, sub.user_id, main.day
HAVING COUNT(DISTINCT main.song_id) >= 3;