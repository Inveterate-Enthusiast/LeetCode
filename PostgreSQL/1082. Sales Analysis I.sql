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
This table can have repeated rows.
product_id is a foreign key (reference column) to the Product table.
Each row of this table contains some information about one sale.
 

Write a solution that reports the best seller by total sales price, If there is a tie, report them all.

Return the result table in any order.


1.
WITH grouped AS
(SELECT seller_id, SUM(price) AS sum_of_sells FROM Sales GROUP BY seller_id)
SELECT seller_id FROM grouped WHERE sum_of_sells = (SELECT MAX(sum_of_sells) FROM grouped);