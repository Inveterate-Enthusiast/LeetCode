--Table: Wineries
--
--+-------------+----------+
--| Column Name | Type     |
--+-------------+----------+
--| id          | int      |
--| country     | varchar  |
--| points      | int      |
--| winery      | varchar  |
--+-------------+----------+
--id is column of unique values for this table.
--This table contains id, country, points, and winery.
--Write a solution to find the top three wineries in each country based on their total points.
--If multiple wineries have the same total points, order them by winery name in ascending order.
--If there's no second winery, output 'No second winery,' and if there's no third winery, output 'No third winery.'
--
--Return the result table ordered by country in ascending order.
--
--
--
--1.
WITH grouped AS (
    SELECT
        winery,
        country,
        SUM(points) AS points,
        DENSE_RANK() OVER(PARTITION BY country ORDER BY SUM(points) DESC, winery ASC) AS our_rank
    FROM Wineries
    GROUP BY winery, country
)
SELECT
    country,
    COALESCE(
        MAX(
            CASE
                WHEN our_rank = 1 THEN CONCAT(winery, ' (', points, ')')
            END
        ),
        'No top winery'
    ) AS top_winery,
    COALESCE(
        MAX(
            CASE
                WHEN our_rank = 2 THEN CONCAT(winery, ' (', points, ')')
            END
        ),
        'No second winery'
    ) AS second_winery,
    COALESCE(
        MAX(
            CASE
                WHEN our_rank = 3 THEN CONCAT(winery, ' (', points, ')')
            END
        ),
        'No third winery'
    ) AS third_winery
FROM grouped

WHERE our_rank <= 3
GROUP BY country
ORDER BY country ASC;