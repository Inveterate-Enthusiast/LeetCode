# Table: Relations
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | user_id     | int  |
# | follower_id | int  |
# +-------------+------+
# (user_id, follower_id) is the primary key (combination of columns with unique values) for this table.
# Each row of this table indicates that the user with ID follower_id is following the user with ID user_id.
#
#
# Write a solution to find all the pairs of users with the maximum number of common followers.
# In other words, if the maximum number of common followers between any two users is maxCommon,
# then you have to return all pairs of users that have maxCommon common followers.
#
# The result table should contain the pairs user1_id and user2_id where user1_id < user2_id.
#
# Return the result table in any order.
import pandas as pd

def find_pairs(relations: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(
        left=relations.rename(columns={"user_id": "user"}),
        right=relations.rename(columns={"user_id": "user"}),
        how="inner",
        on="follower_id",
        suffixes=("1_id", "2_id")
    ).query("user1_id < user2_id")
    grouped = merged.groupby(by=["user1_id", "user2_id"], as_index=False).agg(count=("follower_id", "count"))
    return grouped.loc[grouped["count"] == grouped["count"].max(), ["user1_id", "user2_id"]]

