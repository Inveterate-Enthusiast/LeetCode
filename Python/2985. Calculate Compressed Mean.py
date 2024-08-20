# Table: Orders
#
# +-------------------+------+
# | Column Name       | Type |
# +-------------------+------+
# | order_id          | int  |
# | item_count        | int  |
# | order_occurrences | int  |
# +-------------------+------+
# order_id is column of unique values for this table.
# This table contains order_id, item_count, and order_occurrences.
# Write a solution to calculate the average number of items per order, rounded to 2 decimal places.
#
# Return the result table in any order.
import pandas as pd

def compressed_mean(orders: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({
        "average_items_per_order": [round(((orders["item_count"] * orders["order_occurrences"]).sum() / (orders["order_occurrences"]).sum()) + 1e-9, 2)]
    })

