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
# delivery_id is the column of unique values of this table.
# The table holds information about food delivery to customers that make orders at some date and specify a preferred delivery date (on the same order date or after it).
#
#
# If the customer's preferred delivery date is the same as the order date, then the order is called immediate; otherwise, it is called scheduled.
#
# The first order of a customer is the order with the earliest order date that the customer made. It is guaranteed that a customer has precisely one first order.
#
# Write a solution to find the percentage of immediate orders in the first orders of all customers, rounded to 2 decimal places.
import pandas as pd

def immediate_food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    delivery["our_rank"] = delivery.groupby(by="customer_id", as_index=False)["order_date"].rank(method="dense", ascending=True)
    ranked = delivery.loc[delivery["our_rank"] == 1]
    return pd.DataFrame({
        "immediate_percentage": [round(
            (
                (ranked[ranked["order_date"] == ranked["customer_pref_delivery_date"]].shape[0])
                / (ranked["delivery_id"].shape[0]))
                * 100
                + 1e-9,
            2)]
    })