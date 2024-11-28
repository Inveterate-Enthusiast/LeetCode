# Table: Listens
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | user_id     | int     |
# | song_id     | int     |
# | day         | date    |
# +-------------+---------+
# This table may contain duplicates (In other words, there is no primary key for this table in SQL).
# Each row of this table indicates that the user user_id listened to the song song_id on the day day.
#
#
# Table: Friendship
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | user1_id      | int     |
# | user2_id      | int     |
# +---------------+---------+
# In SQL,(user1_id, user2_id) is the primary key for this table.
# Each row of this table indicates that the users user1_id and user2_id are friends.
# Note that user1_id < user2_id.
#
#
# Recommend friends to Leetcodify users. We recommend user x to user y if:
#
# Users x and y are not friends, and
# Users x and y listened to the same three or more different songs on the same day.
# Note that friend recommendations are unidirectional, meaning if user x and user y should be recommended to each other,
# the result table should have both user x recommended to user y and user y recommended to user x.
# Also, note that the result table should not contain duplicates (i.e., user y should not be recommended to user x multiple times.).
#
# Return the result table in any order.

import pandas as pd

def recommend_friends(listens: pd.DataFrame, friendship: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(
        left=listens,
        right=listens.rename(columns={"user_id": "recommended_id"}),
        how="inner",
        on=["song_id", "day"]
    ).query("user_id != recommended_id")

    concated_friendship = pd.concat([
        friendship.rename(columns={"user1_id": "user_id", "user2_id": "recommended_id"}),
        friendship.rename(columns={"user1_id": "recommended_id", "user2_id": "user_id"})
    ]).drop_duplicates(keep="first")
    concated_friendship["bool"] = 1

    merged_no_friends = pd.merge(
        left=merged,
        right=concated_friendship,
        how="left",
        on=["user_id", "recommended_id"]
    ).query("bool.isna()")

    merged_no_friends["count_songs"] = merged_no_friends.groupby(["user_id", "day", "recommended_id"], as_index=False)["song_id"].transform("nunique")
    filtered = merged_no_friends.loc[merged_no_friends["count_songs"] >= 3, ["user_id", "recommended_id"]].drop_duplicates(keep="first")
    return pd.concat([
        filtered,
        filtered.rename(columns={"recommended_id": "user_id", "user_id": "recommended_id"})[["user_id", "recommended_id"]]
    ]).drop_duplicates(keep="first")
