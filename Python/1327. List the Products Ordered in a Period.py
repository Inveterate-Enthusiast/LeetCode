# Table: Products
#
# +------------------+---------+
# | Column Name      | Type    |
# +------------------+---------+
# | product_id       | int     |
# | product_name     | varchar |
# | product_category | varchar |
# +------------------+---------+
# product_id is the primary key (column with unique values) for this table.
# This table contains data about the company's products.

# Table: Orders
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | product_id    | int     |
# | order_date    | date    |
# | unit          | int     |
# +---------------+---------+
# This table may have duplicate rows.
# product_id is a foreign key (reference column) to the Products table.
# unit is the number of products ordered in order_date.

# Write a solution to get the names of products that have at least 100 units ordered in February 2020 and their amount.
#
# Return the result table in any order.
import pandas as pd




def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    grouped = orders[
        (orders["order_date"].dt.strftime("%Y-%m") == '2020-02')
    ].groupby(by="product_id", as_index=False).agg(unit=("unit", "sum"))
    return pd.merge(
        left=grouped[grouped["unit"] >= 100],
        right=products,
        on="product_id",
        how="left",
    )[["product_name", "unit"]]





