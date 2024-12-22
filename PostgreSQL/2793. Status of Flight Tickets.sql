--Table: Flights
--
--+-------------+------+
--| Column Name | Type |
--+-------------+------+
--| flight_id   | int  |
--| capacity    | int  |
--+-------------+------+
--flight_id column contains distinct values.
--Each row of this table contains flight id and capacity.
--Table: Passengers
--
--+--------------+----------+
--| Column Name  | Type     |
--+--------------+----------+
--| passenger_id | int      |
--| flight_id    | int      |
--| booking_time | datetime |
--+--------------+----------+
--passenger_id column contains distinct values.
--booking_time column contains distinct values.
--Each row of this table contains passenger id, booking time, and their flight id.
--Passengers book tickets for flights in advance. If a passenger books a ticket for a flight and there are still empty seats
--available on the flight, the passenger's ticket will be confirmed. However, the passenger will be on a waitlist if the flight is already at full capacity.
--
--Write a solution to determine the current status of flight tickets for each passenger.
--
--Return the result table ordered by passenger_id in ascending order.
--
--
--
--1.
WITH merged AS (
    SELECT
        main.passenger_id,
        main.booking_time,
        main.flight_id,
        sub.capacity
    FROM Passengers AS main

    LEFT JOIN Flights AS sub
        ON sub.flight_id = main.flight_id
),
with_window AS (
    SELECT
        *,
        COUNT(passenger_id) OVER(PARTITION BY flight_id ORDER BY booking_time ASC) AS cum_cnt
    FROM merged
)
SELECT
    passenger_id,
    (CASE WHEN capacity >= cum_cnt THEN 'Confirmed' ELSE 'Waitlist' END) AS Status
FROM with_window

ORDER BY passenger_id ASC;