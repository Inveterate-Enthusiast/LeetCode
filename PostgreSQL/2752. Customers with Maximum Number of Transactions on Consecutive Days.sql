--Table: Transactions
--
--+------------------+------+
--| Column Name      | Type |
--+------------------+------+
--| transaction_id   | int  |
--| customer_id      | int  |
--| transaction_date | date |
--| amount           | int  |
--+------------------+------+
--transaction_id is the column with unique values of this table.
--Each row contains information about transactions that includes unique (customer_id, transaction_date) along with the corresponding customer_id and amount.
--Write a solution to find all customer_id who made the maximum number of transactions on consecutive days.
--
--Return all customer_id with the maximum number of consecutive transactions. Order the result table by customer_id in ascending order.
--
--
--
--
--1.
WITH windows AS (
    SELECT
        *,
        ROW_NUMBER() OVER(PARTITION BY customer_id ORDER BY transaction_date ASC) AS our_row
    FROM Transactions
),
with_groups AS (
    SELECT
        *,
        (transaction_date - (our_row || 'DAYS')::INTERVAL) AS our_group
    FROM windows
),
grouped AS (
    SELECT
        customer_id,
        our_group,
        COUNT(DISTINCT transaction_date) AS total_number
    FROM with_groups
    GROUP BY customer_id, our_group
)
SELECT
    customer_id
FROM grouped
WHERE total_number = (SELECT MAX(total_number) FROM grouped)
ORDER BY customer_id ASC;