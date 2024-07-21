# Table: Sales
#
# +-------------+-------+
# | Column Name | Type  |
# +-------------+-------+
# | sale_id     | int   |
# | product_id  | int   |
# | year        | int   |
# | quantity    | int   |
# | price       | int   |
# +-------------+-------+
# (sale_id, year) is the primary key (combination of columns with unique values) of this table.
# product_id is a foreign key (reference column) to Product table.
# Each row of this table shows a sale on the product product_id in a certain year.
# Note that the price is per unit.

# Table: Product
#
# +--------------+---------+
# | Column Name  | Type    |
# +--------------+---------+
# | product_id   | int     |
# | product_name | varchar |
# +--------------+---------+
# product_id is the primary key (column with unique values) of this table.
# Each row of this table indicates the product name of each product.

# Write a solution that reports the total quantity sold for every product id.
#
# Return the resulting table in any order.
import pandas as pd
from pathlib import Path

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    grouped = sales.groupby(by="product_id", as_index=False).agg(total_quantity=("quantity", "sum"))
    return grouped[["product_id", "total_quantity"]]

def sales_analysis1(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
   return sales.groupby(by="product_id", as_index=False).agg(total_quantity=("quantity", "sum"))[["product_id", "total_quantity"]]

path = Path(__file__).parent / "data" / "1068. Product Sales Analysis I.xlsx"
sales = pd.read_excel(path, sheet_name="Sales")
product = pd.read_excel(path, sheet_name="Product")
print(sales_analysis1(sales, product))
