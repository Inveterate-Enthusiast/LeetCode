# Table: Friends
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | user_id1    | int  |
# | user_id2    | int  |
# +-------------+------+
# (user_id1, user_id2) is the primary key (combination of columns with unique values) for this table.
# Each row contains user id1, user id2, both of whom are friends with each other.
# Write a solution to find all pairs of users who are friends with each other and have no mutual friends.
#
# Return the result table ordered by user_id1, user_id2 in ascending order.
import pandas as pd

def friends_with_no_mutual_friends(friends: pd.DataFrame) -> pd.DataFrame:
    concated = pd.concat(
        [friends.rename(columns={"user_id1": "user_id", "user_id2": "friends"}),
         friends.rename(columns={"user_id2": "user_id", "user_id1": "friends"})]
    )
    grouped = concated.groupby(by="user_id", as_index=False).agg(friends=("friends", lambda x: set(x)))
    merged1 = pd.merge(
        left=friends,
        right=grouped.rename(columns={"friends": "friends1"}),
        how="left",
        left_on="user_id1",
        right_on="user_id"
    )
    merged2 = pd.merge(
        left=merged1,
        right=grouped.rename(columns={"friends": "friends2"}),
        how="left",
        left_on="user_id2",
        right_on="user_id"
    )
    merged2["common"] = merged2.apply(lambda x: x["friends1"].intersection(x["friends2"]), axis=1)
    return (merged2
            .loc[merged2["common"] == set(), ["user_id1", "user_id2"]]
            .drop_duplicates(keep="first")
            .sort_values(by=["user_id1", "user_id2"], ascending=[True, True]))
