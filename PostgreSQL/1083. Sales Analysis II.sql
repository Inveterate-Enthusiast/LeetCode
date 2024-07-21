Table: Product

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| product_id   | int     |
| product_name | varchar |
| unit_price   | int     |
+--------------+---------+
product_id is the primary key (column with unique values) of this table.
Each row of this table indicates the name and the price of each product.
Table: Sales

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| seller_id   | int     |
| product_id  | int     |
| buyer_id    | int     |
| sale_date   | date    |
| quantity    | int     |
| price       | int     |
+-------------+---------+
This table might have repeated rows.
product_id is a foreign key (reference column) to the Product table.
buyer_id is never NULL. 
sale_date is never NULL. 
Each row of this table contains some information about one sale.
 

Write a solution to report the buyers who have bought S8 but not iPhone. Note that S8 and iPhone are products presented in the Product table.

Return the result table in any order.

1.
WITH merged AS
(SELECT sal.buyer_id, pro.product_name FROM Sales AS sal LEFT JOIN Product AS pro ON sal.product_id = pro.product_id),
grouped AS
(SELECT buyer_id, ARRAY_AGG(DISTINCT product_name) AS our_set FROM merged GROUP BY buyer_id)
SELECT buyer_id FROM grouped WHERE 
('S8' = ANY(our_set)) AND 
('iPhone' <> ALL(our_set));

2.
WITH merged AS
(SELECT sal.buyer_id, pro.product_name FROM Sales AS sal LEFT JOIN Product AS pro ON sal.product_id = pro.product_id),
grouped AS
(SELECT buyer_id, ARRAY_AGG(DISTINCT product_name) AS our_set FROM merged GROUP BY buyer_id)
SELECT buyer_id FROM grouped WHERE 
'S8' IN (SELECT UNNEST(our_set)) AND
'iPhone' NOT IN (SELECT UNNEST(our_set));