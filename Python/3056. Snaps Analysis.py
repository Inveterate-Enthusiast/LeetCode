# Table: Activities
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | activity_id   | int     |
# | user_id       | int     |
# | activity_type | enum    |
# | time_spent    | decimal |
# +---------------+---------+
# activity_id is column of unique values for this table.
# activity_type is an ENUM (category) type of ('send', 'open').
# This table contains activity id, user id, activity type and time spent.
# Table: Age
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | user_id     | int  |
# | age_bucket  | enum |
# +-------------+------+
# user_id is the column of unique values for this table.
# age_bucket is an ENUM (category) type of ('21-25', '26-30', '31-35').
# This table contains user id and age group.
# Write a solution to calculate the percentage of the total time spent on sending and opening snaps for each age group.
# Precentage should be rounded to 2 decimal places.
#
# Return the result table in any order.

import pandas as pd

def snap_analysis(activities: pd.DataFrame, age: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(
        left=activities,
        right=age,
        how="left",
        on="user_id"
    )
    send_group = merged.loc[merged["activity_type"] == "send"].groupby(by="age_bucket", as_index=False).agg(send_total=("time_spent", "sum"))
    open_group = merged.loc[merged["activity_type"] == "open"].groupby(by="age_bucket", as_index=False).agg(open_total=("time_spent", "sum"))
    result = pd.merge(
        left=send_group,
        right=open_group,
        how="outer",
        on="age_bucket"
    ).fillna(0)
    result["total"] = result["send_total"] + result["open_total"]
    result["send_perc"] = (result["send_total"] / result["total"] * 100).round(2)
    result["open_perc"] = (result["open_total"] / result["total"] * 100).round(2)
    return result[["age_bucket", "send_perc", "open_perc"]]