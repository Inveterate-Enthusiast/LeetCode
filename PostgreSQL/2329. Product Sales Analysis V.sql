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
product_id is a foreign key (column with unique values) to Product table.
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


Write a solution to report the spending of each user.

Return the resulting table ordered by spending in descending order. In case of a tie, order them by user_id in ascending order.

1.
SELECT main.user_id, SUM(main.quantity * sub.price) AS spending
FROM Sales AS main
LEFT JOIN
Product AS sub
ON main.product_id = sub.product_id
GROUP BY main.user_id
ORDER BY spending DESC, user_id ASC;