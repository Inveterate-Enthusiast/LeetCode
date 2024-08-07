# Table: Friends
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | id            | int     |
# | name          | varchar |
# | activity      | varchar |
# +---------------+---------+
# id is the id of the friend and the primary key for this table in SQL.
# name is the name of the friend.
# activity is the name of the activity which the friend takes part in.
#
#
# Table: Activities
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | id            | int     |
# | name          | varchar |
# +---------------+---------+
# In SQL, id is the primary key for this table.
# name is the name of the activity.
#
#
# Find the names of all the activities with neither the maximum nor the minimum number of participants.
#
# Each activity in the Activities table is performed by any person in the table Friends.
#
# Return the result table in any order.
import pandas as pd

def activity_participants(friends: pd.DataFrame, activities: pd.DataFrame) -> pd.DataFrame:
    grouped = friends.groupby(by="activity", as_index=False).agg(our_sum=("id", "nunique"))
    merged = pd.merge(
        left=activities.rename(columns={"name": "activity"}),
        right=grouped,
        on="activity",
        how="left"
    ).fillna(0)
    return merged.loc[
        ((merged["our_sum"] != merged["our_sum"].max()) & (merged["our_sum"] != merged["our_sum"].min())),
        ["activity"]
    ]