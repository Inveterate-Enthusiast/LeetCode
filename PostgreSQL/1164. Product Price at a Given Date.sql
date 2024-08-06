Table: Products

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| new_price     | int     |
| change_date   | date    |
+---------------+---------+
(product_id, change_date) is the primary key (combination of columns with unique values) of this table.
Each row of this table indicates that the price of some product was changed to a new price at some date.
 

Write a solution to find the prices of all products on 2019-08-16. Assume the price of all products before any change is 10.

Return the result table in any order.

1.
WITH grouped AS
	(SELECT product_id, MAX(change_date) AS change_date
	FROM Products AS main
	WHERE change_date <= '2019-08-16'::DATE
	GROUP BY product_id)
SELECT DISTINCT product_id, 
(CASE
	WHEN main.product_id IN (SELECT product_id FROM grouped) 
	THEN (SELECT new_price FROM Products AS sub WHERE sub.product_id = main.product_id AND sub.change_date = (SELECT change_date FROM grouped AS sub WHERE sub.product_id = main.product_id))
	ELSE 10
END
) 
AS price
FROM Products AS main
ORDER BY product_id ASC;


2.
WITH grouped AS
	(SELECT product_id, MAX(change_date) AS change_date
	FROM Products AS main
	WHERE change_date <= '2019-08-16'::DATE
	GROUP BY product_id),
our_unique AS
	(SELECT DISTINCT product_id
	FROM Products)
SELECT main.product_id, COALESCE(sub2.new_price, 10) AS price
FROM our_unique AS main
LEFT JOIN
grouped AS sub1
ON main.product_id = sub1.product_id
LEFT JOIN
Products AS sub2
ON main.product_id = sub2.product_id AND sub1.change_date = sub2.change_date;


3.
WITH past_time AS
    (SELECT *, DENSE_RANK() OVER(PARTITION BY product_id ORDER BY change_date DESC) AS our_rank
    FROM Products
    WHERE change_date <= '2019-08-16'::DATE)
SELECT main.product_id, COALESCE(sub.new_price, 10) AS price
FROM (SELECT DISTINCT product_id FROM Products) AS main
LEFT JOIN
(SELECT * FROM past_time WHERE our_rank = 1) AS sub
ON main.product_id = sub.product_id;