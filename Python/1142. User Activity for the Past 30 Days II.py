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

# Write a solution to find the average number of sessions per user for a period of 30 days ending 2019-07-27 inclusively,
# rounded to 2 decimal places. The sessions we want to count for a user are those with at least one activity in that time period.
import pandas as pd
from datetime import datetime as dt
import pandas as np

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    grouped = activity[
        (activity["activity_date"] <= dt(2019,7,27)) &
        (activity["activity_date"] > (dt(2019,7,27) - pd.DateOffset(days=30)))
    ].groupby("user_id", as_index=False).agg(count=("session_id", "nunique"))

    ans = grouped['count'].mean()

    return pd.DataFrame({
        "average_sessions_per_user": [round(ans, 2) if ans is not np.nan else 0]
    })

def user_activity1(activity: pd.DataFrame) -> pd.DataFrame:
    grouped = activity[
        (activity["activity_date"] <= dt(2019, 7, 27)) &
        (activity["activity_date"] > (dt(2019, 7, 27) - pd.DateOffset(days=30)))
        ].groupby("user_id", as_index=False).agg(count=("session_id", "nunique"))

    ans = grouped['count'].mean()

    return pd.DataFrame({
        "average_sessions_per_user": [round(ans, 2) if not pd.isna(ans) else 0]
    })
