# Table: sales
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | sale_id       | int     |
# | product_id    | int     |
# | sale_date     | date    |
# | quantity      | int     |
# | price         | decimal |
# +---------------+---------+
# sale_id is the unique identifier for this table.
# Each row contains information about a product sale including the product_id, date of sale, quantity sold, and price per unit.
# Table: products
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | product_id    | int     |
# | product_name  | varchar |
# | category      | varchar |
# +---------------+---------+
# product_id is the unique identifier for this table.
# Each row contains information about a product including its name and category.
# Write a solution to find the most popular product category for each season. The seasons are defined as:
#
# Winter: December, January, February
# Spring: March, April, May
# Summer: June, July, August
# Fall: September, October, November
# The popularity of a category is determined by the total quantity sold in that season. If there is a tie, select the category with the highest total revenue (quantity × price).
#
# Return the result table ordered by season in ascending order.

import pandas as pd

def seasonal_sales_analysis(products: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    seasons = pd.DataFrame({
        "Winter": [12, 1, 2],
        "Spring": [3, 4, 5],
        "Summer": [6, 7, 8],
        "Fall": [9, 10, 11]
    })
    seasons = seasons.melt(var_name="season", value_name="month")

    sales["month"] = pd.to_datetime(sales["sale_date"]).dt.month
    sales["revenue"] = sales["quantity"] * sales["price"]
    merged_sub = pd.merge(
        left=sales,
        right=seasons,
        how="left",
        on="month"
    )
    merged = pd.merge(
        left=merged_sub,
        right=products,
        how="left",
        on="product_id"
    )
    grouped = merged.groupby(by=["category", "season"], as_index=False).agg(total_revenue=("revenue", "sum"), total_quantity=("quantity", "sum"))
    grouped.sort_values(by=["total_quantity", "total_revenue"], ascending=[False, False], inplace=True)
    grouped["rank"] = grouped.groupby(by=["season"], as_index=False).cumcount() + 1
    return grouped.loc[grouped["rank"] == 1, ["season", "category", "total_quantity", "total_revenue"]].sort_values(by="season", ascending=True)