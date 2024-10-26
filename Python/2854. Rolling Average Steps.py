# Table: Steps
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | user_id     | int  |
# | steps_count | int  |
# | steps_date  | date |
# +-------------+------+
# (user_id, steps_date) is the primary key for this table.
# Each row of this table contains user_id, steps_count, and steps_date.
# Write a solution to calculate 3-day rolling averages of steps for each user.
#
# We calculate the n-day rolling average this way:
#
# For each day, we calculate the average of n consecutive days of step counts ending on that day if available,
# otherwise, n-day rolling average is not defined for it.
# Output the user_id, steps_date, and rolling average. Round the rolling average to two decimal places.
#
# Return the result table ordered by user_id, steps_date in ascending order.
import pandas as pd
import numpy as np
from pathlib import Path
import os

def rolling_average(steps: pd.DataFrame) -> pd.DataFrame:
    window = 3
    min_periods = (window - 1)
    steps.sort_values(by=["user_id", "steps_date"], ascending=[True, True], inplace=True)
    steps["dif"] = steps.groupby(by="user_id", as_index=False)["steps_date"].transform(lambda x: (x - x.shift(1)).dt.days).fillna(0)
    steps["bool"] = steps.groupby(by="user_id", as_index=True)["dif"].rolling(window=min_periods, min_periods=min_periods).apply(lambda x: x.prod()).explode().reset_index(level=0, drop=True)
    steps["rolling_average"] = np.where(steps["bool"] == 1, steps.groupby(by="user_id", as_index=True)["steps_count"].rolling(window=window, min_periods=window).mean().round(2), np.nan)
    return steps.loc[~steps["rolling_average"].isna(), ["user_id", "steps_date", "rolling_average"]]

steps = pd.read_excel(Path(os.getcwd()) / "data" / "2854. Rolling Average Steps.xlsx", sheet_name="Steps")
print(rolling_average(steps))