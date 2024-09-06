# Table: Customers
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | customer_id   | int     |
# | name          | varchar |
# +---------------+---------+
# customer_id is the column with unique values for this table.
# This table contains information about the customers.
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
# | product_id    | int     |
# +---------------+---------+
# order_id is the column with unique values for this table.
# This table contains information about the orders made by customer_id.
# There will be no product ordered by the same user more than once in one day.
#
#
# Table: Products
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | product_id    | int     |
# | product_name  | varchar |
# | price         | int     |
# +---------------+---------+
# product_id is the column with unique values for this table.
# This table contains information about the Products.
#
#
# Write a solution to find the most recent order(s) of each product.
#
# Return the result table ordered by product_name in ascending order and in case of a tie by the product_id in ascending order.
# If there still a tie, order them by order_id in ascending order.
import pandas as pd

def most_recent_orders(customers: pd.DataFrame, orders: pd.DataFrame, products: pd.DataFrame) -> pd.DataFrame:
    orders["our_rank"] = orders.groupby(by="product_id", as_index=False)["order_date"].rank(method="min", ascending=False)
    return (pd.merge(
        left=orders.loc[orders["our_rank"] == 1],
        right=products,
        how="left",
        on="product_id"
    )
            .loc[:, ["product_name", "product_id", "order_id", "order_date"]]
            .sort_values(by=["product_name", "product_id", "order_id"], ascending=[True, True, True]))



