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
Each row contains user_id, purchase_date, and amount_spend.
Table: Users

+-------------+------+
| Column Name | Type |
+-------------+------+
| user_id     | int  |
| membership  | enum |
+-------------+------+
user_id is the primary key for this table.
membership is an ENUM (category) type of ('Standard', 'Premium', 'VIP').
Each row of this table indicates the user_id, membership type.
Write a solution to calculate the total spending by Premium and VIP members on each Friday of every week in November 2023.
If there are no purchases on a particular Friday by Premium or VIP members, it should be considered as 0.

Return the result table ordered by week of the month,  and membership in ascending order.



1.
WITH RECURSIVE calendar AS (
    SELECT '2023-11-1'::DATE AS date

    UNION ALL

    SELECT (date + INTERVAL '1 DAY')::DATE
    FROM calendar
    WHERE date < (('2023-11-1'::DATE + INTERVAL '1 MONTH') - INTERVAL '1 DAY')
),
merged_calendar AS (
    SELECT
        calendar.date,
        (EXTRACT(WEEK FROM date) - (EXTRACT(WEEK FROM (MIN(date) OVER()))) + 1) AS week_of_month,
        members.membership
    FROM calendar

    CROSS JOIN
        (SELECT UNNEST(ARRAY['VIP', 'Premium']) AS membership) AS members

    WHERE TRIM(TO_CHAR(date, 'Day')) = 'Friday'
),
grouped AS (
    SELECT
        pur.purchase_date,
        u.membership,
        SUM(amount_spend) AS total_amount
    FROM Purchases AS pur

    LEFT JOIN Users AS u
        ON u.user_id = pur.user_id

    WHERE u.membership IN ('Premium', 'VIP')
    AND TRIM(TO_CHAR(pur.purchase_date, 'Day')) = 'Friday'

    GROUP BY pur.purchase_date, u.membership
)
SELECT
    cal.week_of_month,
    cal.membership,
    COALESCE(gr.total_amount, 0) AS total_amount
FROM merged_calendar AS cal

LEFT JOIN grouped AS gr
    ON gr.purchase_date = cal.date
    AND gr.membership = cal.membership

ORDER BY cal.week_of_month ASC, membership ASC;