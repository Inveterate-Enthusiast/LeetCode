Table: Delivery

+-----------------------------+---------+
| Column Name                 | Type    |
+-----------------------------+---------+
| delivery_id                 | int     |
| customer_id                 | int     |
| order_date                  | date    |
| customer_pref_delivery_date | date    |
+-----------------------------+---------+
delivery_id is the column with unique values of this table.
Each row contains information about food delivery to a customer that makes an
order at some date and specifies a preferred delivery date (on the order date or after it).
--If the customer's preferred delivery date is the same as the order date, then the order is called immediate, otherwise, it is scheduled.

Write a solution to find the percentage of immediate orders on each unique order_date, rounded to 2 decimal places.

Return the result table ordered by order_date in ascending order.


1.
WITH bool AS (
    SELECT
        *,
        (CASE WHEN order_date = customer_pref_delivery_date THEN 1 ELSE 0 END) AS bool
    FROM Delivery
)
SELECT
    order_date,
    ROUND((SUM(bool)::NUMERIC / COUNT(delivery_id)::NUMERIC) * 100, 2) AS immediate_percentage
FROM bool
GROUP BY order_date
ORDER BY order_date ASC;