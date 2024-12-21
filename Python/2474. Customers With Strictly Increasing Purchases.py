# Table: Orders
#
# +--------------+------+
# | Column Name  | Type |
# +--------------+------+
# | order_id     | int  |
# | customer_id  | int  |
# | order_date   | date |
# | price        | int  |
# +--------------+------+
# order_id is the column with unique values for this table.
# Each row contains the id of an order, the id of customer that ordered it, the date of the order, and its price.
#
#
# Write a solution to report the IDs of the customers with the total purchases strictly increasing yearly.
#
# The total purchases of a customer in one year is the sum of the prices of their orders in that year.
# If for some year the customer did not make any order, we consider the total purchases 0.
# The first year to consider for each customer is the year of their first order.
# The last year to consider for each customer is the year of their last order.
# Return the result table in any order.

import pandas as pd
import numpy as np

def find_specific_customers(orders: pd.DataFrame) -> pd.DataFrame:
    orders["year"] = pd.to_datetime(arg=orders["order_date"]).dt.year
    grouped = orders.groupby(by=["customer_id", "year"], as_index=False).agg(price=("price", "sum")).sort_values(by="year", ascending=True)
    grouped["prev_year"] = grouped.groupby(by="customer_id", as_index=False)["year"].shift(1)
    grouped["prev_price"] = grouped.groupby(by="customer_id", as_index=False)["price"].shift(1)
    grouped["bool"] = np.where(
        ((~grouped["prev_year"].isna()) & ((grouped["year"] - grouped["prev_year"]) != 1))
        |
        ((~grouped["prev_price"].isna()) & (grouped["price"] <= grouped["prev_price"])),
        1, 0
    )
    result = grouped.groupby(by="customer_id", as_index=False).agg(bool=("bool", "sum"))
    return result.loc[result["bool"]==0, ["customer_id"]]