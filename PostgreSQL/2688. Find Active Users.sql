Table: Users

+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| user_id     | int      |
| item        | varchar  |
| created_at  | datetime |
| amount      | int      |
+-------------+----------+
This table may contain duplicate records.
Each row includes the user ID, the purchased item, the date of purchase, and the purchase amount.
Write a solution to identify active users. An active user is a user that has made
a second purchase within 7 days of any other of their purchases.

For example, if the ending date is May 31, 2023. So any date between May 31, 2023, and June 7, 2023 (inclusive)
would be considered "within 7 days" of May 31, 2023.

Return a list of user_id which denotes the list of active users in any order.




1.
WITH with_prev AS (
    SELECT
        *,
        LAG(created_at) OVER(PARTITION BY user_id ORDER BY created_at ASC) AS prev_date
    FROM Users
)
SELECT
    DISTINCT user_id
FROM with_prev
WHERE (EXTRACT(EPOCH FROM AGE(created_at, prev_date))::NUMERIC / 60 / 60 / 24) <= 7;