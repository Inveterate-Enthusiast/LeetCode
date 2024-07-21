# Table: NPV
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | id            | int     |
# | year          | int     |
# | npv           | int     |
# +---------------+---------+
# (id, year) is the primary key (combination of columns with unique values) of this table.
# The table has information about the id and the year of each inventory and the corresponding net present value.
#
# Table: Queries
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | id            | int     |
# | year          | int     |
# +---------------+---------+
# (id, year) is the primary key (combination of columns with unique values) of this table.
# The table has information about the id and the year of each inventory query.
#
# Write a solution to find the npv of each query of the Queries table.
#
# Return the result table in any order.
import pandas as pd

def npv_queries(npv: pd.DataFrame, queries: pd.DataFrame) -> pd.DataFrame:
    return pd.merge(
        left=queries,
        right=npv,
        how="left",
        on=["id", "year"]
    ).assign(npv=lambda x: x["npv"].fillna(0))[["id", "year", "npv"]]



