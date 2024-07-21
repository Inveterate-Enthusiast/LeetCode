# Table: Users
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | id            | int     |
# | name          | varchar |
# +---------------+---------+
# id is the column with unique values for this table.
# name is the name of the user.

# Table: Rides
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | id            | int     |
# | user_id       | int     |
# | distance      | int     |
# +---------------+---------+
# id is the column with unique values for this table.
# user_id is the id of the user who traveled the distance "distance".

# Write a solution to report the distance traveled by each user.
#
# Return the result table ordered by travelled_distance in descending order,
# if two or more users traveled the same distance, order them by their name in ascending order.
import pandas as pd

def top_travellers(users: pd.DataFrame, rides: pd.DataFrame) -> pd.DataFrame:
    grouped = rides.groupby(by="user_id", as_index=False).agg(travelled_distance=("distance", "sum"))
    return pd.merge(
        left=grouped,
        right=users,
        left_on="user_id",
        right_on="id",
        how="right"
    )[["name", "travelled_distance"]].sort_values(by=["travelled_distance", "name"], ascending=[False, True]).fillna(0)



