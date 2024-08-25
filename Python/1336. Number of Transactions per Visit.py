# Table: Visits
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | user_id       | int     |
# | visit_date    | date    |
# +---------------+---------+
# (user_id, visit_date) is the primary key (combination of columns with unique values) for this table.
# Each row of this table indicates that user_id has visited the bank in visit_date.
#
#
# Table: Transactions
#
# +------------------+---------+
# | Column Name      | Type    |
# +------------------+---------+
# | user_id          | int     |
# | transaction_date | date    |
# | amount           | int     |
# +------------------+---------+
# This table may contain duplicates rows.
# Each row of this table indicates that user_id has done a transaction of amount in transaction_date.
# It is guaranteed that the user has visited the bank in the transaction_date.(i.e The Visits table contains (user_id, transaction_date) in one row)
#
#
# A bank wants to draw a chart of the number of transactions bank visitors did in one visit to the bank and the corresponding number of visitors who have done this number of transaction in one visit.
#
# Write a solution to find how many users visited the bank and didn't do any transactions, how many visited the bank and did one transaction, and so on.
#
# The result table will contain two columns:
#
# transactions_count which is the number of transactions done in one visit.
# visits_count which is the corresponding number of users who did transactions_count in one visit to the bank.
# transactions_count should take all values from 0 to max(transactions_count) done by one or more users.
#
# Return the result table ordered by transactions_count.
import numpy as np
import pandas as pd
from pathlib import Path
import os

def draw_chart(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(
        left=visits.rename(columns={"visit_date": "date"}),
        right=transactions.rename(columns={"transaction_date": "date"}),
        how="left",
        on=["user_id", "date"],
        copy=False
    )
    grouped = merged.groupby(by=["user_id", "date"], as_index=False).agg(transactions_count=("amount", "count"))
    grouped = (grouped
                .groupby(by="transactions_count", as_index=False, dropna=False)
                .agg(visits_count=("user_id", "count")))
    return (pd.merge(
        left=(pd.DataFrame({
            "transactions_count": np.arange(0, grouped["transactions_count"].max()+1, 1)
        })),
        right=grouped,
        how="left",
        on="transactions_count"
    )
            .sort_values(by="transactions_count", ascending=True)
            .fillna(0))

path = Path(os.getcwd()) / "data" / "1336. Number of Transactions per Visit.xlsx"
visits = pd.read_excel(path, sheet_name="Visits")
transactions = pd.read_excel(path, sheet_name="Transactions")
print(draw_chart(visits, transactions))