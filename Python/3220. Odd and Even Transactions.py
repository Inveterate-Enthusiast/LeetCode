# Table: transactions
#
# +------------------+------+
# | Column Name      | Type |
# +------------------+------+
# | transaction_id   | int  |
# | amount           | int  |
# | transaction_date | date |
# +------------------+------+
# The transactions_id column uniquely identifies each row in this table.
# Each row of this table contains the transaction id, amount and transaction date.
# Write a solution to find the sum of amounts for odd and even transactions for each day.
# If there are no odd or even transactions for a specific date, display as 0.
#
# Return the result table ordered by transaction_date in ascending order.

import pandas as pd
import numpy as np

def sum_daily_odd_even(transactions: pd.DataFrame) -> pd.DataFrame:
    transactions["bool"] = transactions["amount"]%2 == 0
    transactions["odd"] = np.where(~transactions["bool"], transactions["amount"], 0)
    transactions["even"] = np.where(transactions["bool"], transactions["amount"], 0)
    grouped = transactions.groupby(by="transaction_date", as_index=False).agg(odd_sum=("odd", "sum"), even_sum=("even", "sum"))
    return grouped.sort_values(by="transaction_date", ascending=True)
