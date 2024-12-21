# Table: Friends
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | user1       | int  |
# | user2       | int  |
# +-------------+------+
# (user1, user2) is the primary key (combination of unique values) of this table.
# Each row contains information about friendship where user1 and user2 are friends.
# Write a solution to find the popularity percentage for each user on Meta/Facebook.
# The popularity percentage is defined as the total number of friends the user has divided by the total number of users
# on the platform, then converted into a percentage by multiplying by 100, rounded to 2 decimal places.
#
# Return the result table ordered by user1 in ascending order.

import pandas as pd

def popularity_percentage(friends: pd.DataFrame) -> pd.DataFrame:
    concated = pd.concat([
        friends.rename(columns={"user2": "friends"}),
        friends.rename(columns={"user2": "user1", "user1": "friends"})[["user1", "friends"]]
    ])
    users_cnt = len(set(concated["user1"].tolist()))
    grouped = concated.groupby(by="user1", as_index=False).agg(friends=("friends", "nunique"))
    grouped["percentage_popularity"] = (grouped["friends"] / users_cnt * 100).round(2)
    return grouped[["user1", "percentage_popularity"]].sort_values(by="user1", ascending=True)