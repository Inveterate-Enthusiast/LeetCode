Table: Transactions

+-------------+------+
| Column Name | Type |
+-------------+------+
| account_id  | int  |
| day         | date |
| type        | ENUM |
| amount      | int  |
+-------------+------+
(account_id, day) is the primary key (combination of columns with unique values) for this table.
Each row contains information about one transaction, including the transaction type, the day it occurred on, and the amount.
type is an ENUM (category) of the type ('Deposit','Withdraw')


Write a solution to report the balance of each user after each transaction.
You may assume that the balance of each account before any transaction is 0 and that the balance will never be below 0 at any moment.

Return the result table in ascending order by account_id, then by day in case of a tie.

1.
SELECT account_id, day,
SUM(
    CASE
        WHEN type = 'Deposit' THEN amount
        WHEN type = 'Withdraw' THEN -amount
        ELSE 0
    END
) OVER(PARTITION BY account_id ORDER BY day ASC) AS balance
FROM Transactions
ORDER BY account_id ASC, day ASC;