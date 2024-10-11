Table: Sales

+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| sale_id     | int   |
| product_id  | int   |
| user_id     | int   |
| quantity    | int   |
+-------------+-------+
sale_id contains unique values.
product_id is a foreign key (reference column) to Product table.
Each row of this table shows the ID of the product and the quantity purchased by a user.


Table: Product

+-------------+------+
| Column Name | Type |
+-------------+------+
| product_id  | int  |
| price       | int  |
+-------------+------+
product_id contains unique values.
Each row of this table indicates the price of each product.


Write a solution that reports for each user the product id on which the user spent the most money.
In case the same user spent the most money on two or more products, report all of them.

Return the resulting table in any order.


1.
WITH merged AS (
    SELECT
        main.user_id,
        main.product_id,
        (main.quantity * sub.price) AS amount
    FROM Sales AS main

    LEFT JOIN Product AS sub
    ON sub.product_id = main.product_id
),
grouped AS (
    SELECT
        user_id,
        product_id,
        DENSE_RANK() OVER(PARTITION BY user_id ORDER BY SUM(amount) DESC) AS our_rank
        FROM merged
        GROUP BY user_id, product_id
)
SELECT
    user_id, product_id
FROM grouped
WHERE our_rank = 1;