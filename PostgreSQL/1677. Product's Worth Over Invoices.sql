Table: Product

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| name        | varchar |
+-------------+---------+
product_id is the column with unique values for this table.
This table contains the ID and the name of the product. The name consists of only lowercase English letters. No two products have the same name.
 

Table: Invoice

+-------------+------+
| Column Name | Type |
+-------------+------+
| invoice_id  | int  |
| product_id  | int  |
| rest        | int  |
| paid        | int  |
| canceled    | int  |
| refunded    | int  |
+-------------+------+
invoice_id is the column with unique values for this table and the id of this invoice.
product_id is the id of the product for this invoice.
rest is the amount left to pay for this invoice.
paid is the amount paid for this invoice.
canceled is the amount canceled for this invoice.
refunded is the amount refunded for this invoice.
 

Write a solution that will, for all products, return each product name with the total amount due, paid, canceled, and refunded across all invoices.

Return the result table ordered by product_name.



1.
WITH grouped AS
	(SELECT product_id, SUM(rest) AS rest, SUM(paid) AS paid, SUM(canceled) AS canceled, SUM(refunded) AS refunded
	FROM Invoice
	GROUP BY product_id)
SELECT sub.name, 
COALESCE(main.rest, 0) AS rest, 
COALESCE(main.paid, 0) AS paid, 
COALESCE(main.canceled, 0) AS canceled, 
COALESCE(main.refunded, 0) AS refunded
FROM grouped AS main
RIGHT JOIN 
Product AS sub
ON main.product_id = sub.product_id
ORDER BY sub.name ASC;


2.
SELECT name,
COALESCE(SUM(rest), 0) AS rest, 
COALESCE(SUM(paid), 0) AS paid, 
COALESCE(SUM(canceled), 0) AS canceled, 
COALESCE(SUM(refunded), 0) AS refunded
FROM
Invoice AS main
RIGHT JOIN
Product AS sub
ON main.product_id = sub.product_id
GROUP BY name
ORDER BY name ASC;

