Table: Customers

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| customer_id   | int     |
| customer_name | varchar |
+---------------+---------+
customer_id is the column with unique values for this table.
Each row of this table contains the name and the id customer.


Write a solution to find the missing customer IDs.
The missing IDs are ones that are not in the Customers table but are in the range
between 1 and the maximum customer_id present in the table.

Notice that the maximum customer_id will not exceed 100.

Return the result table ordered by ids in ascending order.


1.
SELECT GENERATE_SERIES(1, (SELECT MAX(customer_id) FROM Customers), 1) AS ids
ORDER BY ids ASC
EXCEPT
SELECT customer_id FROM Customers;