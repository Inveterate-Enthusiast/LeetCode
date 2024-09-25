# Table: Orders
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | order_id    | int  |
# | customer_id | int  |
# | order_type  | int  |
# +-------------+------+
# order_id is the column with unique values for this table.
# Each row of this table indicates the ID of an order, the ID of the customer who ordered it, and the order type.
# The orders could be of type 0 or type 1.
#
#
# Write a solution to report all the orders based on the following criteria:
#
# If a customer has at least one order of type 0, do not report any order of type 1 from that customer.
# Otherwise, report all the orders of the customer.
# Return the result table in any order.
import pandas as pd

def drop_specific_orders(orders: pd.DataFrame) -> pd.DataFrame:
    orders["min"] = orders.groupby(by="customer_id", as_index=False)["order_type"].transform("min")
    return orders.loc[((orders["min"] == 0) & (orders["order_type"] == 0))
                      |
                      (orders["min"] != 0)].drop(labels="min", axis=1)
