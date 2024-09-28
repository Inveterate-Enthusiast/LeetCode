Table: Flights

+-------------------+------+
| Column Name       | Type |
+-------------------+------+
| departure_airport | int  |
| arrival_airport   | int  |
| flights_count     | int  |
+-------------------+------+
(departure_airport, arrival_airport) is the primary key column (combination of columns with unique values) for this table.
Each row of this table indicates that there were flights_count flights that departed from departure_airport and arrived at arrival_airport.


Write a solution to report the ID of the airport with the most traffic.
The airport with the most traffic is the airport that has the largest total number of flights that either departed
from or arrived at the airport. If there is more than one airport with the most traffic, report them all.

Return the result table in any order.


1.
WITH unioned AS
    (
    SELECT departure_airport AS airport_id, flights_count AS count
    FROM Flights

    UNION ALL

    SELECT arrival_airport AS airport_id, flights_count AS count
    FROM Flights
    ),
grouped AS
    (
    SELECT airport_id, SUM(count) AS count
    FROM unioned
    GROUP BY airport_id
    )
SELECT airport_id
FROM grouped
WHERE count = (SELECT MAX(count) FROM grouped);