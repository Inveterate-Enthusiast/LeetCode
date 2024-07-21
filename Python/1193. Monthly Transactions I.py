#Table: Transactions
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | id            | int     |
# | country       | varchar |
# | state         | enum    |
# | amount        | int     |
# | trans_date    | date    |
# +---------------+---------+
# id is the primary key of this table.
# The table has information about incoming transactions.
# The state column is an enum of type ["approved", "declined"].
#
#
# Write an SQL query to find for each month and country, the number of transactions and their total amount, the number of approved transactions and their total amount.
#
# Return the result table in any order.
import inspect
import pandas as pd
from pathlib import Path
import os

def get_stats(df: pd.DataFrame) -> pd.DataFrame:
    trans_count = approved_count = trans_total_amount = approved_total_amount = 0
    for index, row in df.iterrows():
        trans_count += 1
        trans_total_amount += row["amount"]
        if row["state"] == "approved":
            approved_count += 1
            approved_total_amount += row["amount"]
    return pd.DataFrame({
        "trans_count": [trans_count],
        "approved_count": [approved_count],
        "trans_total_amount": [trans_total_amount],
        "approved_total_amount": [approved_total_amount]
    })


def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    transactions["month"] = transactions["trans_date"].dt.strftime("%Y-%m")
    return (transactions.groupby(by=["month", "country"], as_index=True, dropna=False)
            .apply(get_stats, include_groups=False)
            .reset_index()
            .drop(columns="level_2"))

def monthly_transactions1(transactions: pd.DataFrame) -> pd.DataFrame:
    transactions["month"] = transactions["trans_date"].dt.strftime("%Y-%m")
    transactions["state"] = transactions.apply(lambda x: x["amount"] if x["state"] == "approved" else pd.NA, axis=1)
    return (transactions.groupby(by=["month", "country"], as_index=False, dropna=False)
            .agg(
                trans_count=("id", "count"),
                approved_count=("state", "count"),
                trans_total_amount=("amount", "sum"),
                approved_total_amount=("state", "sum")
            ))

path = Path(os.getcwd()) / "data" / "1193. Monthly Transactions I.xlsx"
transactions = pd.read_excel(path)
print(monthly_transactions1(transactions))
