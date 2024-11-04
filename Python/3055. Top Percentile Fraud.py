# Table: Fraud
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | policy_id   | int     |
# | state       | varchar |
# | fraud_score | int     |
# +-------------+---------+
# policy_id is column of unique values for this table.
# This table contains policy id, state, and fraud score.
# The Leetcode Insurance Corp has developed an ML-driven predictive model to detect the likelihood of fraudulent claims.
# Consequently, they allocate their most seasoned claim adjusters to address the top 5% of claims flagged by this model.
#
# Write a solution to find the top 5 percentile of claims from each state.
#
# Return the result table ordered by state in ascending order, fraud_score in descending order, and policy_id in ascending order.
import pandas as pd

def top_percentile_fraud(fraud: pd.DataFrame) -> pd.DataFrame:
    fraud["rank"] = fraud.groupby(by="state", as_index=False)["fraud_score"].rank(method="dense", ascending=False)
    return (fraud
            .loc[fraud["rank"] == 1]
            .drop(labels="rank", axis=1)
            .sort_values(by=["state", "fraud_score", "policy_id"], ascending=[True, False, True]))
