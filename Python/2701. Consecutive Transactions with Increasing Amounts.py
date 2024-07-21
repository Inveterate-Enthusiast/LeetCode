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
# transaction_id is the primary key of this table.
# Each row contains information about transactions that includes unique (customer_id, transaction_date) along with the corresponding customer_id and amount.
# Write an SQL query to find the customers who have made consecutive transactions with increasing amount for at least three consecutive days. Include the customer_id, start date of the consecutive transactions period and the end date of the consecutive transactions period. There can be multiple consecutive transactions by a customer.
#
# Return the result table ordered by customer_id in ascending order.
import pandas as pd
import os
from pathlib import Path


def filter(df: pd.DataFrame, len_of_seq: int) -> pd.DataFrame:
    df["periodId"] = pd.Series(dtype="int")
    prevIndex = periodId = None
    for index, row in df.iterrows():
        if prevIndex is None or row["customer_id"] != df.loc[prevIndex, "customer_id"]:
            periodId = 1
        elif (row["transaction_date"] - pd.Timedelta(value=1, unit="day")) != df.loc[prevIndex, "transaction_date"]\
                or row["amount"] <= df.loc[prevIndex, "amount"]:
            periodId += 1

        df.loc[index, "periodId"] = periodId
        prevIndex = index

    df = df.loc[
        (df["transaction_date"].shift(1) == (df["transaction_date"] - pd.Timedelta(value=1, unit="day")))
        |
        (df["transaction_date"].shift(-1) == (df["transaction_date"] + pd.Timedelta(value=1, unit="day")))
    ]


    return (df.
            groupby(by="customer_id", as_index=True).
            apply(lambda x: x[x["periodId"].map(x["periodId"].value_counts()) >= len_of_seq][["transaction_date", "periodId"]], include_groups=False).
            reset_index())

def consecutive_increasing_transactions2(transactions: pd.DataFrame) -> pd.DataFrame:
    transactions.sort_values(by=["customer_id", "transaction_date"], ascending=[True, True], inplace=True)
    transactions = filter(transactions, 3)
    return (transactions
    .groupby(by=["customer_id", "periodId"], as_index=False)
    .agg(
        consecutive_start=("transaction_date", "min"),
        consecutive_end=("transaction_date", "max")).drop(columns="periodId")
    .sort_values(by="customer_id", ascending=True))






path = Path(os.getcwd()) / "data" / "2701. Consecutive Transactions with Increasing Amounts.xlsx"
transactions = pd.read_excel(path)
print(consecutive_increasing_transactions2(transactions))
