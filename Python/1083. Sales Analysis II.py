# Table: Product
#
# +--------------+---------+
# | Column Name  | Type    |
# +--------------+---------+
# | product_id   | int     |
# | product_name | varchar |
# | unit_price   | int     |
# +--------------+---------+
# product_id is the primary key (column with unique values) of this table.
# Each row of this table indicates the name and the price of each product.

# Table: Sales
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | seller_id   | int     |
# | product_id  | int     |
# | buyer_id    | int     |
# | sale_date   | date    |
# | quantity    | int     |
# | price       | int     |
# +-------------+---------+
# This table might have repeated rows.
# product_id is a foreign key (reference column) to the Product table.
# buyer_id is never NULL.
# sale_date is never NULL.
# Each row of this table contains some information about one sale.

# Write a solution to report the buyers who have bought S8 but not iPhone. Note that S8 and iPhone are products presented in the Product table.
#
# Return the result table in any order.
import pandas as pd
from pathlib import Path

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(
        left = sales,
        right = product,
        on = "product_id",
        how = "left",
        suffixes=("_sal", "_pro"),
        copy=False
    )[["product_name", "buyer_id"]]

    _set = lambda x: set(x)
    grouped = merged.groupby(by="buyer_id", as_index=False).agg(our_set=("product_name", _set))
    return grouped[
        grouped["our_set"].apply(lambda x: "S8" in x and "iPhone" not in x)
    ][["buyer_id"]]

def sales_analysis1(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(
        left = sales,
        right = product,
        on = "product_id",
        how = "left",
        suffixes = ("_sal", "pro"),
        copy = False
    )

    S8_buyer = merged[merged["product_name"] == "S8"][["buyer_id"]].drop_duplicates()
    iPhone_buyer = merged[merged["product_name"] == "iPhone"][["buyer_id"]].drop_duplicates()
    return S8_buyer[~S8_buyer["buyer_id"].isin(iPhone_buyer["buyer_id"])]

path = Path(__file__).parent / "data" / "1082. Sales Analysis II.xlsx"
product = pd.read_excel(path, sheet_name="Product")
sales = pd.read_excel(path, sheet_name="Sales")
print(sales_analysis1(product, sales))