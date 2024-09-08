Table: Product

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| product_name  | varchar |
+---------------+---------+
product_id is the primary key (column with unique values) for this table.
product_name is the name of the product.


Table: Sales

+---------------------+---------+
| Column Name         | Type    |
+---------------------+---------+
| product_id          | int     |
| period_start        | date    |
| period_end          | date    |
| average_daily_sales | int     |
+---------------------+---------+
product_id is the primary key (column with unique values) for this table.
period_start and period_end indicate the start and end date for the sales period, and both dates are inclusive.
The average_daily_sales column holds the average daily sales amount of the items for the period.
The dates of the sales years are between 2018 to 2020.


Write a solution to report the total sales amount of each item for each year, with corresponding product_name, product_id, report_year, and total_amount.

Return the result table ordered by product_id and report_year.



1.
WITH sale_dates AS
    (
    SELECT product_id,
    GENERATE_SERIES(period_start, period_end, '1 day'::INTERVAL)::DATE as sale_date,
    average_daily_sales
    FROM Sales
    )
SELECT main.product_id, sub.product_name, TEXT(EXTRACT(YEAR FROM sale_date)) AS report_year, SUM(average_daily_sales) AS total_amount
FROM sale_dates AS main
LEFT JOIN
Product AS sub
ON main.product_id = sub.product_id
GROUP BY main.product_id, sub.product_name, report_year
ORDER BY main.product_id ASC, report_year ASC;