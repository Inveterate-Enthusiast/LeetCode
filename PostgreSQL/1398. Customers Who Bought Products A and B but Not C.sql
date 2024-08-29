Table: Customers

+---------------------+---------+
| Column Name         | Type    |
+---------------------+---------+
| customer_id         | int     |
| customer_name       | varchar |
+---------------------+---------+
customer_id is the column with unique values for this table.
customer_name is the name of the customer.


Table: Orders

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| order_id      | int     |
| customer_id   | int     |
| product_name  | varchar |
+---------------+---------+
order_id is the column with unique values for this table.
customer_id is the id of the customer who bought the product "product_name".


Write a solution to report the customer_id and customer_name of customers who bought products "A", "B"
but did not buy the product "C" since we want to recommend them to purchase this product.

Return the result table ordered by customer_id.



1.
WITH grouped AS
    (SELECT customer_id
    FROM Orders
    GROUP BY customer_id
    HAVING (NOT ARRAY_AGG(DISTINCT product_name)::TEXT[] @> ARRAY['C'])
    AND (ARRAY_AGG(DISTINCT product_name)::TEXT[] @> ARRAY['A', 'B']))
SELECT main.customer_id, sub.customer_name
FROM grouped AS main
LEFT JOIN
Customers AS sub
ON main.customer_id = sub.customer_id
ORDER BY main.customer_id ASC;