# Table: Products
#
# +------------+---------+
# | Column Name| Type    |
# +------------+---------+
# | product_id | int     |
# | category   | varchar |
# | price      | decimal |
# +------------+---------+
# product_id is the unique key for this table.
# Each row includes the product's ID, its category, and its price.
# Table: Discounts
#
# +------------+---------+
# | Column Name| Type    |
# +------------+---------+
# | category   | varchar |
# | discount   | int     |
# +------------+---------+
# category is the primary key for this table.
# Each row contains a product category and the percentage discount applied to that category (values range from 0 to 100).
# Write a solution to find the final price of each product after applying the category discount.
# If a product's category has no associated discount, its price remains unchanged.
#
# Return the result table ordered by product_id in ascending order.
import pandas as pd

def calculate_final_prices(products: pd.DataFrame, discounts: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(
        left=products,
        right=discounts,
        how="left",
        on="category"
    ).fillna(0)
    merged["final_price"] = merged["price"] - (merged["price"] * merged["discount"] / 100)
    return merged[["product_id", "final_price", "category"]].sort_values(by="product_id", ascending=True)
