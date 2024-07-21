# Table: Visits
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | visit_id    | int     |
# | customer_id | int     |
# +-------------+---------+
# visit_id is the column with unique values for this table.
# This table contains information about the customers who visited the mall.
#
#
# Table: Transactions
#
# +----------------+---------+
# | Column Name    | Type    |
# +----------------+---------+
# | transaction_id | int     |
# | visit_id       | int     |
# | amount         | int     |
# +----------------+---------+
# transaction_id is column with unique values for this table.
# This table contains information about the transactions made during the visit_id.
#
#
# Write a solution to find the IDs of the users who visited without making any transactions and the number of times they made these types of visits.
#
# Return the result table sorted in any order.
import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    return visits.loc[~visits["visit_id"].isin(transactions["visit_id"])].groupby(by="customer_id", as_index=False).agg(count_no_trans=("visit_id", "size"))

def find_customers1(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    our_set = set(transactions["visit_id"])
    return visits.loc[~visits["visit_id"].isin(our_set)].groupby(by="customer_id", as_index=False).agg(count_no_trans=("visit_id", "size"))
