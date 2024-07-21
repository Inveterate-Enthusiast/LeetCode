Table: Products

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| store       | enum    |
| price       | int     |
+-------------+---------+
In SQL, (product_id, store) is the primary key for this table.
store is a category of type ('store1', 'store2', 'store3') where each represents the store this product is available at.
price is the price of the product at this store.
 

Find the price of each product in each store.

Return the result table in any order.



1.
SELECT product_id,
SUM(CASE WHEN store = 'store1' THEN price END) AS store1,
SUM(CASE WHEN store = 'store2' THEN price END) AS store2,
SUM(CASE WHEN store = 'store3' THEN price END) AS store3
FROM Products
GROUP BY product_id;