--Table: Purchases
--
--+---------------+------+
--| Column Name   | Type |
--+---------------+------+
--| user_id       | int  |
--| purchase_date | date |
--| amount_spend  | int  |
--+---------------+------+
--(user_id, purchase_date, amount_spend) is the primary key (combination of columns with unique values) for this table.
--purchase_date will range from November 1, 2023, to November 30, 2023, inclusive of both dates.
--Each row contains user id, purchase date, and amount spend.
--Write a solution to calculate the total spending by users on each Friday of every week in November 2023.
--If there are no purchases on a particular Friday of a week, it will be considered as 0.
--
--Return the result table ordered by week of month in ascending order.
--
--
--
--1.
WITH RECURSIVE cal AS (
    SELECT TO_DATE('2023-11-01', 'YYYY-MM-DD') AS purchase_date

    UNION ALL

    SELECT (purchase_date + INTERVAL '1 DAY')::DATE
    FROM cal
    WHERE purchase_date < (TO_DATE('2023-12-01', 'YYYY-MM-DD') - INTERVAL '1 DAY')::DATE
),
merged AS (
    SELECT
        cal.purchase_date,
        TO_CHAR(cal.purchase_date, 'D') AS day_of_week,
        EXTRACT(WEEK FROM cal.purchase_date) - EXTRACT(WEEK FROM DATE_TRUNC('month', cal.purchase_date)) + 1 AS week_of_month,
        SUM(sub.amount_spend) AS total_amount
    FROM cal

    LEFT JOIN Purchases AS sub
        ON sub.purchase_date = cal.purchase_date

    GROUP BY cal.purchase_date
)
SELECT
    week_of_month,
    purchase_date,
    COALESCE(total_amount, 0) AS total_amount
FROM merged

WHERE day_of_week = '6'
ORDER BY week_of_month ASC;