Table: Steps

+-------------+------+
| Column Name | Type |
+-------------+------+
| user_id     | int  |
| steps_count | int  |
| steps_date  | date |
+-------------+------+
(user_id, steps_date) is the primary key for this table.
Each row of this table contains user_id, steps_count, and steps_date.
Write a solution to calculate 3-day rolling averages of steps for each user.

We calculate the n-day rolling average this way:

For each day, we calculate the average of n consecutive days of step counts ending on that day if available,
otherwise, n-day rolling average is not defined for it.
Output the user_id, steps_date, and rolling average. Round the rolling average to two decimal places.

Return the result table ordered by user_id, steps_date in ascending order.


1.
WITH prev AS (
    SELECT
        *,
        LAG(steps_date, 1) OVER(PARTITION BY user_id ORDER BY steps_date ASC) AS prev_date
    FROM Steps
),
dif AS (
    SELECT
        *,
        COALESCE(EXTRACT(DAY FROM AGE(steps_date, prev_date)), 0) AS dif
    FROM prev
),
condition AS (
    SELECT
        *,
        COUNT(dif) OVER(PARTITION BY user_id ORDER BY steps_date ASC ROWS BETWEEN 1 PRECEDING AND CURRENT ROW) AS total_count,
        COUNT(dif) FILTER(WHERE dif = 1) OVER(PARTITION BY user_id ORDER BY steps_date ASC ROWS BETWEEN 1 PRECEDING AND CURRENT ROW) AS one_count
    FROM dif
),
bool AS (
    SELECT
        *,
        (CASE WHEN total_count = one_count THEN 1 ELSE 0 END) AS bool
    FROM condition
),
calculate AS (
    SELECT
        *,
        ROUND(AVG(steps_count) OVER(PARTITION BY user_id ORDER BY steps_date ASC ROWS BETWEEN 2 PRECEDING AND CURRENT ROW), 2) AS rolling_average
    FROM bool
)
SELECT
    user_id,
    steps_date,
    rolling_average
FROM calculate
WHERE bool = 1
ORDER BY user_id ASC, steps_date ASC;