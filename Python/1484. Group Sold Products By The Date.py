# Table Activities:
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | sell_date   | date    |
# | product     | varchar |
# +-------------+---------+
# There is no primary key (column with unique values) for this table. It may contain duplicates.
# Each row of this table contains the product name and the date it was sold in a market.
#
# Write a solution to find for each date the number of different products sold and their names.
#
# The sold products names for each date should be sorted lexicographically.
#
# Return the result table ordered by sell_date.
import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    return activities.groupby(
        by="sell_date", as_index=False
    ).agg(
        num_sold=("product", "nunique"),
        products=("product",
                  lambda x: ",".join(sorted(x.unique(), reverse=False))))


