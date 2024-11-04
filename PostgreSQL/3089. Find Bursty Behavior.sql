Table: Posts

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| post_id     | int     |
| user_id     | int     |
| post_date   | date    |
+-------------+---------+
post_id is the primary key (column with unique values) for this table.
Each row of this table contains post_id, user_id, and post_date.
Write a solution to find users who demonstrate bursty behavior in their posting patterns during February 2024.
--Bursty behavior is defined as any period of 7 consecutive days where a user's posting frequency is at least twice
to their average weekly posting frequency for February 2024.

Note: Only include the dates from February 1 to February 28 in your analysis, which means you should count February as having exactly 4 weeks.

Return the result table ordered by user_id in ascending order.



1.
WITH rolled AS (
    SELECT
        *,
        COUNT(post_id) OVER(PARTITION BY user_id ORDER BY post_date ASC RANGE BETWEEN INTERVAL '6 days' PRECEDING AND CURRENT ROW) AS _7day_posts
    FROM Posts
    WHERE post_date BETWEEN '2024-2-1'::DATE AND '2024-2-28'::DATE
),
with_max_avg AS (
    SELECT
        *,
        MAX(_7day_posts) OVER(PARTITION BY user_id) AS max_7day_posts,
        ((COUNT(post_id) OVER(PARTITION BY user_id))::NUMERIC / 4) AS avg_weekly_posts
    FROM rolled
)
SELECT DISTINCT
    user_id,
    max_7day_posts,
    avg_weekly_posts
FROM with_max_avg
WHERE max_7day_posts >= (avg_weekly_posts * 2)
ORDER BY user_id ASC;