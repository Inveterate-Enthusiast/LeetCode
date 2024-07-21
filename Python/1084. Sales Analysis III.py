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
# This table can have duplicate rows.
# product_id is a foreign key (reference column) to the Product table.
# Each row of this table contains some information about one sale.

# Write a solution to report the products that were only sold in the first quarter of 2019. That is, between 2019-01-01 and 2019-03-31 inclusive.
#
# Return the result table in any order.
import pandas as pd
from pathlib import Path
from datetime import datetime

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(
        left=sales,
        right=product,
        on="product_id",
        how="left",
        copy=False,
        suffixes=("_sal","_prod")
    )

    first_quarter = merged[merged["sale_date"].between(
        left=datetime(2019,1,1),
        right=datetime(2019,3,31),
        inclusive="both"
    )][["product_id", "product_name"]].drop_duplicates()

    other_quarter = merged[~merged["sale_date"].between(
        left=datetime(2019,1,1),
        right=datetime(2019,3,31),
        inclusive="both"
    )][["product_id", "product_name"]].drop_duplicates()

    return first_quarter[~first_quarter["product_id"].isin(other_quarter["product_id"])]

def sales_analysis1(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    grouped = sales.groupby(by="product_id", as_index=False).agg(
        min=("sale_date", "min"),
        max=("sale_date", "max")
    )

    grouped = grouped[
        (grouped["min"] >= datetime(2019, 1, 1)) &
        (grouped["max"] <= datetime(2019, 3, 31))
    ]
    return pd.merge(
        left=grouped,
        right=product,
        how="left",
        on="product_id"
    )[["product_id", "product_name"]]


path = Path(__file__).parent / "data" / "1082. Sales Analysis III.xlsx"
product = pd.read_excel(path, sheet_name="Product")
sales = pd.read_excel(path, sheet_name="Sales")
# sales['sale_date'] = pd.to_datetime(sales['sale_date'], format='%d.%m.%Y')

print(sales_analysis1(product, sales))