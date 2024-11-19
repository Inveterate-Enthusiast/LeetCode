Table: UserActivity

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| username      | varchar |
| activity      | varchar |
| startDate     | Date    |
| endDate       | Date    |
+---------------+---------+
This table may contain duplicates rows.
This table contains information about the activity performed by each user in a period of time.
A person with username performed an activity from startDate to endDate.


Write a solution to show the second most recent activity of each user.

If the user only has one activity, return that one. A user cannot perform more than one activity at the same time.

Return the result table in any order.




1.
WITH ranked AS (
    SELECT
        *,
        DENSE_RANK() OVER(PARTITION BY username ORDER BY endDate DESC) AS our_rank,
        COUNT(endDate) OVER(PARTITION BY username) AS our_count
    FROM UserActivity
)
SELECT
    username,
    activity,
    startDate,
    endDate
FROM ranked
WHERE ((our_count > 1) AND (our_rank = 2))
OR ((our_count = 1) AND (our_rank = 1));