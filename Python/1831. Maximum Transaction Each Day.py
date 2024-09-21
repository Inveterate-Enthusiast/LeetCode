# Table: Transactions
#
# +----------------+----------+
# | Column Name    | Type     |
# +----------------+----------+
# | transaction_id | int      |
# | day            | datetime |
# | amount         | int      |
# +----------------+----------+
# transaction_id is the column with unique values for this table.
# Each row contains information about one transaction.
#
#
# Write a solution to report the IDs of the transactions with the maximum amount on their respective day.
# If in one day there are multiple such transactions, return all of them.
#
# Return the result table ordered by transaction_id in ascending order.
import pandas as pd

def find_maximum_transaction(transactions: pd.DataFrame) -> pd.DataFrame:
    transactions["date"] = pd.to_datetime(transactions["day"]).dt.strftime("%Y-%m-%d")
    transactions["our_rank"] = transactions.groupby(by="date", as_index=False)["amount"].rank(method="min", ascending=False)
    return transactions.loc[transactions["our_rank"] == 1, ["transaction_id"]].sort_values(by="transaction_id", ascending=True)
