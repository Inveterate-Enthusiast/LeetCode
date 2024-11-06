Table: transactions

+------------------+------+
| Column Name      | Type |
+------------------+------+
| transaction_id   | int  |
| amount           | int  |
| transaction_date | date |
+------------------+------+
The transactions_id column uniquely identifies each row in this table.
Each row of this table contains the transaction id, amount and transaction date.
Write a solution to find the sum of amounts for odd and even transactions for each day.
If there are no odd or even transactions for a specific date, display as 0.

Return the result table ordered by transaction_date in ascending order.


1.
SELECT
    transaction_date,
    COALESCE(SUM(CASE WHEN amount%2 <> 0 THEN amount END), 0) AS odd_sum,
    COALESCE(SUM(CASE WHEN amount%2 = 0 THEN amount END), 0) AS even_sum
FROM transactions
GROUP BY transaction_date
ORDER BY transaction_date ASC;