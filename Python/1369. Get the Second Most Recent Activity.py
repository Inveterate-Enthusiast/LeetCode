# Table: UserActivity
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | username      | varchar |
# | activity      | varchar |
# | startDate     | Date    |
# | endDate       | Date    |
# +---------------+---------+
# This table may contain duplicates rows.
# This table contains information about the activity performed by each user in a period of time.
# A person with username performed an activity from startDate to endDate.
#
#
# Write a solution to show the second most recent activity of each user.
#
# If the user only has one activity, return that one. A user cannot perform more than one activity at the same time.
#
# Return the result table in any order.

import pandas as pd
import numpy as np

def second_most_recent(user_activity: pd.DataFrame) -> pd.DataFrame:
    columns = user_activity.columns.values
    user_activity["rank"] = user_activity.groupby(by="username", as_index=False)["endDate"].rank(method="dense", ascending=False)
    user_activity["count"] = user_activity.groupby(by="username", as_index=False)["endDate"].transform("count")
    user_activity["pointer"] = np.where(
        (user_activity["count"] > 1) & (user_activity["rank"] == 2), 1,
        np.where(
            (user_activity["count"] == 1) & (user_activity["rank"] == 1), 1,
            0
        )
    )
    return user_activity.loc[user_activity["pointer"] == 1, columns]