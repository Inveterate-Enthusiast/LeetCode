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
#
#
# Table: Likes
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | user_id     | int     |
# | page_id     | int     |
# +-------------+---------+
# (user_id, page_id) is the primary key (combination of columns with unique values) for this table.
# Each row of this table indicates that user_id likes page_id.
#
#
# You are implementing a page recommendation system for a social media website.
# Your system will recommend a page to user_id if the page is liked by at least one friend of user_id and is not liked by user_id.
#
# Write a solution to find all the possible page recommendations for every user.
# Each recommendation should appear as a row in the result table with these columns:
#
# user_id: The ID of the user that your system is making the recommendation to.
# page_id: The ID of the page that will be recommended to user_id.
# friends_likes: The number of the friends of user_id that like page_id.
# Return the result table in any order.

import pandas as pd

def recommend_page(friendship: pd.DataFrame, likes: pd.DataFrame) -> pd.DataFrame:
    general = pd.concat([
        pd.merge(
            left=friendship.rename(columns={"user1_id": "user_id", "user2_id": "friend"}),
            right=likes.rename(columns={"user_id": "friend"}),
            how="inner",
            on="friend"
        ),
        pd.merge(
            left=friendship[["user2_id", "user1_id"]].rename(columns={"user2_id": "user_id", "user1_id": "friend"}),
            right=likes.rename(columns={"user_id": "friend"}),
            how="inner",
            on="friend"
        )
    ])
    likes["bool"] = 1
    merged = pd.merge(
        left=general,
        right=likes,
        how="left",
        on=["user_id", "page_id"]
    )
    filtered = merged.loc[merged["bool"].isna()]
    grouped = filtered.groupby(by=["user_id", "page_id"], as_index=False).agg(friends_likes=("friend", "nunique"))
    return grouped