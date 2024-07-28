# Table: Transactions
#
# +----------------+---------+
# | Column Name    | Type    |
# +----------------+---------+
# | id             | int     |
# | country        | varchar |
# | state          | enum    |
# | amount         | int     |
# | trans_date     | date    |
# +----------------+---------+
# id is the column of unique values of this table.
# The table has information about incoming transactions.
# The state column is an ENUM (category) of type ["approved", "declined"].
# Table: Chargebacks
#
# +----------------+---------+
# | Column Name    | Type    |
# +----------------+---------+
# | trans_id       | int     |
# | trans_date     | date    |
# +----------------+---------+
# Chargebacks contains basic information regarding incoming chargebacks from some transactions placed in Transactions table.
# trans_id is a foreign key (reference column) to the id column of Transactions table.
# Each chargeback corresponds to a transaction made previously even if they were not approved.
#
#
# Write a solution to find for each month and country: the number of approved transactions and their total amount, the number of chargebacks, and their total amount.
#
# Note: In your solution, given the month and country, ignore rows with all zeros.
#
# Return the result table in any order.
import pandas as pd

def monthly_transactions(transactions: pd.DataFrame, chargebacks: pd.DataFrame) -> pd.DataFrame:
    transactions["month"] = transactions["trans_date"].dt.strftime("%Y-%m")
    chargebacks["month"] = chargebacks["trans_date"].dt.strftime("%Y-%m")
    grouped1 = transactions[transactions["state"] == "approved"].groupby(by=["month", "country"], as_index=False).agg(approved_count=("amount", "count"), approved_amount=("amount", "sum"))
    grouped2 = pd.merge(
        left=chargebacks,
        right=transactions[["id", "country", "amount"]],
        left_on="trans_id",
        right_on="id",
        how="left"
    ).groupby(by=["month", "country"], as_index=False).agg(chargeback_count=("amount", "count"), chargeback_amount=("amount", "sum"))
    return pd.merge(
        left=grouped1,
        right=grouped2,
        how="outer",
        on=["month", "country"]
    ).fillna(0)