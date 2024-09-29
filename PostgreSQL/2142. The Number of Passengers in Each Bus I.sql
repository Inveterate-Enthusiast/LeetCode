Table: Buses

+--------------+------+
| Column Name  | Type |
+--------------+------+
| bus_id       | int  |
| arrival_time | int  |
+--------------+------+
bus_id is the column with unique values for this table.
Each row of this table contains information about the arrival time of a bus at the LeetCode station.
No two buses will arrive at the same time.


Table: Passengers

+--------------+------+
| Column Name  | Type |
+--------------+------+
| passenger_id | int  |
| arrival_time | int  |
+--------------+------+
passenger_id is the column with unique values for this table.
Each row of this table contains information about the arrival time of a passenger at the LeetCode station.


Buses and passengers arrive at the LeetCode station. If a bus arrives at the station at time tbus and a passenger arrived
at time tpassenger where tpassenger <= tbus and the passenger did not catch any bus, the passenger will use that bus.

Write a solution to report the number of users that used each bus.

Return the result table ordered by bus_id in ascending order.


1.
WITH crossed AS
    (
    SELECT main.bus_id, main.arrival_time AS bus_time,
    sub.passenger_id, sub.arrival_time AS pas_time,
    (sub.arrival_time <= main.arrival_time) AS less
    FROM Buses AS main
    CROSS JOIN
    Passengers AS sub
    ),
ranked AS
    (
    SELECT *, DENSE_RANK() OVER(PARTITION BY passenger_id ORDER BY bus_time ASC) AS our_rank
    FROM crossed
    WHERE less = TRUE
    )
SELECT main.bus_id, COALESCE(sub.passengers_cnt, 0) AS passengers_cnt
FROM Buses AS main
LEFT JOIN
(
    SELECT bus_id, COUNT(passenger_id) AS passengers_cnt
    FROM ranked
    WHERE our_rank = 1
    GROUP BY bus_id
) AS sub
ON main.bus_id = sub.bus_id
ORDER BY bus_id ASC;