# Table: Products
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | product_id  | int     |
# | store_name1 | int     |
# | store_name2 | int     |
# |      :      | int     |
# |      :      | int     |
# |      :      | int     |
# | store_namen | int     |
# +-------------+---------+
# product_id is the primary key for this table.
# Each row in this table indicates the product's price in n different stores.
# If the product is not available in a store, the price will be null in that store's column.
# The names of the stores may change from one testcase to another. There will be at least 1 store and at most 30 stores.
#
#
# Important note: This problem targets those who have a good experience with SQL. If you are a beginner, we recommend that you skip it for now.
#
# Implement the procedure UnpivotProducts to reorganize the Products table so that each row has the id of one product,
# the name of a store where it is sold, and its price in that store. If a product is not available in a store,
# do not include a row with that product_id and store combination in the result table.
# There should be three columns: product_id, store, and price.
#
# The procedure should return the table after reorganizing it.
#
# Return the result table in any order.


import pandas as pd

def find_valid_users(products: pd.DataFrame) -> pd.DataFrame:
    return products.melt(id_vars="product_id", var_name="store", value_name="price").dropna()