Table: Drivers

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| driver_id   | int     |
| join_date   | date    |
+-------------+---------+
driver_id is the column with unique values for this table.
--Each row of this table contains the driver's ID and the date they joined the Hopper company.


Table: Rides

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| ride_id      | int     |
| user_id      | int     |
| requested_at | date    |
+--------------+---------+
ride_id is the column with unique values for this table.
--Each row of this table contains the ID of a ride, the user's ID that requested it, and the day they requested it.
There may be some ride requests in this table that were not accepted.


Table: AcceptedRides

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| ride_id       | int     |
| driver_id     | int     |
| ride_distance | int     |
| ride_duration | int     |
+---------------+---------+
ride_id is the column with unique values for this table.
Each row of this table contains some information about an accepted ride.
It is guaranteed that each accepted ride exists in the Rides table.


Write a solution to compute the average_ride_distance and average_ride_duration of every 3-month window starting from January - March 2020 to October - December 2020. Round average_ride_distance and average_ride_duration to the nearest two decimal places.

The average_ride_distance is calculated by summing up the total ride_distance values from the three months and dividing it by 3. The average_ride_duration is calculated in a similar way.

--Return the result table ordered by month in ascending order, where month is the starting month's number (January is 1, February is 2, etc.).




1.
WITH months AS (
    SELECT GENERATE_SERIES(1, 12, 1) AS month
),
merged AS (
    SELECT
        main.month,
        SUM(COALESCE(sub.ride_distance, 0)) AS distance_sum,
        SUM(COALESCE(sub.ride_duration, 0)) AS duration_sum
    FROM months AS main

    LEFT JOIN (
        SELECT
            main.requested_at,
            sub.ride_distance,
            sub.ride_duration
        FROM Rides AS main

        INNER JOIN AcceptedRides AS sub
            ON sub.ride_id = main.ride_id
    ) AS sub
        ON EXTRACT(MONTH FROM sub.requested_at) = main.month
        AND EXTRACT(YEAR FROM sub.requested_at) = 2020

    GROUP BY main.month
),
our_window AS (
    SELECT
        month,
        ROUND(AVG(distance_sum) OVER(ORDER BY month ASC ROWS BETWEEN CURRENT ROW AND 2 FOLLOWING), 2) AS average_ride_distance,
        ROUND(AVG(duration_sum) OVER(ORDER BY month ASC ROWS BETWEEN CURRENT ROW AND 2 FOLLOWING), 2) AS average_ride_duration
    FROM merged
)
SELECT
    *
FROM window
WHERE month <= 10
ORDER BY month ASC;