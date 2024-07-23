# Table: Customer
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | customer_id | int     |
# | product_key | int     |
# +-------------+---------+
# This table may contain duplicates rows.
# customer_id is not NULL.
# product_key is a foreign key (reference column) to Product table.
#
#
# Table: Product
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | product_key | int     |
# +-------------+---------+
# product_key is the primary key (column with unique values) for this table.
#
#
# Write a solution to report the customer ids from the Customer table that bought all the products in the Product table.
#
# Return the result table in any order.
import pandas as pd
import os
from pathlib import Path

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    _set = set(product["product_key"])
    return customer.groupby(by="customer_id", as_index=False).agg(our_bool=("product_key", lambda x: _set.issubset(set(x)))).query("our_bool").loc[:, ["customer_id"]]

def find_customers1(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    _set = set(product["product_key"])
    grouped = customer.groupby(by="customer_id", as_index=True).apply(lambda x: set(x["product_key"]) >= _set, include_groups=False).reset_index()
    grouped.columns = ["customer_id", "bool"]
    return grouped.loc[grouped["bool"], ["customer_id"]]

path = Path(os.getcwd()) / "data" / "1045. Customers Who Bought All Products.xlsx"
customer = pd.read_excel(path, sheet_name="Customer")
product = pd.read_excel(path, sheet_name="Product")
print(find_customers1(customer, product))