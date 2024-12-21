--Table: HallEvents
--
--+-------------+------+
--| Column Name | Type |
--+-------------+------+
--| hall_id     | int  |
--| start_day   | date |
--| end_day     | date |
--+-------------+------+
--This table may contain duplicates rows.
--Each row of this table indicates the start day and end day of an event and the hall in which the event is held.
--
--
--Write a solution to merge all the overlapping events that are held in the same hall. Two events overlap if they have at least one day in common.
--
--Return the result table in any order.
--
--
--1.
WITH with_prev AS (
    SELECT
        *,
        LAG(end_day, 1) OVER(PARTITION BY hall_id ORDER BY start_day ASC, end_day ASC) AS end_prev
    FROM HallEvents
),
with_cum AS (
    SELECT
        *,
        MAX(end_prev) OVER(PARTITION BY hall_id ORDER BY start_day ASC, end_day ASC) AS end_prev_cum
    FROM with_prev
),
with_bool AS (
    SELECT
        *,
        (
            CASE
                WHEN start_day > end_prev_cum THEN 1
                ELSE 0
            END
        ) AS our_bool
    FROM with_cum
),
with_groups AS (
    SELECT
        *,
        SUM(our_bool) OVER(PARTITION BY hall_id ORDER BY start_day ASC, end_day ASC) AS our_group
    FROM with_bool
)
SELECT
    hall_id,
    MIN(start_day) AS start_day,
    MAX(end_day) AS end_day
FROM with_groups
GROUP BY hall_id, our_group;