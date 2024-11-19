Table: Products

+------------+---------+
| Column Name| Type    |
+------------+---------+
| product_id | int     |
| category   | varchar |
| price      | decimal |
+------------+---------+
product_id is the unique key for this table.
--Each row includes the product's ID, its category, and its price.
Table: Discounts

+------------+---------+
| Column Name| Type    |
+------------+---------+
| category   | varchar |
| discount   | int     |
+------------+---------+
category is the primary key for this table.
Each row contains a product category and the percentage discount applied to that category (values range from 0 to 100).
Write a solution to find the final price of each product after applying the category discount.
--If a product's category has no associated discount, its price remains unchanged.

Return the result table ordered by product_id in ascending order.


1.
SELECT
    main.product_id,
    (main.price - (main.price * COALESCE(sub.discount::NUMERIC / 100, 0))) AS final_price,
    main.category
FROM Products AS main
LEFT JOIN Discounts AS sub
ON sub.category = main.category
ORDER BY product_id ASC;