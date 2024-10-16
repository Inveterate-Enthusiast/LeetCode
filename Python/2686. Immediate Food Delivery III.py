# Table: Delivery
#
# +-----------------------------+---------+
# | Column Name                 | Type    |
# +-----------------------------+---------+
# | delivery_id                 | int     |
# | customer_id                 | int     |
# | order_date                  | date    |
# | customer_pref_delivery_date | date    |
# +-----------------------------+---------+
# delivery_id is the column with unique values of this table.
# Each row contains information about food delivery to a customer that makes an order
# at some date and specifies a preferred delivery date (on the order date or after it).
# If the customer's preferred delivery date is the same as the order date, then the order is called immediate,
# otherwise, it is scheduled.
#
# Write a solution to find the percentage of immediate orders on each unique order_date, rounded to 2 decimal places.
#
# Return the result table ordered by order_date in ascending order.
import pandas as pd

def immediate_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    delivery["bool"] = delivery["order_date"] == delivery["customer_pref_delivery_date"]
    grouped = delivery.groupby(by="order_date", as_index=False).agg(
        immediate=("bool", "sum"),
        all=("delivery_id", "count")
    )
    grouped["immediate_percentage"] = (grouped["immediate"] / grouped["all"] * 100 + 1e-9).round(2)
    return grouped[["order_date", "immediate_percentage"]].sort_values(by="order_date", ascending=True)