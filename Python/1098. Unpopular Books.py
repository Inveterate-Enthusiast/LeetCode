# Table: Books
#
# +----------------+---------+
# | Column Name    | Type    |
# +----------------+---------+
# | book_id        | int     |
# | name           | varchar |
# | available_from | date    |
# +----------------+---------+
# book_id is the primary key (column with unique values) of this table.
#
#
# Table: Orders
#
# +----------------+---------+
# | Column Name    | Type    |
# +----------------+---------+
# | order_id       | int     |
# | book_id        | int     |
# | quantity       | int     |
# | dispatch_date  | date    |
# +----------------+---------+
# order_id is the primary key (column with unique values) of this table.
# book_id is a foreign key (reference column) to the Books table.
#
#
# Write a solution to report the books that have sold less than 10 copies in the last year,
# excluding books that have been available for less than one month from today. Assume today is 2019-06-23.
#
# Return the result table in any order.
import pandas as pd
import numpy as np
from pathlib import Path
import os
from datetime import datetime
import arrow
from dateutil.relativedelta import relativedelta

def unpopular_books(books: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    today = pd.Timestamp(year=2019, month=6, day=23)
    books["dif"] = books.apply(lambda x: relativedelta(today, x["available_from"]).months + 12 * relativedelta(today, x["available_from"]).years, axis=1)
    books = books[books["dif"] > 0]
    merged = books.merge(
        right=orders.loc[orders["dispatch_date"] > (today - relativedelta(years=1))].groupby(by="book_id", as_index=False).agg(count=("quantity", "sum")),
        on="book_id",
        how="left").fillna(0)
    return merged.loc[merged["count"] < 10, ["book_id", "name"]]

path = Path(os.getcwd()) / "data" / "1098. Unpopular Books.xlsx"
books = pd.read_excel(path, sheet_name="Books")
orders = pd.read_excel(path, sheet_name="Orders")
print(unpopular_books(books, orders))

# x1 = datetime(2020, 6,16)
# x2 = datetime(2020, 7, 15)
#
# print(x2 - x1)
# print(len(list(arrow.Arrow.range("month", x1, x2))))
# print(relativedelta(x2, x1).months + 12*relativedelta(x2, x1).years)

# print(x1 + relativedelta(years=1))