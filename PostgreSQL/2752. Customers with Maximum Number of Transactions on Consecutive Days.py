# Table: Transactions
#
# +------------------+------+
# | Column Name      | Type |
# +------------------+------+
# | transaction_id   | int  |
# | customer_id      | int  |
# | transaction_date | date |
# | amount           | int  |
# +------------------+------+
# transaction_id is the column with unique values of this table.
# Each row contains information about transactions that includes unique (customer_id, transaction_date) along with the corresponding customer_id and amount.
# Write a solution to find all customer_id who made the maximum number of transactions on consecutive days.
#
# Return all customer_id with the maximum number of consecutive transactions. Order the result table by customer_id in ascending order.

import pandas as pd
import numpy as np

def find_customers(transactions: pd.DataFrame) -> pd.DataFrame:
    transactions.sort_values(by="transaction_date", ascending=True, inplace=True)
    transactions["prev_date"] = transactions.groupby(by="customer_id", as_index=False)["transaction_date"].shift(1)
    transactions["dif"] = np.where(transactions["prev_date"].isna(), 1, (transactions["transaction_date"] - transactions["prev_date"]).dt.days)
    transactions["bool"] = np.where(transactions["dif"] != 1, 1, 0)
    transactions["group"] = transactions.groupby(by="customer_id", as_index=False)["bool"].cumsum() + 1
    grouped = (transactions
               .groupby(by=["customer_id", "group"], as_index=False)
               .agg(total_number=("transaction_date", "nunique")))
    return (grouped
            .loc[grouped["total_number"] == grouped["total_number"].max(), ["customer_id"]]
            .sort_values(by="customer_id", ascending=True))