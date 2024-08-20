Table: Orders

+-------------------+------+
| Column Name       | Type |
+-------------------+------+
| order_id          | int  |
| item_count        | int  |
| order_occurrences | int  |
+-------------------+------+
order_id is column of unique values for this table.
This table contains order_id, item_count, and order_occurrences.
Write a solution to calculate the average number of items per order, rounded to 2 decimal places.

Return the result table in any order.


1.
SELECT ROUND((SUM(item_count * order_occurrences)::NUMERIC / SUM(order_occurrences)::NUMERIC)::NUMERIC, 2) AS average_items_per_order
FROM Orders