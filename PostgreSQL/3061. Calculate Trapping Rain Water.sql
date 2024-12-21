--Table: Heights
--
--+-------------+------+
--| Column Name | Type |
--+-------------+------+
--| id          | int  |
--| height      | int  |
--+-------------+------+
--id is the primary key (column with unique values) for this table, and it is guaranteed to be in sequential order.
--Each row of this table contains an id and height.
--Write a solution to calculate the amount of rainwater can be trapped between the bars in the landscape, considering that each bar has a width of 1 unit.
--
--Return the result table in any order.
--
--
--1.
WITH with_cum AS (
    SELECT
        *,
        MAX(height) OVER(ORDER BY id ASC) AS left_cum,
        MAX(height) OVER(ORDER BY id DESC) AS right_cum
    FROM Heights
),
with_dif AS (
    SELECT
        *,
        GREATEST(LEAST(left_cum, right_cum) - height, 0) AS dif
    FROM with_cum
)
SELECT
    SUM(dif) AS total_trapped_water
FROM with_dif;