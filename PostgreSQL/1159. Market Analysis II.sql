Table: Users

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| user_id        | int     |
| join_date      | date    |
| favorite_brand | varchar |
+----------------+---------+
user_id is the primary key (column with unique values) of this table.
This table has the info of the users of an online shopping website where users can sell and buy items.


Table: Orders

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| order_id      | int     |
| order_date    | date    |
| item_id       | int     |
| buyer_id      | int     |
| seller_id     | int     |
+---------------+---------+
order_id is the primary key (column with unique values) of this table.
item_id is a foreign key (reference column) to the Items table.
buyer_id and seller_id are foreign keys to the Users table.


Table: Items

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| item_id       | int     |
| item_brand    | varchar |
+---------------+---------+
item_id is the primary key (column with unique values) of this table.


Write a solution to find for each user whether the brand of the second item (by date) they sold is their favorite brand.
If a user sold less than two items, report the answer for that user as no.
It is guaranteed that no seller sells more than one item in a day.

Return the result table in any order.


1.
WITH ranked AS
    (SELECT seller_id, item_id, DENSE_RANK() OVER (PARTITION BY seller_id ORDER BY order_date ASC) AS our_rank
    FROM Orders),
filtered AS
    (SELECT seller_id, MAX(our_rank) AS our_rank
    FROM ranked
    WHERE our_rank = 1 OR our_rank = 2
    GROUP BY seller_id),
merged AS
    (SELECT end_sub.user_id, COALESCE(main.our_rank, 1) AS our_rank, new_sub.item_brand, end_sub.favorite_brand
    FROM filtered AS main
    LEFT JOIN
    ranked AS sub
    ON main.seller_id = sub.seller_id AND main.our_rank = sub.our_rank
    LEFT JOIN
    Items AS new_sub
    ON sub.item_id = new_sub.item_id
    RIGHT JOIN
    Users AS end_sub
    ON end_sub.user_id = main.seller_id)
SELECT user_id AS seller_id, (
CASE
    WHEN our_rank = 1 THEN 'no'
    WHEN item_brand != favorite_brand THEN 'no'
    ELSE 'yes'
END
) AS "2nd_item_fav_brand"
FROM merged;