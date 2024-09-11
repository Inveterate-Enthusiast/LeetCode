# Table: Users
#
# +--------------+---------+
# | Column Name  | Type    |
# +--------------+---------+
# | user_id      | int     |
# | user_name    | varchar |
# | credit       | int     |
# +--------------+---------+
# user_id is the primary key (column with unique values) for this table.
# Each row of this table contains the current credit information for each user.
#
#
# Table: Transactions
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | trans_id      | int     |
# | paid_by       | int     |
# | paid_to       | int     |
# | amount        | int     |
# | transacted_on | date    |
# +---------------+---------+
# trans_id is the primary key (column with unique values) for this table.
# Each row of this table contains information about the transaction in the bank.
# User with id (paid_by) transfer money to user with id (paid_to).
#
#
# Leetcode Bank (LCB) helps its coders in making virtual payments.
# Our bank records all transactions in the table Transaction,
# we want to find out the current balance of all users and check whether they have breached
# their credit limit (If their current credit is less than 0).
#
# Write a solution to report.
#
# user_id,
# user_name,
# credit, current balance after performing transactions, and
# credit_limit_breached, check credit_limit ("Yes" or "No")
# Return the result table in any order.
import pandas as pd
import numpy as np

def bank_account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    income = transactions.groupby(by="paid_to", as_index=False).agg(income=("amount", "sum")).rename(columns={"paid_to": "user_id"})
    expense = transactions.groupby(by="paid_by", as_index=False).agg(expense=("amount", "sum")).rename(columns={"paid_by": "user_id"})
    merged = pd.merge(
        left=users,
        right=income,
        how="left",
        on="user_id"
    ).fillna(0)
    merged = pd.merge(
        left=merged,
        right=expense,
        how="left",
        on="user_id"
    ).fillna(0)
    merged["credit"] = merged["credit"] - merged["expense"] + merged["income"]
    merged["credit_limit_breached"] = np.where(merged["credit"] < 0, "Yes", "No")
    return merged[users.columns.to_list() + ["credit_limit_breached"]]