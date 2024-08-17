# Table: Users
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | user_id     | int     |
# | name        | varchar |
# +-------------+---------+
# user_id is the column with unique values for this table.
# Each row of this table contains user id and name.
# Table: Rides
#
# +--------------+------+
# | Column Name  | Type |
# +--------------+------+
# | ride_id      | int  |
# | user_id      | int  |
# | distance     | int  |
# +--------------+------+
# ride_id is the column of unique values for this table.
# Each row of this table contains ride id, user id, and traveled distance.
# Write a solution to calculate the distance traveled by each user.
# If there is a user who hasn't completed any rides, then their distance should be considered as 0.
# Output the user_id, name and total traveled distance.
#
# Return the result table ordered by user_id in ascending order.
import pandas as pd

def get_total_distance(users: pd.DataFrame, rides: pd.DataFrame) -> pd.DataFrame:
    grouped = rides.groupby(by="user_id", as_index=False).agg(distance=("distance", "sum"))
    return (pd.merge(
        left=users,
        right=grouped,
        on="user_id",
        how="left"
    )
            .sort_values(by="user_id", ascending=True)
            .fillna(0)
            .rename(columns={"distance": "traveled distance"}))

