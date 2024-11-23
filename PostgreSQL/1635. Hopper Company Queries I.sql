Table: Drivers

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| driver_id   | int     |
| join_date   | date    |
+-------------+---------+
driver_id is the primary key (column with unique values) for this table.
--Each row of this table contains the driver's ID and the date they joined the Hopper company.


Table: Rides

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| ride_id      | int     |
| user_id      | int     |
| requested_at | date    |
+--------------+---------+
ride_id is the primary key (column with unique values) for this table.
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
ride_id is the primary key (column with unique values) for this table.
Each row of this table contains some information about an accepted ride.
It is guaranteed that each accepted ride exists in the Rides table.


Write a solution to report the following statistics for each month of 2020:

The number of drivers currently with the Hopper company by the end of the month (active_drivers).
The number of accepted rides in that month (accepted_rides).
--Return the result table ordered by month in ascending order, where month is the month's number (January is 1, February is 2, etc.).





1.
WITH months AS (
    SELECT GENERATE_SERIES(1,12,1) AS month
),
drivers AS (
    SELECT
        main.month,
        (
            CASE
                WHEN main.month = 1 THEN COUNT(DISTINCT sub_1.driver_id)
                ELSE 0
            END
        )
        +
        COUNT(DISTINCT sub.driver_id)
        AS our_count
    FROM months AS main

    LEFT JOIN Drivers AS sub
        ON EXTRACT(MONTH FROM sub.join_date) = main.month
        AND EXTRACT(YEAR FROM sub.join_date) = 2020

    LEFT JOIN Drivers AS sub_1
        ON EXTRACT(YEAR FROM sub_1.join_date) < 2020

    GROUP BY main.month
),
grouped_drivers AS (
    SELECT
        *,
        SUM(our_count) OVER(ORDER BY month ASC) AS active_drivers
    FROM drivers
),
grouped_rides AS (
    SELECT
        EXTRACT(MONTH FROM requested_at) AS month,
        COUNT(DISTINCT main.ride_id) AS accepted_rides
    FROM Rides AS main

    INNER JOIN AcceptedRides AS sub
        ON sub.ride_id = main.ride_id

    WHERE EXTRACT(YEAR FROM main.requested_at) = 2020

    GROUP BY EXTRACT(MONTH FROM requested_at)
)
SELECT
    main.month,
    main.active_drivers,
    COALESCE(sub.accepted_rides, 0) AS accepted_rides
FROM grouped_drivers AS main

LEFT JOIN grouped_rides AS sub
    ON sub.month = main.month

ORDER BY main.month ASC;