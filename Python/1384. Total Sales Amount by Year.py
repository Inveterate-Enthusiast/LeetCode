# Table: Product
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | product_id    | int     |
# | product_name  | varchar |
# +---------------+---------+
# product_id is the primary key (column with unique values) for this table.
# product_name is the name of the product.
#
#
# Table: Sales
#
# +---------------------+---------+
# | Column Name         | Type    |
# +---------------------+---------+
# | product_id          | int     |
# | period_start        | date    |
# | period_end          | date    |
# | average_daily_sales | int     |
# +---------------------+---------+
# product_id is the primary key (column with unique values) for this table.
# period_start and period_end indicate the start and end date for the sales period, and both dates are inclusive.
# The average_daily_sales column holds the average daily sales amount of the items for the period.
# The dates of the sales years are between 2018 to 2020.
#
#
# Write a solution to report the total sales amount of each item for each year,
# with corresponding product_name, product_id, report_year, and total_amount.
#
# Return the result table ordered by product_id and report_year.
import pandas as pd
from pathlib import Path
import os

def year_to_dict(df: pd.DataFrame) -> dict:
    start_date, end_date = df["period_start"], df["period_end"]
    avg_sales = df["average_daily_sales"]
    year_dict = dict()

    if start_date.year == end_date.year:
        year_dict[str(start_date.year)] = ((end_date - start_date).days + 1) * avg_sales
    else:
        for year in range(start_date.year, end_date.year + 1, 1):
            if year == start_date.year:
                days = (pd.Timestamp(year=year, month=12, day=31) - start_date).days + 1
            elif year == end_date.year:
                days = (end_date - pd.Timestamp(year=year, month=1, day=1)).days + 1
            else:
                days = 366 if pd.Timestamp(year=year, month=1, day=1).is_leap_year else 365
            year_dict[str(year)] = days * avg_sales

    return year_dict

def total_sales(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    if sales.empty:
        return pd.DataFrame({
            "product_id": [],
            "product_name": [],
            "report_year": [],
            "total_amount": []
        })
    sales["dict_year"] = sales.apply(year_to_dict, axis=1)
    sales[["report_year", "total_amount"]] = sales["dict_year"].apply(lambda x: pd.Series(data=[list(x.keys()), list(x.values())]))
    exploded = sales[["product_id", "report_year", "total_amount"]].explode(["report_year", "total_amount"])
    merged = pd.merge(
        left=exploded,
        right=product,
        how="left",
        on="product_id"
    )
    return (merged[["product_id", "product_name", "report_year", "total_amount"]]
            .sort_values(by=["product_id", "report_year"], ascending=[True, True]))

path = Path(os.getcwd()) / "data" / "1384. Total Sales Amount by Year.xlsx"
product = pd.read_excel(path, sheet_name="Product")
sales = pd.read_excel(path, sheet_name="Sales")
print(total_sales(product, sales).to_string())