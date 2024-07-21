Table: Warehouse

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| name         | varchar |
| product_id   | int     |
| units        | int     |
+--------------+---------+
(name, product_id) is the primary key (combination of columns with unique values) for this table.
Each row of this table contains the information of the products in each warehouse.
 

Table: Products

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| product_name  | varchar |
| Width         | int     |
| Length        | int     |
| Height        | int     |
+---------------+---------+
product_id is the primary key (column with unique values) for this table.
Each row of this table contains information about the product dimensions (Width, Lenght, and Height) in feets of each product.
 

Write a solution to report the number of cubic feet of volume the inventory occupies in each warehouse.

Return the result table in any order.



1.
SELECT main.name AS warehouse_name,
SUM(sub.Width * sub.Length * sub.Height * main.units) AS volume
FROM Warehouse AS main
INNER JOIN
Products AS sub
ON main.product_id = sub.product_id
GROUP BY main.name;