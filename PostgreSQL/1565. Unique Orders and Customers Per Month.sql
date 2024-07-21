Table: Orders

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| order_id      | int     |
| order_date    | date    |
| customer_id   | int     |
| invoice       | int     |
+---------------+---------+
order_id is the column with unique values for this table.
This table contains information about the orders made by customer_id.
 

Write a solution to find the number of unique orders and the number of unique customers with invoices > $20 for each different month.

Return the result table sorted in any order.



1.
WITH cte AS
	(SELECT *, TO_CHAR(order_date, 'YYYY-MM') AS month
	FROM Orders)
SELECT month,
COUNT(DISTINCT order_id) AS order_count,
COUNT(DISTINCT customer_id) AS customer_count
FROM cte
WHERE invoice > 20
GROUP BY
month;