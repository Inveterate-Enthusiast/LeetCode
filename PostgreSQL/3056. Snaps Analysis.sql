Table: Activities

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| activity_id   | int     |
| user_id       | int     |
| activity_type | enum    |
| time_spent    | decimal |
+---------------+---------+
activity_id is column of unique values for this table.
activity_type is an ENUM (category) type of ('send', 'open').
This table contains activity id, user id, activity type and time spent.
Table: Age

+-------------+------+
| Column Name | Type |
+-------------+------+
| user_id     | int  |
| age_bucket  | enum |
+-------------+------+
user_id is the column of unique values for this table.
age_bucket is an ENUM (category) type of ('21-25', '26-30', '31-35').
This table contains user id and age group.
Write a solution to calculate the percentage of the total time spent on sending and opening snaps for each age group.
Precentage should be rounded to 2 decimal places.

Return the result table in any order.



1.
WITH merged AS (
    SELECT
        main.activity_type,
        main.time_spent,
        sub.age_bucket
    FROM Activities AS main
    LEFT JOIN Age AS sub
    ON main.user_id = sub.user_id
),
grouped AS (
    SELECT
        age_bucket,
        COALESCE(SUM(CASE WHEN activity_type = 'send' THEN time_spent END), 0) AS spend_total,
        COALESCE(SUM(CASE WHEN activity_type = 'open' THEN time_spent END), 0) AS open_total,
        SUM(time_spent) AS total
    FROM merged
    GROUP BY age_bucket
)
SELECT
    age_bucket,
    ROUND(spend_total::NUMERIC / total::NUMERIC * 100, 2) AS send_perc,
    ROUND(open_total::NUMERIC / total::NUMERIC * 100, 2) AS open_perc
FROM grouped;