Table: Products

+------------------+---------+
| Column Name      | Type    |
+------------------+---------+
| product_id       | int     |
| product_name     | varchar |
| product_category | varchar |
+------------------+---------+
product_id is the primary key (column with unique values) for this table.
--This table contains data about the company's products.
 

Table: Orders

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| order_date    | date    |
| unit          | int     |
+---------------+---------+
This table may have duplicate rows.
product_id is a foreign key (reference column) to the Products table.
unit is the number of products ordered in order_date.


1.
WITH grouped AS
	(SELECT product_id, SUM(unit) AS unit FROM Orders WHERE TO_CHAR(order_date, 'YYYY-MM') = '2020-02' GROUP BY product_id)
SELECT sub.product_name, main.unit FROM grouped AS main LEFT JOIN Products AS sub ON main.product_id = sub.product_id WHERE main.unit >= 100;
