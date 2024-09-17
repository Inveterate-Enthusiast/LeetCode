Table: Contests

+--------------+------+
| Column Name  | Type |
+--------------+------+
| contest_id   | int  |
| gold_medal   | int  |
| silver_medal | int  |
| bronze_medal | int  |
+--------------+------+
contest_id is the column with unique values for this table.
This table contains the LeetCode contest ID and the user IDs of the gold, silver, and bronze medalists.
It is guaranteed that any consecutive contests have consecutive IDs and that no ID is skipped.


Table: Users

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| user_id     | int     |
| mail        | varchar |
| name        | varchar |
+-------------+---------+
user_id is the column with unique values for this table.
This table contains information about the users.


Write a solution to report the name and the mail of all interview candidates.
A user is an interview candidate if at least one of these two conditions is true:

The user won any medal in three or more consecutive contests.
The user won the gold medal in three or more different contests (not necessarily consecutive).
Return the result table in any order.


1.
WITH melted AS
    (
    SELECT contest_id, gold_medal AS user_id
    FROM Contests

    UNION ALL

    SELECT contest_id, silver_medal AS user_id
    FROM Contests

    UNION ALL

    SELECT contest_id, bronze_medal AS user_id
    FROM Contests
    ),
ranked AS
    (
    SELECT *, RANK() OVER(PARTITION BY user_id ORDER BY contest_id ASC) AS rank
    FROM melted
    ),
with_new_column AS
    (
    SELECT *, (contest_id - rank) AS diff
    FROM ranked
    ),
grouped_1 AS
    (
    SELECT DISTINCT user_id
    FROM with_new_column
    GROUP BY user_id, diff
    HAVING COUNT(*) >= 3
    ),
grouped_2 AS
    (
    SELECT DISTINCT gold_medal AS user_id
    FROM Contests
    GROUP BY gold_medal
    HAVING COUNT(DISTINCT contest_id) >= 3
    )
SELECT DISTINCT sub.name, sub.mail
FROM (
    SELECT user_id
    FROM grouped_1

    UNION ALL

    SELECT user_id
    FROM grouped_2
) AS main
LEFT JOIN
Users AS sub
ON main.user_id = sub.user_id;