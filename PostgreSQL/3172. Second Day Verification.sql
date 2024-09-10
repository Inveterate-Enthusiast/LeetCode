Table: emails

+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| email_id    | int      |
| user_id     | int      |
| signup_date | datetime |
+-------------+----------+
(email_id, user_id) is the primary key (combination of columns with unique values) for this table.
Each row of this table contains the email ID, user ID, and signup date.
Table: texts

+---------------+----------+
| Column Name   | Type     |
+---------------+----------+
| text_id       | int      |
| email_id      | int      |
| signup_action | enum     |
| action_date   | datetime |
+---------------+----------+
(text_id, email_id) is the primary key (combination of columns with unique values) for this table.
signup_action is an enum type of ('Verified', 'Not Verified').
Each row of this table contains the text ID, email ID, signup action, and action date.
Write a Solution to find the user IDs of those who verified their sign-up on the second day.

Return the result table ordered by user_id in ascending order.




1.
SELECT DISTINCT main.user_id
FROM emails AS main
INNER JOIN
(SELECT * FROM texts WHERE signup_action = 'Verified') AS sub
ON sub.action_date::DATE = (main.signup_date::DATE + INTERVAL '1 DAYS') AND main.email_id = sub.email_id
ORDER BY main.user_id ASC;