Table: Loans

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| loan_id     | int     |
| user_id     | int     |
| loan_type   | varchar |
+-------------+---------+
loan_id is column of unique values for this table.
This table contains loan_id, user_id, and loan_type.
--Write a solution to find all distinct user_id's that have at least one Refinance loan type and at least one Mortgage loan type.

Return the result table ordered by user_id in ascending order.


1.
SELECT user_id
FROM Loans
GROUP BY user_id
HAVING (SUM(CASE WHEN loan_type = 'Refinance' THEN 1 ELSE 0 END)) >= 1
AND (SUM(CASE WHEN loan_type = 'Mortgage' THEN 1 ELSE 0 END)) >= 1
ORDER BY user_id ASC;

2.
SELECT user_id
FROM Loans
GROUP BY user_id
HAVING ARRAY_AGG(DISTINCT loan_type)::text[] @> ARRAY['Refinance', 'Mortgage']
ORDER BY user_id ASC;