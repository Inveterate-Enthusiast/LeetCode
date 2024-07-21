Table: Prices

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| start_date    | date    |
| end_date      | date    |
| price         | int     |
+---------------+---------+
(product_id, start_date, end_date) is the primary key (combination of columns with unique values) for this table.
Each row of this table indicates the price of the product_id in the period from start_date to end_date.
For each product_id there will be no two overlapping periods. That means there will be no two intersecting periods for the same product_id.
 

Table: UnitsSold

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| purchase_date | date    |
| units         | int     |
+---------------+---------+
This table may contain duplicate rows.
Each row of this table indicates the date, units, and product_id of each product sold. 
 

Write a solution to find the average selling price for each product. average_price should be rounded to 2 decimal places.

Return the result table in any order.




1.
WITH merged AS
(SELECT main.product_id, main.price, sub.units FROM Prices AS main LEFT JOIN UnitsSold AS sub ON
main.product_id = sub.product_id AND sub.purchase_date >= main.start_date AND sub.purchase_date <= main.end_date),
grouped AS
(SELECT product_id, SUM(price * units) AS revenue, SUM(units) AS quantity FROM merged GROUP BY product_id ORDER BY product_id ASC)
SELECT product_id,
(CASE WHEN quantity IS NULL THEN 0
ELSE ROUND(revenue::NUMERIC / quantity::NUMERIC, 2)
END) AS average_price 
FROM grouped;
 
2.
SELECT main.product_id,
COALESCE(ROUND(SUM(main.price * sub.units)::NUMERIC / SUM(sub.units)::NUMERIC, 2), 0) AS average_price FROM Prices AS main LEFT JOIN UnitsSold AS sub
ON main.product_id = sub.product_id AND sub.purchase_date >= main.start_date AND sub.purchase_date <= main.end_date
GROUP BY main.product_id
ORDER BY main.product_id ASC;