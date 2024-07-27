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
# Write a solution to find for each user whether the brand of the second item (by date) they sold is their favorite brand.
# If a user sold less than two items, report the answer for that user as no.
# It is guaranteed that no seller sells more than one item in a day.
#
# Return the result table in any order.
import pandas as pd
import numpy as np

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    orders["our_rank"] = orders.groupby(by="seller_id", as_index=False)["order_date"].rank(method="dense", ascending=True)
    ranked_orders = orders.loc[(orders["our_rank"] == 1) | (orders["our_rank"] == 2), ["seller_id", "our_rank", "item_id"]]
    indices = ranked_orders.groupby(by="seller_id")["our_rank"].idxmax()
    ranked_orders = ranked_orders.loc[indices]
    merged = pd.merge(
        left=users.loc[:,["user_id", "favorite_brand"]].rename(columns={"user_id": "seller_id"}),
        right=(pd.merge(
            left=ranked_orders,
            right=items,
            on="item_id",
            how="left"
        )),
        on="seller_id",
        how="left"
    )
    merged["2nd_item_fav_brand"] = np.where(merged["our_rank"] == 1, "no", np.where(merged["favorite_brand"] == merged["item_brand"], "yes", "no"))
    return merged.loc[:, ["seller_id", "2nd_item_fav_brand"]]


