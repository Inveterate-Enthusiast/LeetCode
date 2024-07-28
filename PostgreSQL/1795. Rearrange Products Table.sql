Table: Products

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| store1      | int     |
| store2      | int     |
| store3      | int     |
+-------------+---------+
product_id is the primary key (column with unique values) for this table.
Each row in this table indicates the product's price in 3 different stores: store1, store2, and store3.
If the product is not available in a store, the price will be null in that store's column.


Write a solution to rearrange the Products table so that each row has (product_id, store, price).
If a product is not available in a store, do not include a row with that product_id and store combination in the result table.

Return the result table in any order.



1.
WITH unpivoted AS
    (SELECT product_id,
    UNNEST(ARRAY['store1', 'store2', 'store3']) AS store,
    UNNEST(ARRAY[store1, store2, store3]) AS price
    FROM Products)
SELECT *
FROM unpivoted
WHERE price IS NOT NULL;