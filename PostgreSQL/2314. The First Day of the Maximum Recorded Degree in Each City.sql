Table: Weather

+-------------+------+
| Column Name | Type |
+-------------+------+
| city_id     | int  |
| day         | date |
| degree      | int  |
+-------------+------+
(city_id, day) is the primary key (combination of columns with unique values) for this table.
Each row in this table contains the degree of the weather of a city on a certain day.
All the degrees are recorded in the year 2022.


Write a solution to report the day that has the maximum recorded degree in each city.
If the maximum degree was recorded for the same city multiple times, return the earliest day among them.

Return the result table ordered by city_id in ascending order.


1.
WITH ranked AS (
    SELECT
        *,
        RANK() OVER(PARTITION BY city_id ORDER BY degree DESC, day ASC) AS our_rank
        FROM Weather
)
SELECT
    city_id,
    day,
    degree
FROM ranked
WHERE our_rank = 1
ORDER BY city_id ASC;