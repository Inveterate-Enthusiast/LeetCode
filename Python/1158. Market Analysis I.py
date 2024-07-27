# Table: Users
#
# +----------------+---------+
# | Column Name    | Type    |
# +----------------+---------+
# | user_id        | int     |
# | join_date      | date    |
# | favorite_brand | varchar |
# +----------------+---------+
# user_id is the primary key (column with unique values) of this table.
# This table has the info of the users of an online shopping website where users can sell and buy items.
#
#
# Table: Orders
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | order_id      | int     |
# | order_date    | date    |
# | item_id       | int     |
# | buyer_id      | int     |
# | seller_id     | int     |
# +---------------+---------+
# order_id is the primary key (column with unique values) of this table.
# item_id is a foreign key (reference column) to the Items table.
# buyer_id and seller_id are foreign keys to the Users table.
#
#
# Table: Items
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | item_id       | int     |
# | item_brand    | varchar |
# +---------------+---------+
# item_id is the primary key (column with unique values) of this table.
#
#
# Write a solution to find for each user, the join date and the number of orders they made as a buyer in 2019.
#
# Return the result table in any order.
import pandas as pd

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    grouped = (orders
               .loc[orders["order_date"].dt.to_period("Y") == pd.Period(value=2019, freq="Y")]
               .groupby(by="buyer_id", as_index=False)
               .agg(orders_in_2019=("order_id", "nunique")))
    return pd.merge(
        left=users[["user_id", "join_date"]].rename(columns={"user_id": "buyer_id"}),
        right=grouped,
        how="left",
        on="buyer_id"
    ).fillna(0)
