Table: Purchases

+---------------+------+
| Column Name   | Type |
+---------------+------+
| user_id       | int  |
| purchase_date | date |
| amount_spend  | int  |
+---------------+------+
(user_id, purchase_date, amount_spend) is the primary key (combination of columns with unique values) for this table.
purchase_date will range from November 1, 2023, to November 30, 2023, inclusive of both dates.
Each row contains user id, purchase date, and amount spend.
Write a solution to calculate the total spending by users on each Friday of every week in November 2023.
Output only weeks that include at least one purchase on a Friday.

Return the result table ordered by week of month in ascending order.



1.
WITH with_week_num AS (
    SELECT
        *,
        ((EXTRACT(WEEK FROM purchase_date)) - (EXTRACT(WEEK FROM MAKE_DATE(EXTRACT(YEAR FROM purchase_date)::INTEGER, EXTRACT(MONTH FROM purchase_date)::INTEGER, 1))) + 1) AS week_of_month
    FROM Purchases

    WHERE EXTRACT(YEAR FROM purchase_date) = 2023
    AND EXTRACT(MONTH FROM purchase_date) = 11
    AND EXTRACT(DOW FROM purchase_date) = 5
)
SELECT
    week_of_month,
    purchase_date,
    SUM(amount_spend) AS total_amount
FROM with_week_num
GROUP BY 1, 2
ORDER BY week_of_month ASC;