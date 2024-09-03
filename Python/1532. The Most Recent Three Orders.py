# Table: Customers
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | customer_id   | int     |
# | name          | varchar |
# +---------------+---------+
# customer_id is the column with unique values for this table.
# This table contains information about customers.
#
#
# Table: Orders
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | order_id      | int     |
# | order_date    | date    |
# | customer_id   | int     |
# | cost          | int     |
# +---------------+---------+
# order_id is the column with unique values for this table.
# This table contains information about the orders made by customer_id.
# Each customer has one order per day.
#
#
# Write a solution to find the most recent three orders of each user.
# If a user ordered less than three orders, return all of their orders.
#
# Return the result table ordered by customer_name in ascending order
# and in case of a tie by the customer_id in ascending order. If there is still a tie, order them by order_date in descending order.
import pandas as pd

def recent_three_orders(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    orders["our_rank"] = orders.groupby(by="customer_id", as_index=False)["order_date"].rank(method="dense", ascending=False)
    return (pd.merge(
        right=orders.loc[orders["our_rank"] <= 3, ["customer_id", "order_id", "order_date"]],
        left=customers.rename(columns={"name": "customer_name"}),
        how="right",
        on="customer_id"
    )[["customer_name", "customer_id", "order_id", "order_date"]]
            .sort_values(by=["customer_name", "customer_id", "order_date"], ascending=[True, True, False]))

