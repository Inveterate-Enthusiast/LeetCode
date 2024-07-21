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
# delivery_id is the primary key (column with unique values) of this table.
# The table holds information about food delivery to customers that make orders at some date and specify a preferred delivery date (on the same order date or after it).

# If the customer's preferred delivery date is the same as the order date, then the order is called immediate; otherwise, it is called scheduled.
#
# Write a solution to find the percentage of immediate orders in the table, rounded to 2 decimal places.
import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    immediate_orders = delivery[delivery["order_date"] == delivery["customer_pref_delivery_date"]]["delivery_id"].nunique()
    all_orders = delivery["delivery_id"].nunique()
    ans = immediate_orders / all_orders

    return pd.DataFrame({
        "immediate_percentage": [round((ans*100), 2) if not pd.isna(ans) else 0]
    })

