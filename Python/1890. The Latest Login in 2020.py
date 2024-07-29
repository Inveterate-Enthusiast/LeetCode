# Table: Logins
#
# +----------------+----------+
# | Column Name    | Type     |
# +----------------+----------+
# | user_id        | int      |
# | time_stamp     | datetime |
# +----------------+----------+
# (user_id, time_stamp) is the primary key (combination of columns with unique values) for this table.
# Each row contains information about the login time for the user with ID user_id.
#
#
# Write a solution to report the latest login for all users in the year 2020. Do not include the users who did not login in 2020.
#
# Return the result table in any order.
import pandas as pd

def latest_login(logins: pd.DataFrame) -> pd.DataFrame:
    return logins.loc[logins["time_stamp"].dt.year == 2020,:].groupby(by="user_id", as_index=False, dropna=True).agg(last_stamp=("time_stamp", "max"))