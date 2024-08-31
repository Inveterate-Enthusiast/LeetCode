Table: Accounts

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| name          | varchar |
+---------------+---------+
id is the primary key (column with unique values) for this table.
This table contains the account id and the user name of each account.


Table: Logins

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| login_date    | date    |
+---------------+---------+
This table may contain duplicate rows.
This table contains the account id of the user who logged in and the login date. A user may log in multiple times in the day.


Active users are those who logged in to their accounts for five or more consecutive days.

Write a solution to find the id and the name of active users.

Return the result table ordered by id.


1.
WITH ranked AS
    (
    SELECT DISTINCT id, login_date,
    ((EXTRACT(EPOCH FROM login_date) - EXTRACT(EPOCH FROM MIN(login_date) OVER(PARTITION BY id)))::NUMERIC / (60 * 60 * 24)::NUMERIC) AS days,
    (DENSE_RANK() OVER(PARTITION BY id ORDER BY login_date ASC)) AS our_rank
    FROM Logins
    ),
diffed AS
    (
    SELECT id, (days - our_rank) AS diff
    FROM ranked
    )
SELECT main.id, sub.name
FROM
    (SELECT DISTINCT id
    FROM diffed
    GROUP BY id, diff
    HAVING COUNT(*) >= 5) AS main
LEFT JOIN
Accounts AS sub
ON main.id = sub.id
ORDER BY main.id ASC;