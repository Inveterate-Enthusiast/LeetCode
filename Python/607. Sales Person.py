# Table: SalesPerson
#
# +-----------------+---------+
# | Column Name     | Type    |
# +-----------------+---------+
# | sales_id        | int     |
# | name            | varchar |
# | salary          | int     |
# | commission_rate | int     |
# | hire_date       | date    |
# +-----------------+---------+
# sales_id is the primary key (column with unique values) for this table.
# Each row of this table indicates the name and the ID of a salesperson alongside their salary, commission rate, and hire date.

# Table: Company
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | com_id      | int     |
# | name        | varchar |
# | city        | varchar |
# +-------------+---------+
# com_id is the primary key (column with unique values) for this table.
# Each row of this table indicates the name and the ID of a company and the city in which the company is located.

# Table: Orders
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | order_id    | int  |
# | order_date  | date |
# | com_id      | int  |
# | sales_id    | int  |
# | amount      | int  |
# +-------------+------+
# order_id is the primary key (column with unique values) for this table.
# com_id is a foreign key (reference column) to com_id from the Company table.
# sales_id is a foreign key (reference column) to sales_id from the SalesPerson table.
# Each row of this table contains information about one order.
# This includes the ID of the company, the ID of the salesperson, the date of the order, and the amount paid.

# Write a solution to find the names of all the salespersons who did not have any orders related to the company
# with the name "RED".
#
# Return the result table in any order.
import pandas as pd
from datetime import datetime
import numpy as np
from pprint import pprint

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(
        left = orders,
        right = company,
        on = "com_id",
        how = "outer",
        suffixes = ("_or", "_com"),
        copy = False
    )

    merged = pd.merge(
        left = merged,
        right = sales_person,
        on = "sales_id",
        how = "outer",
        suffixes = ("_or", "_sale"),
        copy = False
    )

    grouped = merged.groupby(
        by = "name_sale",
        as_index = False
    )["name_or"].apply(set)
    return grouped[grouped["name_or"].apply(lambda x: "RED" not in x)][["name_sale"]].rename(columns={"name_sale": "name"})

def sales_person1(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(
        left = orders,
        right = company[company["name"] == "RED"],
        on = "com_id",
        how = "inner"
    ).drop_duplicates("sales_id")

    sale_filter = ~sales_person["sales_id"].isin(merged["sales_id"])

    return sales_person[sale_filter][["name"]]











Sales_person = pd.DataFrame({
    "sales_id": [1, 2, 3, 4, 5],
    "name": ["John", "Amy", "Mark", "Pam", "Alex"],
    "salary": [100_000, 12_000, 65_000, 25_000, 5_000],
    "commission_rate": [6, 5, 12, 25, 10],
    "hire_date": [datetime(2006, 1, 4),
                  datetime(2010, 5, 1),
                  datetime(2012, 8, 25),
                  datetime(2005, 1, 1),
                  datetime(2007, 2, 3)]
})

company = pd.DataFrame({
    "com_id": [1, 2, 3, 4],
    "name": ["RED", "ORANGE", "YELLOW", "GREEN"],
    "city": ["Boston", "New York", "Boston", "Austin"]
})

orders = pd.DataFrame({
    "order_id": [1, 2, 3, 4],
    "order_date": [datetime(2014, 1, 1),
                   datetime(2014, 1, 2),
                   datetime(2014, 1, 3),
                   datetime(2014, 1, 4)],
    "com_id": [3, 4, 1, 1],
    "sales_id": [4, 5, 1, 4],
    "amount": [10_000, 5_000, 50_000, 25_000]
})

print(sales_person1(Sales_person, company, orders))