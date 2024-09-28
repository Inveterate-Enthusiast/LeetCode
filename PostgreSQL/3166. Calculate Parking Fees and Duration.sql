Table: ParkingTransactions

+--------------+-----------+
| Column Name  | Type      |
+--------------+-----------+
| lot_id       | int       |
| car_id       | int       |
| entry_time   | datetime  |
| exit_time    | datetime  |
| fee_paid     | decimal   |
+--------------+-----------+
(lot_id, car_id, entry_time) is the primary key (combination of columns with unique values) for this table.
Each row of this table contains the ID of the parking lot, the ID of the car, the entry and exit times, and the fee paid for the parking duration.
Write a solution to find the total parking fee paid by each car across all parking lots,
and the average hourly fee (rounded to 2 decimal places) paid by each car. Also, find the parking lot where each car spent the most total time.

Return the result table ordered by car_id in ascending order.

Note: Test cases are generated in such a way that an individual car cannot be in multiple parking lots at the same time.


1.
WITH grouped AS
    (
    SELECT car_id, lot_id, SUM(exit_time - entry_time) AS time_lot
    FROM ParkingTransactions
    GROUP BY car_id, lot_id
    ),
ranked AS
    (
    SELECT *, DENSE_RANK() OVER(PARTITION BY car_id ORDER BY time_lot DESC) AS our_rank
    FROM grouped
    ),
common AS
    (
    SELECT car_id,
    SUM(fee_paid) AS total_fee_paid,
    ROUND((SUM(fee_paid)::NUMERIC / SUM(EXTRACT(EPOCH FROM (exit_time - entry_time)) / (60*60))::NUMERIC), 2) AS avg_hourly_fee
    FROM ParkingTransactions
    GROUP BY car_id
    )
SELECT main.car_id, main.total_fee_paid, main.avg_hourly_fee, sub.lot_id AS most_time_lot
FROM common AS main
LEFT JOIN
(SELECT car_id, lot_id FROM ranked WHERE our_rank = 1) AS sub
ON main.car_id = sub.car_id
ORDER BY main.car_id ASC;