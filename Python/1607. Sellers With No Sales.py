# Table: Customer
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | customer_id   | int     |
# | customer_name | varchar |
# +---------------+---------+
# customer_id is the column with unique values for this table.
# Each row of this table contains the information of each customer in the WebStore.
#
#
# Table: Orders
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | order_id      | int     |
# | sale_date     | date    |
# | order_cost    | int     |
# | customer_id   | int     |
# | seller_id     | int     |
# +---------------+---------+
# order_id is the column with unique values for this table.
# Each row of this table contains all orders made in the webstore.
# sale_date is the date when the transaction was made between the customer (customer_id) and the seller (seller_id).
#
#
# Table: Seller
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | seller_id     | int     |
# | seller_name   | varchar |
# +---------------+---------+
# seller_id is the column with unique values for this table.
# Each row of this table contains the information of each seller.
#
#
# Write a solution to report the names of all sellers who did not make any sales in 2020.
#
# Return the result table ordered by seller_name in ascending order.
import pandas as pd

def sellers_with_no_sales(customer: pd.DataFrame, orders: pd.DataFrame, seller: pd.DataFrame) -> pd.DataFrame:
    grouped = orders.loc[orders["sale_date"].dt.year == 2020].groupby(by="seller_id", as_index=False).agg(amount=("order_cost", "sum"))
    return pd.merge(
        left=seller,
        right=grouped,
        how="left",
        on="seller_id"
    ).sort_values(by="seller_name", ascending=True).query("amount.isna()").loc[:, ["seller_name"]]

