Table: Spending

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| user_id     | int     |
| spend_date  | date    |
| platform    | enum    |
| amount      | int     |
+-------------+---------+
The table logs the history of the spending of users that make purchases from an online shopping website that has a desktop and a mobile application.
(user_id, spend_date, platform) is the primary key (combination of columns with unique values) of this table.
The platform column is an ENUM (category) type of ('desktop', 'mobile').


Write a solution to find the total number of users and the total amount spent using the mobile only, the desktop only, and both mobile and desktop together for each date.

Return the result table in any order.


1.
WITH unioned_pl AS
    (SELECT DISTINCT platform
    FROM Spending
    UNION ALL
    SELECT 'both'),
unioned AS
    (SELECT main.platform, sub.spend_date
    FROM unioned_pl AS main
    CROSS JOIN
    (SELECT DISTINCT spend_date FROM Spending) AS sub),
grouped AS
    (SELECT spend_date, user_id,
    (CASE WHEN COUNT(DISTINCT platform) > 1 THEN 'both' ELSE MIN(DISTINCT platform) END) AS platform,
    SUM(amount) AS total_amount,
    COUNT(DISTINCT user_id) AS total_users
    FROM Spending
    GROUP BY spend_date, user_id),
final_grouped AS
    (SELECT spend_date, platform, SUM(total_amount) AS total_amount, SUM(total_users) AS total_users
    FROM grouped
    GROUP BY spend_date, platform)
SELECT sub.spend_date, sub.platform, COALESCE(main.total_amount, 0) AS total_amount, COALESCE(main.total_users, 0) AS total_users
FROM final_grouped AS main
RIGHT JOIN
unioned AS sub
ON main.spend_date = sub.spend_date AND main.platform = sub.platform;
