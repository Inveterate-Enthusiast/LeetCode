Table: Transactions

+----------------+----------+
| Column Name    | Type     |
+----------------+----------+
| transaction_id | int      |
| day            | datetime |
| amount         | int      |
+----------------+----------+
transaction_id is the column with unique values for this table.
Each row contains information about one transaction.


Write a solution to report the IDs of the transactions with the maximum amount on their respective day.
If in one day there are multiple such transactions, return all of them.

Return the result table ordered by transaction_id in ascending order.



1.
WITH ranked AS
    (
    SELECT *, RANK() OVER(PARTITION BY day::DATE ORDER BY amount DESC) AS our_rank
    FROM Transactions
    )
SELECT transaction_id
FROM ranked
WHERE our_rank = 1
ORDER BY transaction_id ASC;