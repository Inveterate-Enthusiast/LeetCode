# Table: Loans
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | loan_id     | int     |
# | user_id     | int     |
# | loan_type   | varchar |
# +-------------+---------+
# loan_id is column of unique values for this table.
# This table contains loan_id, user_id, and loan_type.
# Write a solution to find all distinct user_id's that have at least one Refinance loan type and at least one Mortgage loan type.
#
# Return the result table ordered by user_id in ascending order.
import pandas as pd


def loan_types(loans: pd.DataFrame) -> pd.DataFrame:
    our_set = {"Refinance", "Mortgage"}
    grouped = loans.groupby(by="user_id", as_index=False).agg(our_set=("loan_type", lambda x: set(x)))
    return grouped.loc[grouped["our_set"] >= our_set, ["user_id"]].sort_values(by="user_id", ascending=True)

