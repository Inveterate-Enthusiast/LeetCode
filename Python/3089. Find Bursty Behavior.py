# Table: Posts
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | post_id     | int     |
# | user_id     | int     |
# | post_date   | date    |
# +-------------+---------+
# post_id is the primary key (column with unique values) for this table.
# Each row of this table contains post_id, user_id, and post_date.
# Write a solution to find users who demonstrate bursty behavior in their posting patterns during February 2024.
# Bursty behavior is defined as any period of 7 consecutive days where a user's posting frequency is at least twice
# to their average weekly posting frequency for February 2024.
#
# Note: Only include the dates from February 1 to February 28 in your analysis, which means you should count February as having exactly 4 weeks.
#
# Return the result table orderd by user_id in ascending order.
import pandas as pd
from datetime import datetime as dt
from pathlib import Path
import os

def find_bursty_behavior(posts: pd.DataFrame) -> pd.DataFrame:
    filtered = posts.loc[
        (posts["post_date"] >= dt(2024, 2, 1))
        & (posts["post_date"] <= (dt(2024, 2, 28)))
    ]
    filtered.sort_values(by=["user_id", "post_date"], ascending=[True, True], inplace=True)
    filtered.set_index("post_date", inplace=True)
    filtered["7day_posts"] = (
        filtered.groupby("user_id")["post_id"]
        .rolling("7D")
        .count()
        .reset_index(level=0, drop=True)
    )
    filtered["max_7day_posts"] = filtered.groupby(by="user_id", as_index=False)["7day_posts"].transform("max")
    filtered["total_posts"] = filtered.groupby(by="user_id", as_index=False)["post_id"].transform("nunique")
    filtered["avg_weekly_posts"] = filtered["total_posts"] / 4
    return (filtered
            .loc[filtered["max_7day_posts"] >= (filtered["avg_weekly_posts"] * 2), ["user_id", "max_7day_posts", "avg_weekly_posts"]]
            .drop_duplicates(keep="first")
            .sort_values(by="user_id", ascending=True))

posts = pd.read_excel(Path(os.getcwd()) / "data" / "3089. Find Bursty Behavior.xlsx")
print(find_bursty_behavior(posts))