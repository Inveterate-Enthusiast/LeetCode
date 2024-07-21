# Table: Prices
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | product_id    | int     |
# | start_date    | date    |
# | end_date      | date    |
# | price         | int     |
# +---------------+---------+
# (product_id, start_date, end_date) is the primary key (combination of columns with unique values) for this table.
# Each row of this table indicates the price of the product_id in the period from start_date to end_date.
# For each product_id there will be no two overlapping periods. That means there will be no two intersecting periods for the same product_id.

# Table: UnitsSold
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | product_id    | int     |
# | purchase_date | date    |
# | units         | int     |
# +---------------+---------+
# This table may contain duplicate rows.
# Each row of this table indicates the date, units, and product_id of each product sold.

# Write a solution to find the average selling price for each product. average_price should be rounded to 2 decimal places.
#
# Return the result table in any order.
import pandas as pd
from pathlib import Path
import os
from collections import defaultdict

def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    OurDict = defaultdict(lambda: [0, 0])

    for index, row in prices.iterrows():
        OurDict[row["product_id"]]

    for index, row in units_sold.iterrows():
        OurDict[row["product_id"]][0] += (row["units"] * prices[
            (prices["product_id"] == row["product_id"]) &
            (prices["start_date"] <= row["purchase_date"]) &
            (prices["end_date"] >= row["purchase_date"])
        ].iloc[0]["price"])
        OurDict[row["product_id"]][1] += row["units"]

    ansDF = pd.DataFrame(columns=["product_id", "average_price"])
    for id, our_list in OurDict.items():
        ansDF.loc[(x := len(ansDF.index)), "product_id"] = id
        ansDF.loc[x, "average_price"] = round((our_list[0] / our_list[1]) if our_list[1] != 0 else 0, 2)

    return ansDF


def average_selling_price1(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(
        left=prices,
        right=units_sold,
        on="product_id",
        how="left"
    )

    ansDF = (merged
             .query("purchase_date >= start_date & purchase_date <= end_date")
             .assign(revenue=merged["price"] * merged["units"])
             .groupby(by="product_id", as_index=False)
             .apply(lambda x: (x["revenue"].sum() / x["units"].sum()).round(2))
             .rename(columns={None: "average_price"})
             )

    for i in set(prices["product_id"].unique()).difference(set(units_sold["product_id"].unique())):
        ansDF.loc[len(ansDF.index)] = [i, 0]

    return ansDF


path = Path(os.getcwd()) / "data" / "1251. Average Selling Price.xlsx"
prices = pd.read_excel(path, sheet_name="Prices")
units_sols = pd.read_excel(path, sheet_name="UnitsSold")
print(average_selling_price1(prices, units_sols))
