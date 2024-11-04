Table: Fraud

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| policy_id   | int     |
| state       | varchar |
| fraud_score | int     |
+-------------+---------+
policy_id is column of unique values for this table.
This table contains policy id, state, and fraud score.
The Leetcode Insurance Corp has developed an ML-driven predictive model to detect the likelihood of fraudulent claims.
Consequently, they allocate their most seasoned claim adjusters to address the top 5% of claims flagged by this model.

Write a solution to find the top 5 percentile of claims from each state.

Return the result table ordered by state in ascending order, fraud_score in descending order, and policy_id in ascending order.



1.
WITH ranked AS (
    SELECT
        *,
        DENSE_RANK() OVER(PARTITION BY state ORDER BY fraud_score DESC) AS our_rank
    FROM Fraud
)
SELECT
    policy_id,
    state,
    fraud_score
FROM ranked
WHERE our_rank = 1
ORDER BY state ASC, fraud_score DESC, policy_id ASC;