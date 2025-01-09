--Table: Products
--
--+-------------+---------+
--| Column Name | Type    |
--+-------------+---------+
--| product_id  | int     |
--| name        | varchar |
--+-------------+---------+
--product_id is the unique key for this table.
--Each row of this table contains the ID and name of a product.
--Write a solution to find all products whose names contain a sequence of exactly three digits in a row.
--
--Return the result table ordered by product_id in ascending order.
--
--
--1.
SELECT
    *
FROM Products
WHERE name ~ '.*(?<!\d)\d{3}(?!\d).*'
ORDER BY product_id ASC;