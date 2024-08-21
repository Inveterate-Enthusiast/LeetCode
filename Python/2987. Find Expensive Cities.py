# Table: Listings
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | listing_id  | int     |
# | city        | varchar |
# | price       | int     |
# +-------------+---------+
# listing_id is column of unique values for this table.
# This table contains listing_id, city, and price.
# Write a solution to find cities where the average home prices exceed the national average home price.
#
# Return the result table sorted by city in ascending order.
import pandas as pd

def find_expensive_cities(listings: pd.DataFrame) -> pd.DataFrame:
    avg = listings["price"].mean()
    grouped = (listings
                .groupby(by="city", as_index=False)
                .agg(price=("price", "mean")))
    return grouped.loc[
        grouped["price"] > avg,
        ["city"]
    ].sort_values(by="city", ascending=True)

