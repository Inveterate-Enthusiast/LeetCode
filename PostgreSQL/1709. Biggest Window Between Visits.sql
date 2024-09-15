Table: UserVisits

+-------------+------+
| Column Name | Type |
+-------------+------+
| user_id     | int  |
| visit_date  | date |
+-------------+------+
This table does not have a primary key, it might contain duplicate rows.
This table contains logs of the dates that users visited a certain retailer.


Assume today's date is '2021-1-1'.

Write a solution that will, for each user_id, find out the largest window of days between
each visit and the one right after it (or today if you are considering the last visit).

Return the result table ordered by user_id.


1.
WITH added AS
    (
    SELECT *
    FROM UserVisits

    UNION ALL

    SELECT DISTINCT(user_id), '2021-1-1'::DATE AS visit_date
    FROM UserVisits
    ),
calculated AS
    (
    SELECT *,
    ((EXTRACT(EPOCH FROM (visit_date::TIMESTAMP - LAG(visit_date::TIMESTAMP, 1) OVER (PARTITION BY user_id ORDER BY visit_date ASC))))::NUMERIC / (60 * 60 * 24)::NUMERIC)::INT AS diff
    FROM added
    )
SELECT user_id, MAX(diff) AS biggest_window
FROM calculated
GROUP BY user_id
ORDER BY user_id ASC;