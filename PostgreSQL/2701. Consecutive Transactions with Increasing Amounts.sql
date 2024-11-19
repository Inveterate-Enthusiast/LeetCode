Table: Transactions

+------------------+------+
| Column Name      | Type |
+------------------+------+
| transaction_id   | int  |
| customer_id      | int  |
| transaction_date | date |
| amount           | int  |
+------------------+------+
transaction_id is the primary key of this table. 
Each row contains information about transactions that includes unique (customer_id, transaction_date) along with the corresponding customer_id and amount.  
Write an SQL query to find the customers who have made consecutive transactions with increasing amount for at least three consecutive days. Include the customer_id, start date of the consecutive transactions period and the end date of the consecutive transactions period. There can be multiple consecutive transactions by a customer.

Return the result table ordered by customer_id in ascending order.


1.
WITH sub AS (
    SELECT
        main.customer_id,
        main.transaction_date AS date_1,
        sub.transaction_date AS date_2,
        main.amount,
        main.transaction_date - (ROW_NUMBER() OVER(PARTITION BY main.customer_id ORDER BY main.transaction_date) * INTERVAL '1 DAY') AS diff
    FROM Transactions AS main

    INNER JOIN Transactions AS sub
        ON sub.customer_id = main.customer_id
        AND sub.transaction_date = (main.transaction_date + INTERVAL '1 DAY')
        AND sub.amount > main.amount
)
SELECT
    customer_id,
    MIN(date_1) AS consecutive_start,
    MAX(date_2) AS consecutive_end
FROM sub
GROUP BY customer_id, diff
HAVING COUNT(*) >= 2
ORDER BY customer_id;