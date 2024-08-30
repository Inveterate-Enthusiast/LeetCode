# Table: Sales
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | sale_date     | date    |
# | fruit         | enum    |
# | sold_num      | int     |
# +---------------+---------+
# (sale_date, fruit) is the primary key (combination of columns with unique values) of this table.
# This table contains the sales of "apples" and "oranges" sold each day.
#
#
# Write a solution to report the difference between the number of apples and oranges sold each day.
#
# Return the result table ordered by sale_date.
import pandas as pd

def apples_oranges(sales: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(
        left=sales.loc[sales["fruit"] == "apples"],
        right=sales.loc[sales["fruit"] == "oranges"],
        how="outer",
        on="sale_date",
        suffixes=("_app", "_or")
    ).fillna(0)
    merged["diff"] = merged["sold_num_app"] - merged["sold_num_or"]
    return merged[["sale_date", "diff"]].sort_values(by="sale_date", ascending=True)

