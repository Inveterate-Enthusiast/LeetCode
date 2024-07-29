Table: Signups

+----------------+----------+
| Column Name    | Type     |
+----------------+----------+
| user_id        | int      |
| time_stamp     | datetime |
+----------------+----------+
user_id is the column with unique values for this table.
Each row contains information about the signup time for the user with ID user_id.


Table: Confirmations

+----------------+----------+
| Column Name    | Type     |
+----------------+----------+
| user_id        | int      |
| time_stamp     | datetime |
| action         | ENUM     |
+----------------+----------+
(user_id, time_stamp) is the primary key (combination of columns with unique values) for this table.
user_id is a foreign key (reference column) to the Signups table.
action is an ENUM (category) of the type ('confirmed', 'timeout')
Each row of this table indicates that the user with ID user_id requested a confirmation message at time_stamp
and that confirmation message was either confirmed ('confirmed') or expired without confirming ('timeout').


Write a solution to find the IDs of the users that requested a confirmation message twice within a 24-hour window.
Two messages exactly 24 hours apart are considered to be within the window. The action does not affect the answer, only the request time.

Return the result table in any order.


1.
WITH with_dif AS
    (SELECT user_id, time_stamp, EXTRACT(EPOCH FROM AGE(time_stamp, LAG(time_stamp, 1) OVER(PARTITION BY user_id ORDER BY time_stamp ASC)))/60/60 AS diff
    FROM Confirmations
    ORDER BY user_id ASC, time_stamp ASC)
SELECT DISTINCT user_id
FROM with_dif
WHERE diff IS NOT NULL AND diff <= 24;