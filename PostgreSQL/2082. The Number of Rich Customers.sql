Table: Store

+-------------+------+
| Column Name | Type |
+-------------+------+
| bill_id     | int  |
| customer_id | int  |
| amount      | int  |
+-------------+------+
bill_id is the primary key (column with unique values) for this table.
Each row contains information about the amount of one bill and the customer associated with it.


Write a solution to report the number of customers who had at least one bill with an amount strictly greater than 500.



1.
SELECT COUNT(DISTINCT customer_id) AS rich_count
FROM Store
WHERE amount > 500;