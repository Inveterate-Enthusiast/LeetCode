Table: OrdersDetails

+-------------+------+
| Column Name | Type |
+-------------+------+
| order_id    | int  |
| product_id  | int  |
| quantity    | int  |
+-------------+------+
(order_id, product_id) is the primary key (combination of columns with unique values) for this table.
A single order is represented as multiple rows, one row for each product in the order.
Each row of this table contains the quantity ordered of the product product_id in the order order_id.


You are running an e-commerce site that is looking for imbalanced orders. An imbalanced order is one whose maximum
quantity is strictly greater than the average quantity of every order (including itself).

The average quantity of an order is calculated as (total quantity of all products in the order) /
(number of different products in the order). The maximum quantity of an order is the highest quantity of any single product in the order.

Write a solution to find the order_id of all imbalanced orders.

Return the result table in any order.


1.
WITH ranked AS
    (
    SELECT *,
    DENSE_RANK() OVER(PARTITION BY order_id ORDER BY quantity DESC) AS our_rank,
    AVG(quantity) OVER(PARTITION BY order_id) AS avg
    FROM OrdersDetails
    )
SELECT order_id
FROM ranked
WHERE our_rank = 1 AND quantity > (SELECT MAX(avg) FROM ranked);