# Table: Orders
#
# +---------------+------+
# | Column Name   | Type |
# +---------------+------+
# | order_id      | int  |
# | product_id    | int  |
# | quantity      | int  |
# | purchase_date | date |
# +---------------+------+
# order_id contains unique values.
# Each row in this table contains the ID of an order, the id of the product purchased, the quantity, and the purchase date.
#
#
# Write a solution to report the IDs of all the products that were ordered three or more times in two consecutive years.
#
# Return the result table in any order.
import pandas as pd

def find_valid_products(orders: pd.DataFrame) -> pd.DataFrame:
    orders["year"] = pd.to_datetime(orders["purchase_date"]).dt.year
    grouped = orders.groupby(by=["product_id", "year"], as_index=False).agg(count=("order_id", "count"))
    grouped.sort_values(by=["product_id", "year"], ascending=[True, True], inplace=True)
    grouped["bool"] = grouped.groupby(by="product_id", as_index=False).apply(
        lambda x:
        (x["count"] >= 3) &
        (x["count"].shift(1) >= 3) &
        ((x["year"] - x["year"].shift(1)) == 1)).reset_index(drop=True)
    return grouped.loc[grouped["bool"], ["product_id"]].drop_duplicates()
