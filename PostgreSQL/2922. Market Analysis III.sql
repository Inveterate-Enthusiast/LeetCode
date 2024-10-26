Table: Users

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| seller_id      | int     |
| join_date      | date    |
| favorite_brand | varchar |
+----------------+---------+
seller_id is column of unique values for this table.
This table contains seller id, join date, and favorite brand of sellers.
Table: Items

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| item_id       | int     |
| item_brand    | varchar |
+---------------+---------+
item_id is the column of unique values for this table.
This table contains item id and item brand.
Table: Orders

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| order_id      | int     |
| order_date    | date    |
| item_id       | int     |
| seller_id     | int     |
+---------------+---------+
order_id is the column of unique values for this table.
item_id is a foreign key to the Items table.
seller_id is a foreign key to the Users table.
This table contains order id, order date, item id and seller id.
Write a solution to find the top seller who has sold the highest number of unique items
with a different brand than their favorite brand. If there are multiple sellers with the same highest count, return all of them.

Return the result table ordered by seller_id in ascending order.




1.
WITH with_brands AS (
    SELECT
        ord.seller_id,
        ord.item_id,
        (CASE WHEN (NOT us.favorite_brand IS NULL AND us.favorite_brand = it.item_brand) THEN 0 ELSE 1 END) AS flag
    FROM Orders AS ord

    LEFT JOIN Items AS it
    ON it.item_id = ord.item_id

    LEFT JOIN Users AS us
    ON us.seller_id = ord.seller_id
    AND us.join_date <= ord.order_date
),
grouped AS (
    SELECT
        seller_id,
        COUNT(DISTINCT item_id) AS num_items
    FROM with_brands
    WHERE flag = 1
    GROUP BY seller_id
)
SELECT
    seller_id,
    num_items
FROM grouped
WHERE num_items = (SELECT MAX(num_items) FROM grouped)
ORDER BY seller_id ASC;