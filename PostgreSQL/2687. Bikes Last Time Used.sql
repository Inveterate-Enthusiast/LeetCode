Table: Bikes

+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| ride_id     | int      |
| bike_number | int      |
| start_time  | datetime |
| end_time    | datetime |
+-------------+----------+
ride_id column contains unique values.
Each row contains a ride information that includes ride_id, bike number, start and end time of the ride.
Write a solution to find the last time when each bike was used.

Return the result table ordered by the bikes that were most recently used.


1.
SELECT bike_number, MAX(end_time) AS end_time
FROM Bikes
GROUP BY bike_number
ORDER BY end_time DESC;