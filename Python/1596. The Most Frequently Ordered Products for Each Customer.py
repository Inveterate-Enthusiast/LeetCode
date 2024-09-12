# Table: Customers
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | customer_id   | int     |
# | name          | varchar |
# +---------------+---------+
# customer_id is the column with unique values for this table.
# This table contains information about the customers.
#
#
# Table: Orders
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | order_id      | int     |
# | order_date    | date    |
# | customer_id   | int     |
# | product_id    | int     |
# +---------------+---------+
# order_id is the column with unique values for this table.
# This table contains information about the orders made by customer_id.
# No customer will order the same product more than once in a single day.
#
#
# Table: Products
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | product_id    | int     |
# | product_name  | varchar |
# | price         | int     |
# +---------------+---------+
# product_id is the column with unique values for this table.
# This table contains information about the products.
#
#
# Write a solution to find the most frequently ordered product(s) for each customer.
#
# The result table should have the product_id and product_name for each customer_id who ordered at least one order.
#
# Return the result table in any order.
import pandas as pd

def most_frequently_products(customers: pd.DataFrame, orders: pd.DataFrame, products: pd.DataFrame) -> pd.DataFrame:
    grouped = orders.groupby(by=["customer_id", "product_id"], as_index=False).agg(count=("product_id", "count"))
    grouped["our_rank"] = grouped.groupby(by="customer_id", as_index=False)["count"].rank(method="min", ascending=False)
    grouped = grouped.loc[grouped["our_rank"] == 1, ["customer_id", "product_id"]]
    return pd.merge(
        left=grouped,
        right=products[["product_id", "product_name"]],
        how="left",
        on="product_id"
    )