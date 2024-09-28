# Table: Friendship
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | user1_id    | int  |
# | user2_id    | int  |
# +-------------+------+
# (user1_id, user2_id) is the primary key (combination of columns with unique values) for this table.
# Each row of this table indicates that the users user1_id and user2_id are friends.
# Note that user1_id < user2_id.
#
#
# A friendship between a pair of friends x and y is strong if x and y have at least three common friends.
#
# Write a solution to find all the strong friendships.
#
# Note that the result table should not contain duplicates with user1_id < user2_id.
#
# Return the result table in any order.
import pandas as pd
from pathlib import Path
import os

def strong_friendship(friendship: pd.DataFrame) -> pd.DataFrame:
    grouped1 = friendship.groupby(by="user1_id", as_index=False).agg(friends=("user2_id", lambda x: set(x))).rename(columns={"user1_id": "user"})
    grouped2 = friendship.groupby(by="user2_id", as_index=False).agg(friends=("user1_id", lambda x: set(x))).rename(columns={"user2_id": "user"})
    grouped = pd.concat([grouped1, grouped2])
    grouped = grouped.groupby(by="user", as_index=False).agg(friends=("friends", lambda x: set.union(*x)))
    merged = pd.merge(
        left=grouped,
        right=grouped,
        how="cross",
        suffixes=("1_id", "2_id")
    ).query("user1_id < user2_id")
    merged = merged.loc[merged.apply(lambda x: (x["user1_id"] in x["friends2_id"]) & (x["user2_id"] in x["friends1_id"]), axis=1)]
    merged["common_friend"] = (merged
                                .apply(lambda x: len(y) if (y := (x["friends1_id"]
                                                                       .intersection(x["friends2_id"])
                                                                       .difference(set([x["user1_id"], x["user2_id"]])))) else 0,
                                       axis=1))

    return merged.loc[merged["common_friend"] >= 3, ["user1_id", "user2_id", "common_friend"]]

friendship = pd.read_excel(Path(os.getcwd()) / "data" / "1949. Strong Friendship.xlsx")
print(strong_friendship(friendship))