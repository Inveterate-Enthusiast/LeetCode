# Table: Customers
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | customer_id   | int     |
# | customer_name | varchar |
# +---------------+---------+
# customer_id is the column with unique values for this table.
# Each row of this table contains the name and the id customer.
#
#
# Write a solution to find the missing customer IDs. The missing IDs are ones that are not in the Customers table
# but are in the range between 1 and the maximum customer_id present in the table.
#
# Notice that the maximum customer_id will not exceed 100.
#
# Return the result table ordered by ids in ascending order.
import pandas as pd

def find_missing_ids(customers: pd.DataFrame) -> pd.DataFrame:
    our_ids = set(customers["customer_id"])
    our_max = max(our_ids)
    all_ids = set(range(1, our_max + 1))
    missing_ids = all_ids.difference(our_ids)
    return pd.DataFrame({
        "ids": sorted(list(missing_ids))
    })

