# Table: Sales
#
# +--------------+---------+
# | Column Name  | Type    |
# +--------------+---------+
# | sale_id      | int     |
# | product_name | varchar |
# | sale_date    | date    |
# +--------------+---------+
# sale_id is the column with unique values for this table.
# Each row of this table contains the product name and the date it was sold.
#
#
# Since table Sales was filled manually in the year 2000, product_name may contain leading and/or trailing white spaces, also they are case-insensitive.
#
# Write a solution to report
#
# product_name in lowercase without leading or trailing white spaces.
# sale_date in the format ('YYYY-MM').
# total the number of times the product was sold in this month.
# Return the result table ordered by product_name in ascending order. In case of a tie, order it by sale_date in ascending order.
import pandas as pd
import os
from pathlib import Path


def grouping(df: pd.DataFrame) -> pd.DataFrame:
    return (df
            .groupby(by="sale_date", as_index=False)
            .agg(total=("sale_id", "count")))


def fix_name_format(sales: pd.DataFrame) -> pd.DataFrame:
    sales["sale_date"] = sales["sale_date"].dt.strftime("%Y-%m")
    sales["product_name"] = sales["product_name"].astype(str).str.lower().str.strip()
    return (sales
            .groupby(by="product_name", as_index=True)
            .apply(grouping, include_groups=False)
            .reset_index()
            .sort_values(by=["product_name", "sale_date"], ascending=[True, True])
            .loc[:, ["product_name", "sale_date", "total"]])

path = Path(os.getcwd()) / "data" / "1543. Fix Product Name Format.xlsx"
sales = pd.read_excel(path)
print(fix_name_format(sales))
