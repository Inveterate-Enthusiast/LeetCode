--Table: Products
--
--+-------------+---------+
--| Column Name | Type    |
--+-------------+---------+
--| product_id  | int     |
--| store       | varchar |
--| price       | int     |
--+-------------+---------+
--(product_id, store) is the primary key (combination of columns with unique values) for this table.
--Each row of this table indicates the price of product_id in store.
--There will be at most 30 different stores in the table.
--price is the price of the product at this store.
--
--
--Important note: This problem targets those who have a good experience with SQL. If you are a beginner, we recommend that you skip it for now.
--
--Implement the procedure PivotProducts to reorganize the Products table so that each row has the id of one product
--and its price in each store. The price should be null if the product is not sold in a store.
--The columns of the table should contain each store and they should be sorted in lexicographical order.
--
--The procedure should return the table after reorganizing it.
--
--Return the result table in any order.
--
--
--1. But it's MySQL, 'cos there is impossible use PostgreSQL to solve this problem here
CREATE PROCEDURE PivotProducts()
BEGIN
	# Write your MySQL query statement below.
    set session group_concat_max_len = 1000000; # default is 1024

	set @sql = null;
	select group_concat(
		distinct concat(
			'sum(if(store = "', store, '", price, null)) as ', store
		)
	)
	into @sql
	from Products;

	set @sql = concat('select product_id, ', @sql, ' from Products group by 1');

	prepare stmt from @sql;
	execute stmt;
	deallocate prepare stmt;
END