Table: Accounts

+----------------+------+
| Column Name    | Type |
+----------------+------+
| account_id     | int  |
| max_income     | int  |
+----------------+------+
account_id is the column with unique values for this table.
Each row contains information about the maximum monthly income for one bank account.


Table: Transactions

+----------------+----------+
| Column Name    | Type     |
+----------------+----------+
| transaction_id | int      |
| account_id     | int      |
| type           | ENUM     |
| amount         | int      |
| day            | datetime |
+----------------+----------+
transaction_id is the column with unique values for this table.
Each row contains information about one transaction.
type is ENUM (category) type of ('Creditor','Debtor') where 'Creditor' means the user deposited money into their account
and 'Debtor' means the user withdrew money from their account.
amount is the amount of money deposited/withdrawn during the transaction.


A bank account is suspicious if the total income exceeds the max_income for this account for two or more consecutive months.
The total income of an account in some month is the sum of all its deposits in that month (i.e., transactions of the type 'Creditor').

Write a solution to report the IDs of all suspicious bank accounts.

Return the result table in any order.


1.
WITH grouped AS (
    SELECT
        account_id,
        SUM(amount) AS amount,
        EXTRACT(YEAR FROM day) AS year,
        EXTRACT(MONTH FROM day) AS month
    FROM Transactions
    WHERE type = 'Creditor'
    GROUP BY account_id, year, month
),
our_diff AS (
    SELECT
        main.*,
        (((main.year - main.prev_year) * 12) + (main.month - main.prev_month)) AS diff,
        sub.max_income
        FROM (
            SELECT
                *,
                LAG(year, 1) OVER(PARTITION BY account_id ORDER BY year ASC, month ASC) AS prev_year,
                LAG(month, 1) OVER(PARTITION BY account_id ORDER BY year ASC, month ASC) AS prev_month,
                LAG(amount, 1) OVER(PARTITION BY account_id ORDER BY year ASC, month ASC) AS prev_amount
                FROM grouped
        ) AS main
        LEFT JOIN
        Accounts AS sub
        ON sub.account_id = main.account_id
),
result AS (
    SELECT
        *,
        (
        CASE
            WHEN diff <= 1 AND amount > max_income AND prev_amount > max_income THEN 1
            ELSE 0
        END
        ) AS our_check
    FROM our_diff
)
SELECT DISTINCT account_id
FROM result
WHERE our_check = 1;
