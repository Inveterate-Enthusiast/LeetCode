Table: Transactions

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| id             | int     |
| country        | varchar |
| state          | enum    |
| amount         | int     |
| trans_date     | date    |
+----------------+---------+
id is the column of unique values of this table.
The table has information about incoming transactions.
The state column is an ENUM (category) of type ["approved", "declined"].
Table: Chargebacks

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| trans_id       | int     |
| trans_date     | date    |
+----------------+---------+
Chargebacks contains basic information regarding incoming chargebacks from some transactions placed in Transactions table.
trans_id is a foreign key (reference column) to the id column of Transactions table.
Each chargeback corresponds to a transaction made previously even if they were not approved.


Write a solution to find for each month and country: the number of approved transactions and their total amount, the number of chargebacks, and their total amount.

Note: In your solution, given the month and country, ignore rows with all zeros.

Return the result table in any order.


1.
WITH grouped1 AS
    (SELECT TO_CHAR(trans_date, 'YYYY-MM') AS month,
    country,
    COUNT(amount) AS approved_count,
    SUM(amount) AS approved_amount
    FROM Transactions
    WHERE state = 'approved'
    GROUP BY 1, 2),
grouped2 AS
    (SELECT TO_CHAR(main.trans_date, 'YYYY-MM') AS month,
    sub.country,
    COUNT(sub.amount) AS chargeback_count,
    SUM(sub.amount) AS chargeback_amount
    FROM Chargebacks AS main
    LEFT JOIN
    Transactions AS sub
    ON main.trans_id = sub.id
    GROUP BY 1, 2)
SELECT COALESCE(main.month, sub.month) AS month,
COALESCE(main.country, sub.country) AS country,
COALESCE(main.approved_count, 0) AS approved_count,
COALESCE(main.approved_amount, 0) AS approved_amount,
COALESCE(sub.chargeback_count, 0) AS chargeback_count,
COALESCE(sub.chargeback_amount, 0) AS chargeback_amount
FROM grouped1 AS main
FULL OUTER JOIN
grouped2 AS sub
ON main.month = sub.month AND main.country = sub.country;