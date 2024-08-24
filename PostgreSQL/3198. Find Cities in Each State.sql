Table: cities

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| state       | varchar |
| city        | varchar |
+-------------+---------+
(state, city) is the primary key (combination of columns with unique values) for this table.
Each row of this table contains the state name and the city name within that state.
Write a solution to find all the cities in each state and combine them into a single comma-separated string.

Return the result table ordered by state in ascending order.




1.
SELECT state, STRING_AGG(city, ', ' ORDER BY city ASC) AS cities
FROM cities
GROUP BY state
ORDER BY state ASC;