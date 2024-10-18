Table: Flights

+-------------+------+
| Column Name | Type |
+-------------+------+
| flight_id   | int  |
| capacity    | int  |
+-------------+------+
flight_id is the column with unique values for this table.
Each row of this table contains flight id and its capacity.
Table: Passengers

+--------------+------+
| Column Name  | Type |
+--------------+------+
| passenger_id | int  |
| flight_id    | int  |
+--------------+------+
passenger_id is the column with unique values for this table.
Each row of this table contains passenger id and flight id.
Passengers book tickets for flights in advance. If a passenger books a ticket for a flight and there
are still empty seats available on the flight, the passenger ticket will be confirmed.
However, the passenger will be on a waitlist if the flight is already at full capacity.

Write a solution to report the number of passengers who successfully booked a flight (got a seat)
and the number of passengers who are on the waitlist for each flight.

Return the result table ordered by flight_id in ascending order.



1.
WITH with_bools AS (
    SELECT
        main.passenger_id,
        main.flight_id,
        (COALESCE(sub.capacity, 0) >= DENSE_RANK() OVER(PARTITION BY main.flight_id ORDER BY main.passenger_id ASC)) AS bool
    FROM Passengers AS main

    LEFT JOIN Flights AS sub
    ON sub.flight_id = main.flight_id
),
grouped AS (
    SELECT
        flight_id,
        SUM(CASE WHEN bool = TRUE THEN 1 ELSE 0 END) AS booked_cnt,
        SUM(CASE WHEN bool = FALSE THEN 1 ELSE 0 END) AS waitlist_cnt
    FROM with_bools
    GROUP BY flight_id
)
SELECT
    main.flight_id,
    COALESCE(sub.booked_cnt, 0) AS booked_cnt,
    COALESCE(sub.waitlist_cnt, 0) AS waitlist_cnt
FROM Flights AS main

LEFT JOIN grouped AS sub
ON sub.flight_id = main.flight_id

ORDER BY main.flight_id ASC;