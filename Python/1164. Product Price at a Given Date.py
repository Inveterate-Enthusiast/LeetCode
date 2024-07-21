# Table: Products
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | product_id    | int     |
# | new_price     | int     |
# | change_date   | date    |
# +---------------+---------+
# (product_id, change_date) is the primary key (combination of columns with unique values) of this table.
# Each row of this table indicates that the price of some product was changed to a new price at some date.
#
#
# Write a solution to find the prices of all products on 2019-08-16. Assume the price of all products before any change is 10.
#
# Return the result table in any order.
import pandas as pd
from typing import Optional
from datetime import datetime
from pathlib import Path
import os

def get_price(df: pd.DataFrame) -> Optional[int]:
    df = df.loc[df["change_date"] <= datetime(2019,8,16)]
    ans = (df.loc[df["change_date"].idxmax(), "new_price"]) if not df.empty else 10
    return ans

def price_at_given_date(products: pd.DataFrame) -> pd.DataFrame:
    return (products.groupby(by="product_id", as_index=False)
            .apply(get_price, include_groups=False)
            .rename(columns={None: "price"})
            .sort_values(by="product_id", ascending=True))

path = Path(os.getcwd()) / "data" / "1164. Product Price at a Given Date.xlsx"
products = pd.read_excel(path)
print(price_at_given_date(products))