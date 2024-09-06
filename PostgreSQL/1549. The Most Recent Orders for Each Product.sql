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
There will be no product ordered by the same user more than once in one day.


Table: Products

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| product_name  | varchar |
| price         | int     |
+---------------+---------+
product_id is the column with unique values for this table.
This table contains information about the Products.


Write a solution to find the most recent order(s) of each product.

Return the result table ordered by product_name in ascending order and in case of a tie by the product_id in ascending order.
If there still a tie, order them by order_id in ascending order.


1.
WITH ranked AS
    (SELECT *, RANK() OVER(PARTITION BY product_id ORDER BY order_date DESC) AS our_rank
    FROM Orders)
SELECT sub.product_name, main.product_id, main.order_id, main.order_date
FROM (SELECT * FROM ranked WHERE our_rank = 1) AS main
LEFT JOIN
Products AS sub
ON main.product_id = sub.product_id
ORDER BY product_name ASC, product_id ASC, order_id ASC;