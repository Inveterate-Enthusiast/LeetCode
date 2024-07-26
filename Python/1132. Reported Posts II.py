# Table: Actions
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | user_id       | int     |
# | post_id       | int     |
# | action_date   | date    |
# | action        | enum    |
# | extra         | varchar |
# +---------------+---------+
# This table may have duplicate rows.
# The action column is an ENUM (category) type of ('view', 'like', 'reaction', 'comment', 'report', 'share').
# The extra column has optional information about the action, such as a reason for the report or a type of reaction.
#
#
# Table: Removals
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | post_id       | int     |
# | remove_date   | date    |
# +---------------+---------+
# post_id is the primary key (column with unique values) of this table.
# Each row in this table indicates that some post was removed due to being reported or as a result of an admin review.
#
#
# Write a solution to find the average daily percentage of posts that got removed after being reported as spam, rounded to 2 decimal places.
import pandas as pd

def reported_posts(actions: pd.DataFrame, removals: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(
        left=actions[actions["extra"] == "spam"],
        right=removals,
        on="post_id",
        how="left",
        copy=False
    )
    merged["bool"] = ~merged["remove_date"].isna()
    grouped = merged.drop_duplicates(subset=["post_id", "action_date"], keep="first").groupby(by="action_date", as_index=False).agg(sum=("bool","sum"), count=("post_id", "nunique"))
    grouped["avg"] = grouped["sum"] / grouped["count"] * 100
    return pd.DataFrame({
        "average_daily_percent": [round(grouped["avg"].mean(), 2)]
    })
