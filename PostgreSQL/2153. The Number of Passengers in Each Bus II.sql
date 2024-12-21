--Table: Buses
--
--+--------------+------+
--| Column Name  | Type |
--+--------------+------+
--| bus_id       | int  |
--| arrival_time | int  |
--| capacity     | int  |
--+--------------+------+
--bus_id contains unique values.
--Each row of this table contains information about the arrival time of a bus at the LeetCode station and its capacity
--(the number of empty seats it has).
--No two buses will arrive at the same time and all bus capacities will be positive integers.
--
--
--Table: Passengers
--
--+--------------+------+
--| Column Name  | Type |
--+--------------+------+
--| passenger_id | int  |
--| arrival_time | int  |
--+--------------+------+
--passenger_id contains unique values.
--Each row of this table contains information about the arrival time of a passenger at the LeetCode station.
--
--
--Buses and passengers arrive at the LeetCode station. If a bus arrives at the station at a time tbus and a passenger
--arrived at a time tpassenger where tpassenger <= tbus and the passenger did not catch any bus, the passenger will use that bus.
--In addition, each bus has a capacity. If at the moment the bus arrives at the station there are more passengers waiting than its capacity capacity,
--only capacity passengers will use the bus.
--
--Write a solution to report the number of users that used each bus.
--
--Return the result table ordered by bus_id in ascending order.


--1.
WITH RECURSIVE with_prev_bus AS (
    SELECT
        *,
        COALESCE(LAG(arrival_time, 1) OVER(ORDER BY arrival_time ASC), 0) AS prev_time
    FROM Buses
),
with_count AS (
    SELECT
        bus.bus_id,
        bus.arrival_time,
        bus.capacity,
        COUNT(pas.passenger_id) AS pas_count,
        ROW_NUMBER() OVER(ORDER BY bus.arrival_time ASC) AS our_row
    FROM with_prev_bus AS bus

    LEFT JOIN Passengers AS pas
        ON pas.arrival_time <= bus.arrival_time
        AND pas.arrival_time > bus.prev_time

    GROUP BY bus.bus_id, bus.arrival_time, bus.capacity
),
main AS (
    SELECT
        our_row,
        bus_id,
        LEAST(capacity, pas_count) AS boarded,
        (pas_count - LEAST(capacity, pas_count)) AS rem
    FROM with_count

    WHERE our_row = 1

    UNION ALL

    SELECT
        sub.our_row,
        sub.bus_id,
        LEAST(sub.capacity, main.rem + sub.pas_count) AS boarded,
        ((sub.pas_count + main.rem) - LEAST(sub.capacity, main.rem + sub.pas_count)) AS rem
    FROM main

    INNER JOIN with_count AS sub
        ON sub.our_row = (main.our_row + 1)
)
SELECT
    bus_id,
    boarded AS passengers_cnt
FROM main

ORDER BY bus_id ASC;