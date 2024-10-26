Table: Transactions

+------------------+----------+
| Column Name      | Type     |
+------------------+----------+
| user_id          | int      |
| spend            | decimal  |
| transaction_date | datetime |
+------------------+----------+
(user_id, transaction_date) is column of unique values for this table.
This table contains user_id, spend, and transaction_date.
Write a solution to find the third transaction (if they have at least three transactions) of every user,
where the spending on the preceding two transactions is lower than the spending on the third transaction.

Return the result table by user_id in ascending order.

1.
WITH ranked AS (
    SELECT
        *,
        DENSE_RANK() OVER(PARTITION BY user_id ORDER BY transaction_date ASC) AS our_rank,
        LAG(spend, 1) OVER(PARTITION BY user_id ORDER BY transaction_date ASC) AS prev_1,
        LAG(spend, 2) OVER(PARTITION BY user_id ORDER BY transaction_date ASC) AS prev_2
    FROM Transactions
)
SELECT
    user_id,
    spend AS third_transaction_spend,
    transaction_date AS third_transaction_date
FROM ranked
WHERE our_rank = 3
AND spend > prev_1
AND spend > prev_2
ORDER BY user_id;