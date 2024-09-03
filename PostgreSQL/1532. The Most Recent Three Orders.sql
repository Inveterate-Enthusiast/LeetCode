Table: Customers

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| customer_id   | int     |
| name          | varchar |
+---------------+---------+
customer_id is the column with unique values for this table.
This table contains information about customers.


Table: Orders

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| order_id      | int     |
| order_date    | date    |
| customer_id   | int     |
| cost          | int     |
+---------------+---------+
order_id is the column with unique values for this table.
This table contains information about the orders made by customer_id.
Each customer has one order per day.


Write a solution to find the most recent three orders of each user. If a user ordered less than three orders, return all of their orders.

Return the result table ordered by customer_name in ascending order and in case of a tie by the customer_id in ascending order.
If there is still a tie, order them by order_date in descending order.



1.
WITH ranked AS
    (
    SELECT *, DENSE_RANK() OVER(PARTITION BY customer_id ORDER BY order_date DESC) AS our_rank
    FROM Orders
    )
SELECT sub.name AS customer_name, main.customer_id, main.order_id, main.order_date
FROM ranked AS main
LEFT JOIN
Customers AS sub
ON main.customer_id = sub.customer_id
WHERE main.our_rank <= 3
ORDER BY customer_name ASC, main.customer_id ASC, main.order_date DESC;