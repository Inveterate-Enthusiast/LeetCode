# Table: Orders
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | order_id      | int     |
# | order_date    | date    |
# | customer_id   | int     |
# | invoice       | int     |
# +---------------+---------+
# order_id is the column with unique values for this table.
# This table contains information about the orders made by customer_id.
#
#
# Write a solution to find the number of unique orders and the number of unique customers with invoices > $20 for each different month.
#
# Return the result table sorted in any order.
import pandas as pd
import os
from pathlib import Path


def grouping(df: pd.DataFrame) -> pd.Series:
    our_set1 = set(df.groupby(by="customer_id", as_index=False).agg(total=("invoice", "sum")).query("total > 20")["customer_id"])
    our_set2 = set(df.groupby(by="order_id", as_index=False).agg(total=("invoice", "sum")).query("total > 20")["order_id"])
    return pd.Series(
        data=[len(our_set1),
              len(our_set2)],
        index=["order_count", "customer_count"]
    )


def unique_orders_and_customers(orders: pd.DataFrame) -> pd.DataFrame:
    orders["order_date"] = orders["order_date"].dt.strftime("%Y-%m")
    return (orders
            .groupby(by="order_date", as_index=True)
            .apply(grouping, include_groups=False)
            .reset_index()
            .rename(columns={"order_date": "month"})
            .query("order_count != 0 and customer_count != 0")
            .loc[:, ["month", "order_count", "customer_count"]])


def unique_orders_and_customers1(orders: pd.DataFrame) -> pd.DataFrame:
    orders["month"] = orders["order_date"].dt.strftime("%Y-%m")
    return (orders
            .loc[orders["invoice"] > 20]
            .groupby(by="month", as_index=False)
            .agg(order_count=("order_id", "nunique"),
                 customer_count=("customer_id", "nunique")))



path = Path(os.getcwd()) / "data" / "1565. Unique Orders and Customers Per Month.xlsx"
orders = pd.read_excel(path)
print(unique_orders_and_customers1(orders))