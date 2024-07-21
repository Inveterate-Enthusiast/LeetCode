# Table: Customers
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | customer_id   | int     |
# | name          | varchar |
# | country       | varchar |
# +---------------+---------+
# customer_id is the column with unique values for this table.
# This table contains information about the customers in the company.
#
# Table: Product
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | product_id    | int     |
# | description   | varchar |
# | price         | int     |
# +---------------+---------+
# product_id is the column with unique values for this table.
# This table contains information on the products in the company.
# price is the product cost.
#
# Table: Orders
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | order_id      | int     |
# | customer_id   | int     |
# | product_id    | int     |
# | order_date    | date    |
# | quantity      | int     |
# +---------------+---------+
# order_id is the column with unique values for this table.
# This table contains information on customer orders.
# customer_id is the id of the customer who bought "quantity" products with id "product_id".
# Order_date is the date in format ('YYYY-MM-DD') when the order was shipped.
#
# Write a solution to report the customer_id and customer_name of customers who have spent at least $100 in each month of June and July 2020.
#
# Return the result table in any order.
import pandas as pd
import os
from pathlib import Path
from datetime import datetime

def find_customers(df: pd.DataFrame) -> bool:
    return ((df.loc[df["order_date"].dt.to_period("M") == pd.Period(datetime(2020,6,1), freq="M"),
            ["total_sum"]].sum() >= 100)
            &
            (df.loc[df["order_date"].dt.to_period("M") == pd.Period(datetime(2020,7,1), freq="M"),
            ["total_sum"]].sum() >= 100))


def customer_order_frequency(customers: pd.DataFrame, product: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(
        left=product.loc[:, ["product_id", "price"]],
        right=orders,
        how="right",
        on="product_id",
        copy=False
    )
    merged["total_sum"] = merged.apply(lambda x: x["price"] * x["quantity"], axis=1)
    grouped = merged.groupby(by="customer_id", as_index=False).apply(find_customers, include_groups=False)
    grouped.columns = ["customer_id", "bool"]

    return pd.merge(
        left=grouped.loc[grouped["bool"], ["customer_id"]],
        right=customers,
        how="left",
        on="customer_id"
    ).loc[:, ["customer_id", "name"]]


path = Path(os.getcwd()) / "data" / "1511. Customer Order Frequency.xlsx"
customers = pd.read_excel(path, sheet_name="Customers")
product = pd.read_excel(path, sheet_name="Product")
orders = pd.read_excel(path, sheet_name="Orders")
print(customer_order_frequency(customers, product, orders))