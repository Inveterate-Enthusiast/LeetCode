# Table: UserVisits
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | user_id     | int  |
# | visit_date  | date |
# +-------------+------+
# This table does not have a primary key, it might contain duplicate rows.
# This table contains logs of the dates that users visited a certain retailer.
#
#
# Assume today's date is '2021-1-1'.
#
# Write a solution that will, for each user_id, find out the largest window of days between each
# visit and the one right after it (or today if you are considering the last visit).
#
# Return the result table ordered by user_id.
import pandas as pd
from datetime import datetime
from pathlib import Path
import os

def grouping(df: pd.Series) -> pd.Series:
    today = datetime(2021, 1, 1)
    df["past_date"] = df["visit_date"].shift(1)
    df["diff"] = (df["visit_date"] - df["past_date"]).dt.days.fillna(0)
    return pd.Series(data=max(df["diff"].max(), (today - df["visit_date"].max()).days), index=["biggest_window"])

def biggest_window(user_visits: pd.DataFrame) -> pd.DataFrame:
    if user_visits.empty:
        return pd.DataFrame({
            "user_id": list(),
            "biggest_window": list()
        })
    user_visits.sort_values(by="visit_date", ascending=True, inplace=True)
    grouped = user_visits.groupby(by="user_id", as_index=True).apply(grouping, include_groups=False).reset_index()
    return grouped.sort_values(by="user_id", ascending=True)


def biggest_window1(user_visits: pd.DataFrame) -> pd.DataFrame:
    today = datetime(2021, 1, 1)
    added = pd.concat(
        [user_visits,
         pd.DataFrame(columns=user_visits.columns,
                      data=list(
                          map(
                              list, zip(*[
                                  (x := user_visits["user_id"].unique()),
                                  [today] * len(x)
                              ])
                          ))
                      )
         ]
    ).sort_values(by=["user_id", "visit_date"], ascending=[True, True])
    added["past_date"] = added.groupby(by="user_id", as_index=False)["visit_date"].shift(1)
    added["diff"] = (added["visit_date"] - added["past_date"]).dt.days
    return added.groupby(by="user_id", as_index=False).agg(biggest_window=("diff", "max")).sort_values(by="user_id", ascending=True)

user_visits = pd.read_excel(Path(os.getcwd()) / "data" / "1709. Biggest Window Between Visits.xlsx")
print(biggest_window1(user_visits))