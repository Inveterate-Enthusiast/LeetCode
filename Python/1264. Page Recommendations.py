# Table: Friendship
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | user1_id      | int     |
# | user2_id      | int     |
# +---------------+---------+
# (user1_id, user2_id) is the primary key (combination of columns with unique values) for this table.
# Each row of this table indicates that there is a friendship relation between user1_id and user2_id.
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
# Write a solution to recommend pages to the user with user_id = 1 using the pages that your friends liked. It should not recommend pages you already liked.
#
# Return result table in any order without duplicates.
import pandas as pd

def page_recommendations(friendship: pd.DataFrame, likes: pd.DataFrame) -> pd.DataFrame:
    friends = pd.concat([
        (friendship.loc[friendship["user1_id"] == 1, ["user2_id"]].rename(columns={"user2_id": "user_id"})),
        (friendship.loc[friendship["user2_id"] == 1, ["user1_id"]].rename(columns={"user1_id": "user_id"}))
    ])
    used_pages = set(likes.loc[likes["user_id"] == 1, "page_id"].values)
    return pd.merge(
        left=friends,
        right=likes.rename(columns={"page_id": "recommended_page"}),
        on="user_id",
        how="inner"
    ).loc[lambda x: ~x["recommended_page"].isin(used_pages), ["recommended_page"]].drop_duplicates(keep="first")
