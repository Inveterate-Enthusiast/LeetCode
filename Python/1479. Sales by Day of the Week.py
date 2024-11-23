# Table: Orders
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | order_id      | int     |
# | customer_id   | int     |
# | order_date    | date    |
# | item_id       | varchar |
# | quantity      | int     |
# +---------------+---------+
# (ordered_id, item_id) is the primary key (combination of columns with unique values) for this table.
# This table contains information on the orders placed.
# order_date is the date item_id was ordered by the customer with id customer_id.
#
#
# Table: Items
#
# +---------------------+---------+
# | Column Name         | Type    |
# +---------------------+---------+
# | item_id             | varchar |
# | item_name           | varchar |
# | item_category       | varchar |
# +---------------------+---------+
# item_id is the primary key (column with unique values) for this table.
# item_name is the name of the item.
# item_category is the category of the item.
#
#
# You are the business owner and would like to obtain a sales report for category items and the day of the week.
#
# Write a solution to report how many units in each category have been ordered on each day of the week.
#
# Return the result table ordered by category.

import pandas as pd

def sales_by_day(orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    week_days = pd.DataFrame({
        "day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
        "num": [1, 2, 3, 4, 5, 6, 7]
    })
    crossed = pd.merge(
        left=week_days,
        right=items[["item_category"]].drop_duplicates(keep="first"),
        how="cross"
    )
    orders["day"] = orders["order_date"].dt.day_name()
    merged = pd.merge(
        left=orders,
        right=items,
        how="left",
        on="item_id"
    )
    grouped = merged.groupby(by=["item_category", "day"], as_index=False).agg(values=("quantity", "sum"))
    merged_2 = pd.merge(
        left=crossed,
        right=grouped,
        how="left",
        on=["day", "item_category"]
    ).rename(columns={"item_category": "Category"})
    pivot = merged_2.pivot_table(values="values", index="Category", columns="day", fill_value=0, dropna=False)
    pivot = pivot[week_days["day"].tolist()]
    return pivot.reset_index().sort_values(by="Category", ascending=True)