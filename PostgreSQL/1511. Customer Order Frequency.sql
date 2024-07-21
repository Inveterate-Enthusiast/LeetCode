Table: Customers

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| customer_id   | int     |
| name          | varchar |
| country       | varchar |
+---------------+---------+
customer_id is the column with unique values for this table.
This table contains information about the customers in the company.
 

Table: Product

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| description   | varchar |
| price         | int     |
+---------------+---------+
product_id is the column with unique values for this table.
This table contains information on the products in the company.
price is the product cost.
 

Table: Orders

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| order_id      | int     |
| customer_id   | int     |
| product_id    | int     |
| order_date    | date    |
| quantity      | int     |
+---------------+---------+
order_id is the column with unique values for this table.
This table contains information on customer orders.
customer_id is the id of the customer who bought "quantity" products with id "product_id".
Order_date is the date in format ('YYYY-MM-DD') when the order was shipped.
 

Write a solution to report the customer_id and customer_name of customers who have spent at least $100 in each month of June and July 2020.

Return the result table in any order.


1.
WITH merged AS
	(SELECT main.customer_id, main.order_date, 
	(main.quantity * sub.price) AS total_sum
	FROM Orders AS main
	LEFT JOIN
	Product AS sub
	ON main.product_id = sub.product_id)
SELECT DISTINCT main.customer_id, sub.name
FROM merged AS main
LEFT JOIN
Customers AS sub
ON main.customer_id = sub.customer_id
WHERE
main.customer_id IN 
	(SELECT customer_id
	FROM merged
	WHERE TO_CHAR(order_date, 'YYYY-MM') = '2020-06'
	GROUP BY customer_id
	HAVING SUM(total_sum) >= 100)
AND main.customer_id IN 
	(SELECT customer_id
	FROM merged
	WHERE TO_CHAR(order_date, 'YYYY-MM') = '2020-07'
	GROUP BY customer_id
	HAVING SUM(total_sum) >= 100);
	
2.
WITH merged AS
	(SELECT main.customer_id, main.order_date, 
	(main.quantity * sub.price) AS total_sum
	FROM Orders AS main
	LEFT JOIN
	Product AS sub
	ON main.product_id = sub.product_id)
SELECT DISTINCT main.customer_id, sub.name
FROM merged AS main
LEFT JOIN
Customers AS sub
ON main.customer_id = sub.customer_id
WHERE
main.customer_id IN
	(SELECT DISTINCT customer_id
	FROM merged
	GROUP BY customer_id
	HAVING
	SUM(CASE WHEN TO_CHAR(order_date, 'YYYY-MM') = '2020-06' THEN total_sum ELSE 0 END) >= 100 
	AND 
	SUM(CASE WHEN TO_CHAR(order_date, 'YYYY-MM') = '2020-07' THEN total_sum ELSE 0 END) >= 100);