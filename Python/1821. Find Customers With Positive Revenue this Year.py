# Table: Customers
#
# +--------------+------+
# | Column Name  | Type |
# +--------------+------+
# | customer_id  | int  |
# | year         | int  |
# | revenue      | int  |
# +--------------+------+
# (customer_id, year) is the primary key (combination of columns with unique values) for this table.
# This table contains the customer ID and the revenue of customers in different years.
# Note that this revenue can be negative.
#
#
# Write a solution to report the customers with postive revenue in the year 2021.
#
# Return the result table in any order.
import pandas as pd

def find_customers(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.loc[customers["year"] == 2021].groupby(by="customer_id", as_index=False).agg(total=("revenue", "sum")).query("total > 0")[["customer_id"]]