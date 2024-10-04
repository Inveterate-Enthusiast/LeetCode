Table: Rides

+--------------+------+
| Column Name  | Type |
+--------------+------+
| ride_id      | int  |
| driver_id    | int  |
| passenger_id | int  |
+--------------+------+
ride_id is the column with unique values for this table.
Each row of this table contains the ID of the driver and the ID of the passenger that rode in ride_id.
Note that driver_id != passenger_id.


Write a solution to report the ID of each driver and the number of times they were a passenger.

Return the result table in any order.


1.
SELECT main.driver_id, COALESCE(COUNT(sub.ride_id), 0) AS cnt
FROM (SELECT DISTINCT driver_id FROM Rides) AS main
LEFT JOIN
Rides AS sub
ON main.driver_id = sub.passenger_id
GROUP BY main.driver_id;