Table: Customers

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| customer_id   | int     |
| name          | varchar |
+---------------+---------+
customer_id is the column with unique values for this table.
This table contains information about the customers.


Table: Orders

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| order_id      | int     |
| order_date    | date    |
| customer_id   | int     |
| product_id    | int     |
+---------------+---------+
order_id is the column with unique values for this table.
This table contains information about the orders made by customer_id.
No customer will order the same product more than once in a single day.


Table: Products

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| product_name  | varchar |
| price         | int     |
+---------------+---------+
product_id is the column with unique values for this table.
This table contains information about the products.


Write a solution to find the most frequently ordered product(s) for each customer.

The result table should have the product_id and product_name for each customer_id who ordered at least one order.

Return the result table in any order.



1.
WITH ranked AS
    (
    SELECT customer_id, product_id, RANK() OVER(PARTITION BY customer_id ORDER BY our_count DESC) AS our_rank
    FROM (
        SELECT customer_id, product_id, COUNT(*) AS our_count
        FROM Orders
        GROUP BY customer_id, product_id
        )
    )
SELECT main.customer_id, main.product_id, sub.product_name
FROM ranked AS main
LEFT JOIN
Products AS sub
ON main.product_id = sub.product_id
WHERE main.our_rank = 1;