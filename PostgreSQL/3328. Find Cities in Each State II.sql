Table: cities

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| state       | varchar |
| city        | varchar |
+-------------+---------+
(state, city) is the combination of columns with unique values for this table.
Each row of this table contains the state name and the city name within that state.
Write a solution to find all the cities in each state and analyze them based on the following requirements:

Combine all cities into a comma-separated string for each state.
Only include states that have at least 3 cities.
Only include states where at least one city starts with the same letter as the state name.
Return the result table ordered by the count of matching-letter cities in descending order and then by state name in ascending order.



1.
WITH sub AS (
    SELECT
        *,
        COUNT(cities) OVER(PARTITION BY state) AS cities_count,
        (CASE WHEN LEFT(city, 1) = LEFT(state, 1) THEN 1 ELSE 0 END) AS matching_letter_count
    FROM cities
)
SELECT
    state,
    STRING_AGG(city, ', ' ORDER BY city ASC) AS cities,
    SUM(matching_letter_count) AS matching_letter_count
FROM sub
WHERE cities_count >= 3
GROUP BY state
HAVING SUM(matching_letter_count) > 0
ORDER BY matching_letter_count DESC, state ASC;