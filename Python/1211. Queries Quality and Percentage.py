# Table: Queries
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | query_name  | varchar |
# | result      | varchar |
# | position    | int     |
# | rating      | int     |
# +-------------+---------+
# This table may have duplicate rows.
# This table contains information collected from some queries on a database.
# The position column has a value from 1 to 500.
# The rating column has a value from 1 to 5. Query with rating less than 3 is a poor query.

# We define query quality as:
#
# The average of the ratio between query rating and its position.
#
# We also define poor query percentage as:
#
# The percentage of all queries with rating less than 3.
#
# Write a solution to find each query_name, the quality and poor_query_percentage.
#
# Both quality and poor_query_percentage should be rounded to 2 decimal places.
#
# Return the result table in any order.
import pandas as pd
from pathlib import Path
import os

def queries_stats(queries: pd.DataFrame) -> pd.DataFrame:
    queries["quality"] = queries["rating"] / queries["position"] + 1e-6
    queries["poor_query_percentage"] = (queries["rating"] < 3) * 100
    return queries.groupby(by="query_name", as_index=False).agg({"quality": "mean", "poor_query_percentage": "mean"}).round(2)


path = Path(os.getcwd()) / "data" / "1211. Queries Quality and Percentage.xlsx"
queries = pd.read_excel(path)
print(queries_stats(queries))

