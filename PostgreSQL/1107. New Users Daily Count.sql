Table: Traffic

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| activity      | enum    |
| activity_date | date    |
+---------------+---------+
This table may have duplicate rows.
The activity column is an ENUM (category) type of ('login', 'logout', 'jobs', 'groups', 'homepage').


Write a solution to reports for every date within at most 90 days
from today, the number of users that logged in for the first time on that date. Assume today is 2019-06-30.

Return the result table in any order.


1.
WITH grouped AS
    (SELECT user_id, MIN(activity_date) AS activity_date
    FROM Traffic
    WHERE activity = 'login'
    GROUP BY user_id)
SELECT main.activity_date AS login_date, COUNT(DISTINCT sub.user_id) AS user_count
FROM (SELECT activity_date FROM Traffic WHERE activity_date >= ('2019-06-30'::DATE - INTERVAL '90 DAYS')) AS main
INNER JOIN
grouped AS sub
ON main.activity_date = sub.activity_date
GROUP BY
main.activity_date;