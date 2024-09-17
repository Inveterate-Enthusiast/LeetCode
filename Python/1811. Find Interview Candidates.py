# Table: Contests
#
# +--------------+------+
# | Column Name  | Type |
# +--------------+------+
# | contest_id   | int  |
# | gold_medal   | int  |
# | silver_medal | int  |
# | bronze_medal | int  |
# +--------------+------+
# contest_id is the column with unique values for this table.
# This table contains the LeetCode contest ID and the user IDs of the gold, silver, and bronze medalists.
# It is guaranteed that any consecutive contests have consecutive IDs and that no ID is skipped.
#
#
# Table: Users
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | user_id     | int     |
# | mail        | varchar |
# | name        | varchar |
# +-------------+---------+
# user_id is the column with unique values for this table.
# This table contains information about the users.
#
#
# Write a solution to report the name and the mail of all interview candidates. A user is an interview candidate if at least one of these two conditions is true:
#
# The user won any medal in three or more consecutive contests.
# The user won the gold medal in three or more different contests (not necessarily consecutive).
# Return the result table in any order.
import pandas as pd
from pathlib import Path
import os

def find_interview_candidates(contests: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    if contests.empty:
        return pd.DataFrame({
            "name": list(),
            "mail": list()
        })

    melted = pd.melt(frame=contests, id_vars="contest_id", value_vars=None, var_name="contests", value_name="user_id")
    melted["rank"] = melted.groupby(by="user_id", as_index=False)["contest_id"].rank(method="min", ascending=True)
    melted["diff"] = melted["contest_id"] - melted["rank"]
    first_condition = set(melted
                          .groupby(by=["user_id", "diff"], as_index=False)
                          .agg(count=("diff", "count"))
                          .query("count >= 3")
                          .drop_duplicates(subset="user_id", keep="first")["user_id"])
    second_condition = set(melted
                           .loc[melted["contests"] == "gold_medal"]
                           .groupby(by="user_id", as_index=False)
                           .agg(count=("contest_id", "nunique"))
                           .query("count >= 3")["user_id"])
    return pd.merge(
        left=pd.DataFrame({
            "user_id": list(first_condition.union(second_condition))
        }),
        right=users,
        how="left",
        on="user_id"
    )[["name", "mail"]]

path = Path(os.getcwd()) / "data" / "1811. Find Interview Candidates.xlsx"
contests = pd.read_excel(path, sheet_name="Contests")
users = pd.read_excel(path, sheet_name="Users")
print(find_interview_candidates(contests, users))