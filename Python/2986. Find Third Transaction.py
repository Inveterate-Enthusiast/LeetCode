# Table: Transactions
#
# +------------------+----------+
# | Column Name      | Type     |
# +------------------+----------+
# | user_id          | int      |
# | spend            | decimal  |
# | transaction_date | datetime |
# +------------------+----------+
# (user_id, transaction_date) is column of unique values for this table.
# This table contains user_id, spend, and transaction_date.
# Write a solution to find the third transaction (if they have at least three transactions) of every user,
# where the spending on the preceding two transactions is lower than the spending on the third transaction.
#
# Return the result table by user_id in ascending order.
import pandas as pd

def find_third_transaction(transactions: pd.DataFrame) -> pd.DataFrame:
    transactions.sort_values(by=["user_id", "transaction_date"], ascending=[True, True], inplace=True)
    transactions["rank"] = transactions.groupby(by="user_id", as_index=False)["transaction_date"].rank(method="dense", ascending=True)
    transactions["prev_1"] = transactions.groupby(by="user_id", as_index=False)["spend"].shift(1)
    transactions["prev_2"] = transactions.groupby(by="user_id", as_index=False)["spend"].shift(2)
    return (transactions.loc[
        (transactions["rank"] == 3)
        & (transactions["spend"] > transactions["prev_1"])
        & (transactions["spend"] > transactions["prev_2"])
    ]
            .drop(labels=["prev_1", "prev_2", "rank"], axis=1)
            .rename(columns={"spend": "third_transaction_spend", "transaction_date": "third_transaction_date"}))