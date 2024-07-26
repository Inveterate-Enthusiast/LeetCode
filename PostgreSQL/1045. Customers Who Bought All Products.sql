Table: Customer

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| customer_id | int     |
| product_key | int     |
+-------------+---------+
This table may contain duplicates rows.
customer_id is not NULL.
product_key is a foreign key (reference column) to Product table.


Table: Product

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_key | int     |
+-------------+---------+
product_key is the primary key (column with unique values) for this table.


Write a solution to report the customer ids from the Customer table that bought all the products in the Product table.

Return the result table in any order.

1.
WITH grouped AS
    (SELECT customer_id, ARRAY_AGG(DISTINCT product_key) AS our_array
    FROM Customer
    GROUP BY customer_id)
SELECT customer_id
FROM grouped
WHERE our_array @> ARRAY(SELECT DISTINCT product_key FROM Product);

2.
SELECT customer_id
FROM Customer
GROUP BY customer_id
HAVING ARRAY_AGG(DISTINCT product_key) @> ARRAY(SELECT DISTINCT product_key FROM Product);