# Table: Warehouse
#
# +--------------+---------+
# | Column Name  | Type    |
# +--------------+---------+
# | name         | varchar |
# | product_id   | int     |
# | units        | int     |
# +--------------+---------+
# (name, product_id) is the primary key (combination of columns with unique values) for this table.
# Each row of this table contains the information of the products in each warehouse.
#
#
# Table: Products
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | product_id    | int     |
# | product_name  | varchar |
# | Width         | int     |
# | Length        | int     |
# | Height        | int     |
# +---------------+---------+
# product_id is the primary key (column with unique values) for this table.
# Each row of this table contains information about the product dimensions (Width, Lenght, and Height) in feets of each product.
#
#
# Write a solution to report the number of cubic feet of volume the inventory occupies in each warehouse.
#
# Return the result table in any order.
import pandas as pd
import math

def warehouse_manager(warehouse: pd.DataFrame, products: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(
        left=warehouse,
        right=products,
        on="product_id",
        how="inner"
    )
    merged["volume"] = merged.apply(lambda x: math.prod([x["Width"], x["Length"], x["Height"], x["units"]]), axis=1)
    return merged.groupby(by="name", as_index=False).agg(volume=("volume", "sum")).rename(columns={"name": "warehouse_name"})

