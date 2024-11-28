# Table: Listens
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | user_id     | int     |
# | song_id     | int     |
# | day         | date    |
# +-------------+---------+
# This table may contain duplicate rows.
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
# (user1_id, user2_id) is the primary key (combination of columns with unique values) for this table.
# Each row of this table indicates that the users user1_id and user2_id are friends.
# Note that user1_id < user2_id.
#
#
# Write a solution to report the similar friends of Leetcodify users. A user x and user y are similar friends if:
#
# Users x and y are friends, and
# Users x and y listened to the same three or more different songs on the same day.
# Return the result table in any order. Note that you must return the similar pairs of friends
# the same way they were represented in the input (i.e., always user1_id < user2_id).

import pandas as pd

def leetcodify_similar_friends(listens: pd.DataFrame, friendship: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(
        left=listens.rename(columns={"user_id": "user1_id"}),
        right=listens.rename(columns={"user_id": "user2_id"}),
        how="inner",
        on=["song_id", "day"]
    ).query("(user1_id != user2_id) & (user1_id < user2_id)")
    grouped = (merged
               .groupby(by=["user1_id", "user2_id", "day"], as_index=False)
               .agg(song_count=("song_id", "nunique"))
               .query("song_count >= 3")
               [["user1_id", "user2_id"]]
               .drop_duplicates(keep="first"))
    friendship_1 = pd.concat([
                            friendship,
                            friendship.rename(columns={"user1_id": "user2_id", "user2_id": "user1_id"})[["user1_id", "user2_id"]]
                        ]).drop_duplicates(keep="first").query("user1_id < user2_id")
    friendship_1["bool"] = 1
    result = pd.merge(
        left=grouped,
        right=friendship_1,
        how="left",
        on=["user1_id", "user2_id"]
    )
    return result.loc[result["bool"] == 1, ["user1_id", "user2_id"]]

