--Table: user_transactions
--
--+------------------+----------+
--| Column Name      | Type     |
--+------------------+----------+
--| transaction_id   | integer  |
--| product_id       | integer  |
--| spend            | decimal  |
--| transaction_date | datetime |
--+------------------+----------+
--The transaction_id column uniquely identifies each row in this table.
--Each row of this table contains the transaction ID, product ID, the spend amount, and the transaction date.
--Write a solution to calculate the year-on-year growth rate for the total spend for each product.
--
--The result table should include the following columns:
--
--year: The year of the transaction.
--product_id: The ID of the product.
--curr_year_spend: The total spend for the current year.
--prev_year_spend: The total spend for the previous year.
--yoy_rate: The year-on-year growth rate percentage, rounded to 2 decimal places.
--Return the result table ordered by product_id,year in ascending order.
--
--
--1.
WITH grouped AS (
    SELECT
        product_id,
        EXTRACT(YEAR FROM transaction_date) AS year,
        SUM(spend) AS curr_year_spend
    FROM user_transactions

    GROUP BY product_id, EXTRACT(YEAR FROM transaction_date)
)
SELECT
    main.year,
    main.product_id,
    main.curr_year_spend,
    sub.curr_year_spend AS prev_year_spend,
    (
        CASE
            WHEN sub.curr_year_spend IS NULL THEN NULL
            ELSE ROUND(((main.curr_year_spend - sub.curr_year_spend) / ABS(sub.curr_year_spend)) * 100, 2)
        END
    ) AS yoy_rate
FROM grouped AS main

LEFT JOIN grouped AS sub
    ON (sub.year + 1) = main.year
    AND sub.product_id = main.product_id

ORDER BY main.product_id ASC, main.year ASC;