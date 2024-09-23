# Table: Transactions
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | account_id  | int  |
# | day         | date |
# | type        | ENUM |
# | amount      | int  |
# +-------------+------+
# (account_id, day) is the primary key (combination of columns with unique values) for this table.
# Each row contains information about one transaction, including the transaction type, the day it occurred on, and the amount.
# type is an ENUM (category) of the type ('Deposit','Withdraw')
#
#
# Write a solution to report the balance of each user after each transaction.
# You may assume that the balance of each account before any transaction is 0 and that the balance will never be below 0 at any moment.
#
# Return the result table in ascending order by account_id, then by day in case of a tie.
import pandas as pd
from pathlib import Path
import os

def grouping(df: pd.DataFrame) -> pd.Series:
    balance_list = list()
    cur_balance = 0
    for index, row in df.iterrows():
        cur_balance += row["amount"] if row["type"] == "Deposit" else -(row["amount"])
        cur_balance = cur_balance if cur_balance >= 0 else 0
        balance_list.append(cur_balance)

    return pd.Series(
        data=[df["day"], balance_list],
        index=["day", "balance"]
    )

def account_balance(transactions: pd.DataFrame) -> pd.DataFrame:
    if transactions.empty:
        return pd.DataFrame({
            "account_id": list(),
            "day": list(),
            "balance": list()
        })
    grouped = transactions.sort_values(by="day", ascending=True).groupby(by="account_id", as_index=True).apply(grouping, include_groups=False).reset_index()
    exploded = grouped.explode(["day", "balance"])
    return exploded.sort_values(by=["account_id", "day"], ascending=[True, True])

def account_balance1(transactions: pd.DataFrame) -> pd.DataFrame:
    transactions.sort_values(by="day", ascending=True, inplace=True)
    transactions["balance_change"] = transactions.apply(lambda x: x["amount"] if x["type"] == "Deposit" else -(x["amount"]), axis=1)
    transactions["balance"] = transactions.groupby(by="account_id", as_index=False)["balance_change"].cumsum()
    return transactions[["account_id", "day", "balance"]].sort_values(by=["account_id", "day"], ascending=[True, True])

transactions = pd.read_excel(Path(os.getcwd()) / "data" / "2066. Account Balance.xlsx")
print(account_balance1(transactions))