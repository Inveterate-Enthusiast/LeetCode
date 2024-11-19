Table: Transactions

+------------------+---------+
| Column Name      | Type    |
+------------------+---------+
| transaction_id   | int     |
| customer_id      | int     |
| product_id       | int     |
| transaction_date | date    |
| amount           | decimal |
+------------------+---------+
transaction_id is the unique identifier for this table.
Each row of this table contains information about a transaction, including the customer ID, product ID, date, and amount spent.
Table: Products

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| category    | varchar |
| price       | decimal |
+-------------+---------+
product_id is the unique identifier for this table.
Each row of this table contains information about a product, including its category and price.
Write a solution to analyze customer purchasing behavior. For each customer, calculate:

The total amount spent.
The number of transactions.
The number of unique product categories purchased.
The average amount spent.
The most frequently purchased product category (if there is a tie, choose the one with the most recent transaction).
A loyalty score defined as: (Number of transactions * 10) + (Total amount spent / 100).
Round total_amount, avg_transaction_amount, and loyalty_score to 2 decimal places.

Return the result table ordered by loyalty_score in descending order, then by customer_id in ascending order.



1.
WITH merged AS (
    SELECT
        main.customer_id,
        main.product_id,
        main.transaction_id,
        main.amount,
        main.transaction_date,
        sub.category
    FROM Transactions AS main

    LEFT JOIN Products AS sub
        ON sub.product_id = main.product_id
),
find_top AS (
    SELECT
        customer_id,
        category,
        COUNT(DISTINCT transaction_id) AS our_count,
        MAX(transaction_date) AS max_date
    FROM merged
    GROUP BY customer_id, category
),
find_top_2 AS (
    SELECT
        *,
        DENSE_RANK() OVER(PARTITION BY customer_id ORDER BY our_count DESC, max_date DESC) AS our_rank
    FROM find_top
)
SELECT
    main.customer_id,
    SUM(main.amount) AS total_amount,
    COUNT(DISTINCT main.transaction_id) AS transaction_count,
    COUNT(DISTINCT main.category) AS unique_categories,
    ROUND((SUM(main.amount)::NUMERIC / COUNT(DISTINCT main.transaction_id)::NUMERIC), 2) AS avg_transaction_amount,
    MAX(sub.category) AS top_category,
    ROUND(((COUNT(DISTINCT main.transaction_id) * 10)::NUMERIC + (SUM(main.amount)::NUMERIC / 100)), 2) AS loyalty_score
FROM merged AS main

LEFT JOIN (SELECT * FROM find_top_2 WHERE our_rank = 1) AS sub
    ON sub.customer_id = main.customer_id

GROUP BY main.customer_id

ORDER BY loyalty_score DESC, main.customer_id ASC;