--Table: Orders
--
--+--------------+------+
--| Column Name  | Type |
--+--------------+------+
--| order_id     | int  |
--| customer_id  | int  |
--| order_date   | date |
--| price        | int  |
--+--------------+------+
--order_id is the column with unique values for this table.
--Each row contains the id of an order, the id of customer that ordered it, the date of the order, and its price.
--
--
--Write a solution to report the IDs of the customers with the total purchases strictly increasing yearly.
--
--The total purchases of a customer in one year is the sum of the prices of their orders in that year.
-- If for some year the customer did not make any order, we consider the total purchases 0.
--The first year to consider for each customer is the year of their first order.
--The last year to consider for each customer is the year of their last order.
--Return the result table in any order.


-- 1.
WITH grouped AS (
    SELECT
        customer_id,
        EXTRACT(YEAR FROM order_date) AS year,
        SUM(price) AS price
    FROM Orders

    GROUP BY customer_id, EXTRACT(YEAR FROM order_date)
),
with_prevs AS (
    SELECT
        *,
        LAG(year, 1) OVER(PARTITION BY customer_id ORDER BY year ASC) AS prev_year,
        LAG(price, 1) OVER(PARTITION BY customer_id ORDER BY year ASC) AS prev_price
    FROM grouped
)
SELECT
    customer_id
FROM with_prevs

GROUP BY customer_id
HAVING
SUM(
    CASE
        WHEN
            ((NOT prev_year IS NULL) AND (NOT (year - prev_year) = 1))
            OR
            ((NOT prev_price IS NULL) AND (price <= prev_price))
            THEN 1
        ELSE 0
    END
) = 0;