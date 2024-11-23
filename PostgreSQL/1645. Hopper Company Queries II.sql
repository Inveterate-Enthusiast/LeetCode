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


Write a solution to report the percentage of working drivers (working_percentage) for each month of 2020 where:


Note that if the number of available drivers during a month is zero, we consider the working_percentage to be 0.

--Return the result table ordered by month in ascending order, where month is the month's number (January is 1, February is 2, etc.). Round working_percentage to the nearest 2 decimal places.




1.
WITH months AS (
    SELECT GENERATE_SERIES(1, 12, 1) AS month
),
drivers_grouped AS (
    SELECT
        main.month,
        (
        CASE
            WHEN month = 1 THEN COUNT(DISTINCT sub_1.driver_id)
            ELSE 0
        END
        ) + COUNT(DISTINCT sub.driver_id) AS our_count
    FROM months AS main

    LEFT JOIN Drivers AS sub
        ON EXTRACT(MONTH FROM sub.join_date) = main.month
        AND EXTRACT(YEAR FROM sub.join_date) = 2020

    LEFT JOIN Drivers AS sub_1
        ON EXTRACT(YEAR FROM sub_1.join_date) < 2020

    GROUP BY main.month
),
drivers_available AS (
    SELECT
        *,
        SUM(our_count) OVER(ORDER BY month ASC) AS available
    FROM drivers_grouped
),
drivers_accepted AS (
    SELECT
        main.month,
        COUNT(DISTINCT AcRides.driver_id) AS accepted
    FROM months AS main

    INNER JOIN Rides
        ON EXTRACT(MONTH FROM Rides.requested_at) = main.month
        AND EXTRACT(YEAR FROM Rides.requested_at) = 2020

    INNER JOIN AcceptedRides AS AcRides
        ON AcRides.ride_id = Rides.ride_id

    GROUP BY main.month
)
SELECT
    main.month,
    ROUND(
        (
        CASE
            WHEN NOT COALESCE(main.available, 0) = 0 THEN (COALESCE(sub.accepted, 0) / COALESCE(main.available, 0) * 100)
            ELSE 0
        END
        ),
        2
    ) AS working_percentage
FROM drivers_available AS main

LEFT JOIN drivers_accepted AS sub
    ON sub.month = main.month

ORDER BY main.month ASC;