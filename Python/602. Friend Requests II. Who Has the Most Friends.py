# Table: RequestAccepted
#
# +----------------+---------+
# | Column Name    | Type    |
# +----------------+---------+
# | requester_id   | int     |
# | accepter_id    | int     |
# | accept_date    | date    |
# +----------------+---------+
# (requester_id, accepter_id) is the primary key (combination of columns with unique values) for this table.
# This table contains the ID of the user who sent the request, the ID of the user who received the request, and the date when the request was accepted.
#
#
# Write a solution to find the people who have the most friends and the most friends number.
#
# The test cases are generated so that only one person has the most friends.
import pandas as pd
from pathlib import Path
import os

def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:
    grouped1 = request_accepted.rename(columns={"requester_id": "id"}).groupby(by="id", as_index=False).agg(num=("accepter_id", "nunique"))
    grouped2 = request_accepted.rename(columns={"accepter_id": "id"}).groupby(by="id", as_index=False).agg(num=("requester_id", "nunique"))
    merged = pd.merge(
        left=grouped1,
        right=grouped2,
        on="id",
        how="outer",
        suffixes=("_1", "_2")
    ).fillna(0)
    merged["num"] = merged["num_1"] + merged["num_2"]
    return merged.loc[merged["num"] == merged["num"].max(), ["id", "num"]]

def most_friends1(request_accepted: pd.DataFrame) -> pd.DataFrame:
    unioned = pd.DataFrame(columns=["id"])
    unioned["id"] = pd.concat([request_accepted["requester_id"], request_accepted["accepter_id"]])
    return unioned.groupby(by="id", as_index=False).agg(num=("id", "count")).query("num == num.max()")

path = Path(os.getcwd()) / "data" / "602. Friend Requests II Who Has the Most Friends.xlsx"
request_accepted = pd.read_excel(path)
print(most_friends1(request_accepted))