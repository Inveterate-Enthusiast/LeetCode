# Table: Salesperson
#
# +----------------+---------+
# | Column Name    | Type    |
# +----------------+---------+
# | salesperson_id | int     |
# | name           | varchar |
# +----------------+---------+
# salesperson_id contains unique values.
# Each row in this table shows the ID of a salesperson.
#
#
# Table: Customer
#
# +----------------+------+
# | Column Name    | Type |
# +----------------+------+
# | customer_id    | int  |
# | salesperson_id | int  |
# +----------------+------+
# customer_id contains unique values.
# salesperson_id is a foreign key (reference column) from the Salesperson table.
# Each row in this table shows the ID of a customer and the ID of the salesperson.
#
#
# Table: Sales
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | sale_id     | int  |
# | customer_id | int  |
# | price       | int  |
# +-------------+------+
# sale_id contains unique values.
# customer_id is a foreign key (reference column) from the Customer table.
# Each row in this table shows ID of a customer and the price they paid for the sale with sale_id.
#
#
# Write a solution to report the sum of prices paid by the customers of each salesperson. If a salesperson does not have any customers, the total value should be 0.
#
# Return the result table in any order.
import pandas as pd

def calculate_influence(salesperson: pd.DataFrame, customer: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    grouped = sales.groupby(by="customer_id", as_index=False).agg(total=("price", "sum"))
    merged = pd.merge(
        left=customer,
        right=grouped,
        how="left",
        on="customer_id"
    ).fillna(0)
    grouped_2 = merged.groupby(by="salesperson_id", as_index=False).agg(total=("total", "sum"))
    merged_2 = pd.merge(
        left=salesperson,
        right=grouped_2,
        how="left",
        on="salesperson_id"
    ).fillna(0)
    return merged_2[["salesperson_id", "name", "total"]]