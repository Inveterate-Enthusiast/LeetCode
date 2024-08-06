# Table: Store
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | bill_id     | int  |
# | customer_id | int  |
# | amount      | int  |
# +-------------+------+
# bill_id is the primary key (column with unique values) for this table.
# Each row contains information about the amount of one bill and the customer associated with it.
#
#
# Write a solution to report the number of customers who had at least one bill with an amount strictly greater than 500.
import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({
        "rich_count": [store.loc[store["amount"] > 500, "customer_id"].nunique()]
    })
