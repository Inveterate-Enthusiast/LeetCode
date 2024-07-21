Table: Customer

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| customer_id   | int     |
| customer_name | varchar |
+---------------+---------+
customer_id is the column with unique values for this table.
Each row of this table contains the information of each customer in the WebStore.
 

Table: Orders

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| order_id      | int     |
| sale_date     | date    |
| order_cost    | int     |
| customer_id   | int     |
| seller_id     | int     |
+---------------+---------+
order_id is the column with unique values for this table.
Each row of this table contains all orders made in the webstore.
sale_date is the date when the transaction was made between the customer (customer_id) and the seller (seller_id).
 

Table: Seller

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| seller_id     | int     |
| seller_name   | varchar |
+---------------+---------+
seller_id is the column with unique values for this table.
Each row of this table contains the information of each seller.
 

Write a solution to report the names of all sellers who did not make any sales in 2020.

Return the result table ordered by seller_name in ascending order.



1.
WITH grouped AS
	(SELECT seller_id, SUM(order_cost) AS amount
	FROM Orders
	WHERE DATE_PART('YEAR', sale_date) = 2020
	GROUP BY seller_id)
SELECT main.seller_name
FROM Seller AS main
LEFT JOIN
grouped AS sub
ON main.seller_id = sub.seller_id
WHERE sub.amount = 0 OR sub.amount IS NULL
ORDER BY main.seller_name ASC;

2.
WITH grouped AS
	(SELECT seller_id
	FROM Orders
	WHERE DATE_PART('YEAR', sale_date) = 2020
	GROUP BY seller_id
	HAVING SUM(order_cost) > 0)
SELECT seller_name
FROM Seller
WHERE seller_id NOT IN (SELECT seller_id FROM grouped)
ORDER BY seller_name ASC;