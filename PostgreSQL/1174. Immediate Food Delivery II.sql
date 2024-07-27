Table: Delivery

+-----------------------------+---------+
| Column Name                 | Type    |
+-----------------------------+---------+
| delivery_id                 | int     |
| customer_id                 | int     |
| order_date                  | date    |
| customer_pref_delivery_date | date    |
+-----------------------------+---------+
delivery_id is the column of unique values of this table.
The table holds information about food delivery to customers that make orders at some date and specify a preferred delivery date (on the same order date or after it).


--If the customer's preferred delivery date is the same as the order date, then the order is called immediate; otherwise, it is called scheduled.

The first order of a customer is the order with the earliest order date that the customer made. It is guaranteed that a customer has precisely one first order.

Write a solution to find the percentage of immediate orders in the first orders of all customers, rounded to 2 decimal places.


1.
WITH ranked AS
    (SELECT *, DENSE_RANK() OVER(PARTITION BY customer_id ORDER BY order_date ASC) AS our_rank
    FROM Delivery),
filtered AS
    (SELECT *, (CASE WHEN order_date = customer_pref_delivery_date THEN 1 ELSE 0 END) AS bool
    FROM ranked
    WHERE our_rank = 1)
SELECT ROUND(((SELECT SUM(bool) FROM filtered)::NUMERIC / (SELECT COUNT(bool) FROM filtered)::NUMERIC) * 100, 2) AS immediate_percentage;