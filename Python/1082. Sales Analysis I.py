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
# This table can have repeated rows.
# product_id is a foreign key (reference column) to the Product table.
# Each row of this table contains some information about one sale.

# Write a solution that reports the best seller by total sales price, If there is a tie, report them all.
#
# Return the result table in any order.
import pandas as pd
from pathlib import Path

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    grouped = sales.groupby(by="seller_id", as_index=False).agg(sum_of_sells=("price", "sum"))
    return grouped[grouped["sum_of_sells"] == grouped["sum_of_sells"].max()][["seller_id"]]

path = Path(__file__).parent / "data" / "1082. Sales Analysis I.xlsx"
product = pd.read_excel(path, sheet_name="Product")
sales = pd.read_excel(path, sheet_name="Sales")
print(sales_analysis(product, sales))
