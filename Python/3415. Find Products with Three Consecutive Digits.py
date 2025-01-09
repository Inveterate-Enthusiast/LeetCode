# Table: Products
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | product_id  | int     |
# | name        | varchar |
# +-------------+---------+
# product_id is the unique key for this table.
# Each row of this table contains the ID and name of a product.
# Write a solution to find all products whose names contain a sequence of exactly three digits in a row.
#
# Return the result table ordered by product_id in ascending order.

import pandas as pd
import re

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    pattern = r".*(?<!\d)\d{3}(?!\d).*"
    products["bool"] = products["name"].apply(lambda x: bool(re.match(pattern, str(x))))
    return products.loc[products["bool"]].sort_values(by="product_id", ascending=True).drop(labels="bool", axis=1)