# Table: Products
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | product_id  | int     |
# | store       | varchar |
# | price       | int     |
# +-------------+---------+
# (product_id, store) is the primary key (combination of columns with unique values) for this table.
# Each row of this table indicates the price of product_id in store.
# There will be at most 30 different stores in the table.
# price is the price of the product at this store.
#
#
# Important note: This problem targets those who have a good experience with SQL.
# If you are a beginner, we recommend that you skip it for now.
#
# Implement the procedure PivotProducts to reorganize the Products table
# so that each row has the id of one product and its price in each store.
# The price should be null if the product is not sold in a store.
# The columns of the table should contain each store and they should be sorted in lexicographical order.
#
# The procedure should return the table after reorganizing it.
#
# Return the result table in any order.





import pandas as pd
from pathlib import Path
import os

def dynamic_pivoting_table(products: pd.DataFrame) -> pd.DataFrame:
    stores = sorted(list(set(products["store"].values.tolist())))
    pivot = products.pivot_table(columns="store", index="product_id", values="price")
    pivot = pivot[stores]
    return pivot.reset_index()

products = pd.read_excel(Path(os.getcwd()) / "data"/ "2252. Dynamic Pivoting of a Table.xlsx", sheet_name="Products")
print(dynamic_pivoting_table(products))