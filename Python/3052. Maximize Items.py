# Table: Inventory
#
# +----------------+---------+
# | Column Name    | Type    |
# +----------------+---------+
# | item_id        | int     |
# | item_type      | varchar |
# | item_category  | varchar |
# | square_footage | decimal |
# +----------------+---------+
# item_id is the column of unique values for this table.
# Each row includes item id, item type, item category and sqaure footage.
# Leetcode warehouse wants to maximize the number of items it can stock in a 500,000 square feet warehouse.
# It wants to stock as many prime items as possible, and afterwards use the remaining square footage to stock the most number of non-prime items.
#
# Write a solution to find the number of prime and non-prime items that can be stored in the 500,000 square feet warehouse.
# Output the item type with prime_eligible followed by not_prime and the maximum number of items that can be stocked.
#
# Note:
#
# Item count must be a whole number (integer).
# If the count for the not_prime category is 0, you should output 0 for that particular category.
# Return the result table ordered by item count in descending order.



import pandas as pd
import numpy as np
from pathlib import Path
import os


def maximize_items(inventory: pd.DataFrame) -> pd.DataFrame:
    _max = 500_000
    prime_items = inventory.loc[inventory["item_type"] == "prime_eligible"]
    not_prime_items = inventory.loc[inventory["item_type"] == "not_prime"]
    prime_foot, prime_unique = prime_items["square_footage"].sum(), prime_items["item_id"].nunique()
    not_prime_foot, not_prime_unique = not_prime_items["square_footage"].sum(), not_prime_items["item_id"].nunique()
    whole_prime_number = np.floor(_max / prime_foot)
    whole_not_prime_number = np.floor((_max - (whole_prime_number * prime_foot)) / not_prime_foot)
    return pd.DataFrame({
        "item_type": ["prime_eligible", "not_prime"],
        "item_count": [(whole_prime_number * prime_unique), (whole_not_prime_number * not_prime_unique)]
    }).sort_values(by="item_count", ascending=False)


def maximize_items1(inventory: pd.DataFrame) -> pd.DataFrame:
    _max = 500_000
    grouped = inventory.groupby(by="item_type", as_index=False).agg(foot=("square_footage", "sum"), nunique=("item_id", "nunique"))
    grouped["item_count"] = np.where(
        grouped["item_type"] == "prime_eligible",
        np.floor(_max / grouped["foot"]) * grouped["nunique"],
        np.floor((_max - (np.floor(_max / grouped.loc[grouped["item_type"] == "prime_eligible", "foot"].values) * grouped.loc[grouped["item_type"] == "prime_eligible", "foot"].values)) / grouped["foot"]) * grouped["nunique"]
    )
    return grouped[["item_type", "item_count"]].sort_values(by="item_count", ascending=False)

inventory = pd.read_excel(Path(os.getcwd()) / "data" / "3052. Maximize Items.xlsx")
print(maximize_items(inventory))
print(maximize_items1(inventory))