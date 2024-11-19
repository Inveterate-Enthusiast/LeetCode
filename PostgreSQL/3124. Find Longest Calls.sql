Table: Contacts

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| first_name  | varchar |
| last_name   | varchar |
+-------------+---------+
id is the primary key (column with unique values) of this table.
id is a foreign key (reference column) to Calls table.
Each row of this table contains id, first_name, and last_name.
Table: Calls

+-------------+------+
| Column Name | Type |
+-------------+------+
| contact_id  | int  |
| type        | enum |
| duration    | int  |
+-------------+------+
(contact_id, type, duration) is the primary key (column with unique values) of this table.
type is an ENUM (category) type of ('incoming', 'outgoing').
Each row of this table contains information about calls, comprising of contact_id, type, and duration in seconds.
Write a solution to find the three longest incoming and outgoing calls.

Return the result table ordered by type, duration, and first_name in descending order and duration must be formatted as HH:MM:SS.



1.
WITH merged AS (
    SELECT
        sub.first_name,
        main.type,
        TO_CHAR(CONCAT(main.duration, ' SECONDS')::INTERVAL, 'HH24:MI:SS') AS duration_formatted,
        DENSE_RANK() OVER(PARTITION BY main.type ORDER BY main.duration DESC) AS our_rank
    FROM Calls AS main

    LEFT JOIN Contacts AS sub
        ON main.contact_id = sub.id
)
SELECT
    first_name,
    type,
    duration_formatted
FROM merged

WHERE our_rank <= 3
ORDER BY type DESC, duration_formatted DESC, first_name DESC;