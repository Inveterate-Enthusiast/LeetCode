# Table: Activity
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | user_id       | int     |
# | session_id    | int     |
# | activity_date | date    |
# | activity_type | enum    |
# +---------------+---------+
# This table may have duplicate rows.
# The activity_type column is an ENUM (category) of type ('open_session', 'end_session', 'scroll_down', 'send_message').
# The table shows the user activities for a social media website.
# Note that each session belongs to exactly one user.

# Write a solution to find the daily active user count for a period
# of 30 days ending 2019-07-27 inclusively.
# A user was active on someday if they made at least one activity on that day.
#
# Return the result table in any order.
import pandas as pd
from datetime import datetime as dt

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    return activity[
        (activity["activity_date"] <= dt(2019,7,27)) &
        (activity["activity_date"] > (dt(2019,7,27) - pd.DateOffset(days=30)))].\
        groupby(by="activity_date", as_index=False).agg(active_users=("user_id", "nunique")).rename(columns={"activity_date":"day"})

