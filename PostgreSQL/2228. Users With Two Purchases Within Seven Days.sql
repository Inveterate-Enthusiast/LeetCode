Table: Purchases

+---------------+------+
| Column Name   | Type |
+---------------+------+
| purchase_id   | int  |
| user_id       | int  |
| purchase_date | date |
+---------------+------+
purchase_id contains unique values.
This table contains logs of the dates that users purchased from a certain retailer.


Write a solution to report the IDs of the users that made any two purchases at most 7 days apart.

Return the result table ordered by user_id.



1.
WITH diffed AS (
    SELECT *, purchase_date - LAG(purchase_date, 1) OVER(PARTITION BY user_id ORDER BY purchase_date ASC) AS diff
    FROM Purchases
)
SELECT DISTINCT user_id
FROM diffed
WHERE diff <= 7
ORDER BY user_id ASC;