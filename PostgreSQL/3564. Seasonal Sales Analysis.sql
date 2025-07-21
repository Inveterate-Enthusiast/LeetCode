-- Table: sales
--
--+---------------+---------+
--| Column Name   | Type    |
--+---------------+---------+
--| sale_id       | int     |
--| product_id    | int     |
--| sale_date     | date    |
--| quantity      | int     |
--| price         | decimal |
--+---------------+---------+
--sale_id is the unique identifier for this table.
--Each row contains information about a product sale including the product_id, date of sale, quantity sold, and price per unit.
--Table: products
--
--+---------------+---------+
--| Column Name   | Type    |
--+---------------+---------+
--| product_id    | int     |
--| product_name  | varchar |
--| category      | varchar |
--+---------------+---------+
--product_id is the unique identifier for this table.
--Each row contains information about a product including its name and category.
--Write a solution to find the most popular product category for each season. The seasons are defined as:
--
--Winter: December, January, February
--Spring: March, April, May
--Summer: June, July, August
--Fall: September, October, November
--The popularity of a category is determined by the total quantity sold in that season. If there is a tie, select the category with the highest total revenue (quantity × price).
--
--Return the result table ordered by season in ascending order.

WITH products AS (
    SELECT
        main.product_id,
        sub.category,
        main.quantity,
        (main.quantity * main.price) AS revenue,

        (
            CASE
                WHEN EXTRACT(MONTH FROM main.sale_date) IN (12, 1, 2) THEN 'Winter'
                WHEN EXTRACT(MONTH FROM main.sale_date) IN (3, 4, 5) THEN 'Spring'
                WHEN EXTRACT(MONTH FROM main.sale_date) IN (6, 7, 8) THEN 'Summer'
                WHEN EXTRACT(MONTH FROM main.sale_date) IN (9, 10, 11) THEN 'Fall'
            END
        ) AS season
    FROM sales AS main

    LEFT JOIN products AS sub
        ON sub.product_id = main.product_id
),
grouped AS (
    SELECT
        season,
        category,
        SUM(quantity) AS total_quantity,
        SUM(revenue) AS total_revenue
    FROM products

    GROUP BY
        season,
        category
),
ranked AS (
    SELECT
        *,
        DENSE_RANK() OVER(PARTITION BY season ORDER BY total_quantity DESC, total_revenue DESC) AS our_rank
    FROM grouped
)
SELECT
    season,
    category,
    total_quantity,
    total_revenue
FROM ranked

WHERE
    our_rank = 1

ORDER BY
    season ASC;