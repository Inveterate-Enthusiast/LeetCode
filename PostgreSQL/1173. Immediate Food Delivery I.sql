Table: Delivery

+-----------------------------+---------+
| Column Name                 | Type    |
+-----------------------------+---------+
| delivery_id                 | int     |
| customer_id                 | int     |
| order_date                  | date    |
| customer_pref_delivery_date | date    |
+-----------------------------+---------+
delivery_id is the primary key (column with unique values) of this table.
The table holds information about food delivery to customers that make orders at some date and specify a preferred delivery date (on the same order date or after it).
 

--If the customer's preferred delivery date is the same as the order date, then the order is called immediate; otherwise, it is called scheduled.

Write a solution to find the percentage of immediate orders in the table, rounded to 2 decimal places.


1.
WITH immediate_count AS
(SELECT COUNT(DISTINCT delivery_id) AS count FROM Delivery WHERE order_date = customer_pref_delivery_date),
all_count AS
(SELECT COUNT(DISTINCT delivery_id) AS count FROM Delivery)
SELECT COALESCE(ROUND(((SELECT count FROM immediate_count)::NUMERIC / (SELECT count FROM all_count)::NUMERIC)*100, 2), 0) AS immediate_percentage;