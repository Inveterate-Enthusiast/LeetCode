# Table: Follow
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | followee    | varchar |
# | follower    | varchar |
# +-------------+---------+
# (followee, follower) is the primary key (combination of columns with unique values) for this table.
# Each row of this table indicates that the user follower follows the user followee on a social network.
# There will not be a user following themself.
#
#
# A second-degree follower is a user who:
#
# follows at least one user, and
# is followed by at least one user.
# Write a solution to report the second-degree users and the number of their followers.
#
# Return the result table ordered by follower in alphabetical order.
import pandas as pd
import os
from pathlib import Path

def second_degree_follower(follow: pd.DataFrame) -> pd.DataFrame:
    follow["bool"] = follow.apply(lambda x: x["followee"] in follow["follower"].values, axis=1)
    grouped = follow.loc[follow["bool"]].groupby(by="followee", as_index=False).agg(num=("follower", "count")).rename(columns={"followee": "follower"})
    return grouped.sort_values(by="follower", ascending=True)

def second_degree_follower1(follow: pd.DataFrame) -> pd.DataFrame:
    grouped_ee = follow.groupby(by="followee", as_index=False).agg(num=("follower", "nunique")).query("num >= 1").rename(columns={"followee": "follower"})
    grouped_er = follow.groupby(by="follower", as_index=False).agg(num=("followee", "nunique")).query("num >= 1")
    return grouped_ee.loc[grouped_ee["follower"].isin(grouped_er["follower"])].sort_values(by="follower", ascending=True)

path = Path(os.getcwd()) / "data" / "614. Second Degree Follower.xlsx"
follow = pd.read_excel(path)
print(second_degree_follower1(follow))