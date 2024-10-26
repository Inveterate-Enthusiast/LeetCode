Table: Calls

+--------------+----------+
| Column Name  | Type     |
+--------------+----------+
| caller_id    | int      |
| recipient_id | int      |
| call_time    | datetime |
| city         | varchar  |
+--------------+----------+
(caller_id, recipient_id, call_time) is the primary key (combination of columns with unique values) for this table.
Each row contains caller id, recipient id, call time, and city.
Write a solution to find the peak calling hour for each city.
If multiple hours have the same number of calls, all of those hours will be recognized as peak hours for that specific city.

Return the result table ordered by peak calling hour and city in descending order.




1.
WITH grouped AS (
    SELECT
        city,
        EXTRACT(HOUR FROM call_time) AS peak_calling_hour,
        COUNT(caller_id) AS number_of_calls
    FROM Calls
    GROUP BY 1, 2
),
ranked AS (
    SELECT
        *,
        RANK() OVER(PARTITION BY city ORDER BY number_of_calls DESC) AS rank
    FROM grouped
)
SELECT
    city,
    peak_calling_hour,
    number_of_calls
FROM ranked
WHERE rank = 1
ORDER BY peak_calling_hour DESC, city DESC;