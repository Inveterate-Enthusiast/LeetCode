# Table: Customer
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | customer_id   | int     |
# | name          | varchar |
# | visited_on    | date    |
# | amount        | int     |
# +---------------+---------+
# In SQL,(customer_id, visited_on) is the primary key for this table.
# This table contains data about customer transactions in a restaurant.
# visited_on is the date on which the customer with ID (customer_id) has visited the restaurant.
# amount is the total paid by a customer.
#
#
# You are the restaurant owner and you want to analyze a possible expansion (there will be at least one customer every day).
#
# Compute the moving average of how much the customer paid in a seven days window (i.e., current day + 6 days before).
# average_amount should be rounded to two decimal places.
#
# Return the result table ordered by visited_on in ascending order.
import pandas as pd
from pathlib import Path
import os

def restaurant_growth(customer: pd.DataFrame) -> pd.DataFrame:
    customer.sort_values(by="visited_on", ascending=True, inplace=True)
    customer["cum_sum"] = customer["amount"].cumsum()
    customer["row_num"] = range(customer.shape[0])
    grouped = customer.loc[customer.groupby(by="visited_on", as_index=True)["row_num"].idxmax()]
    grouped["7day_date"] = grouped["visited_on"] - pd.Timedelta(value=7, unit="day")
    grouped_2 = grouped[["visited_on", "cum_sum"]].rename(columns={"visited_on": "7day_date", "cum_sum": "7day_sum"})
    merged = pd.merge(
        left=grouped,
        right=grouped_2,
        on="7day_date",
        how="left"
    ).fillna(0)
    merged["amount"] = merged["cum_sum"] - merged["7day_sum"]
    merged["average_amount"] = round(merged["amount"] / 7 + 1e-9, 2)
    return merged.loc[merged["visited_on"] >= (merged["visited_on"].min() + pd.Timedelta(value=6, unit="day")), ["visited_on", "amount", "average_amount"]]


path = Path(os.getcwd()) / "data" / "1321. Restaurant Growth.xlsx"
customer = pd.read_excel(path)
print(restaurant_growth(customer))