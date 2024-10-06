Table: Orders

+---------------+------+
| Column Name   | Type |
+---------------+------+
| order_id      | int  |
| product_id    | int  |
| quantity      | int  |
| purchase_date | date |
+---------------+------+
order_id contains unique values.
Each row in this table contains the ID of an order, the id of the product purchased, the quantity, and the purchase date.


Write a solution to report the IDs of all the products that were ordered three or more times in two consecutive years.

Return the result table in any order.



1.
WITH grouped AS (
    SELECT
        product_id,
        EXTRACT(YEAR FROM purchase_date) AS year,
        COUNT(order_id) AS count
    FROM Orders
    GROUP BY product_id, year
),
with_prev AS (
    SELECT
        *,
        LAG(count, 1) OVER(PARTITION BY product_id ORDER BY year ASC) AS prev_count,
        LAG(year, 1) OVER(PARTITION BY product_id ORDER BY year ASC) AS prev_year
    FROM grouped
)
SELECT DISTINCT product_id
FROM with_prev
WHERE count >= 3 AND prev_count >= 3 AND (year - prev_year) = 1;