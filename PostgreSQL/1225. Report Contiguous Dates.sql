Table: Failed

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| fail_date    | date    |
+--------------+---------+
fail_date is the primary key (column with unique values) for this table.
This table contains the days of failed tasks.


Table: Succeeded

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| success_date | date    |
+--------------+---------+
success_date is the primary key (column with unique values) for this table.
This table contains the days of succeeded tasks.


A system is running one task every day. Every task is independent of the previous tasks. The tasks can fail or succeed.

Write a solution to report the period_state for each continuous interval of days in the period from 2019-01-01 to 2019-12-31.

period_state is 'failed' if tasks in this interval failed or 'succeeded' if tasks in this interval succeeded. Interval of days are retrieved as start_date and end_date.

Return the result table ordered by start_date.


1.
WITH unioned AS (
    SELECT
        fail_date AS date,
        'failed' AS state
    FROM Failed

    UNION ALL

    SELECT
        success_date AS date,
        'succeeded' AS state
    FROM Succeeded
),
prev_state AS (
    SELECT
        *,
        LAG(state, 1) OVER(ORDER BY date ASC) AS prev_state
    FROM unioned
    WHERE date BETWEEN '2019-1-1'::DATE AND '2019-12-31'::DATE
    ORDER BY prev_state
),
sub AS (
    SELECT
        *,
        (CASE WHEN NOT state = COALESCE(prev_state, state) THEN 1 ELSE 0 END) AS bool
    FROM prev_state
),
with_groups AS (
    SELECT
        *,
        SUM(bool) OVER(ORDER BY date ASC) AS groups
    FROM sub
)
SELECT
    MAX(state) AS period_state,
    MIN(date) AS start_date,
    MAX(date) AS end_date
FROM with_groups
GROUP BY groups
ORDER BY MIN(date) ASC;