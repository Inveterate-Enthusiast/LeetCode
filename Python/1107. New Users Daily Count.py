# Table: Traffic
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | user_id       | int     |
# | activity      | enum    |
# | activity_date | date    |
# +---------------+---------+
# This table may have duplicate rows.
# The activity column is an ENUM (category) type of ('login', 'logout', 'jobs', 'groups', 'homepage').
#
#
# Write a solution to reports for every date within at most 90 days from today,
# the number of users that logged in for the first time on that date. Assume today is 2019-06-30.
#
# Return the result table in any order.
import pandas as pd

def new_users_daily_count(traffic: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(
        left=(traffic.loc[traffic["activity_date"] >= (pd.Timestamp(year=2019, month=6, day=30) - pd.Timedelta(value=90, unit="D")), ["activity_date"]]),
        right=(traffic.loc[traffic["activity"] == "login"].groupby(by="user_id", as_index=False).agg(activity_date=("activity_date", "min"))),
        how="inner",
        on="activity_date"
    ).rename(columns={"activity_date": "login_date"})
    return merged.groupby(by="login_date", as_index=False).agg(user_count=("user_id", "nunique"))
