# Table: Activity
#
# +----------------+---------+
# | Column Name    | Type    |
# +----------------+---------+
# | machine_id     | int     |
# | process_id     | int     |
# | activity_type  | enum    |
# | timestamp      | float   |
# +----------------+---------+
# The table shows the user activities for a factory website.
# (machine_id, process_id, activity_type) is the primary key (combination of columns with unique values) of this table.
# machine_id is the ID of a machine.
# process_id is the ID of a process running on the machine with ID machine_id.
# activity_type is an ENUM (category) of type ('start', 'end').
# timestamp is a float representing the current time in seconds.
# 'start' means the machine starts the process at the given timestamp and 'end' means the machine ends the process at the given timestamp.
# The 'start' timestamp will always be before the 'end' timestamp for every (machine_id, process_id) pair.
#
# There is a factory website that has several machines each running the same number of processes.
# Write a solution to find the average time each machine takes to complete a process.
#
# The time to complete a process is the 'end' timestamp minus the 'start' timestamp.
# The average time is calculated by the total time to complete every process on the machine divided by the number of processes that were run.
#
# The resulting table should have the machine_id along with the average time as processing_time, which should be rounded to 3 decimal places.
#
# Return the result table in any order.
import pandas as pd
from pathlib import Path
import os
from typing import Optional

def taken_time(df: pd.DataFrame) -> Optional[float]:
    ans = 0
    for index, row in df.sort_values(by="timestamp", ascending=True).iterrows():
        if row["activity_type"] == "start":
            ans -= row["timestamp"]
        elif row["activity_type"] == "end":
            ans += row["timestamp"]

    return ans

def total_ratio_time(df: pd.DataFrame) -> Optional[float]:
    return round(df.loc[:, "processing_time"].sum() / df.loc[:, "processing_time"].count(), 3)

def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    grouped = activity.groupby(by=["machine_id", "process_id"], as_index=False).apply(taken_time, include_groups=False)
    grouped.columns = ["machine_id", "process_id", "processing_time"]
    return grouped.groupby(by="machine_id", as_index=False).apply(total_ratio_time, include_groups=False).rename(columns={None: "processing_time"})

path = Path(os.getcwd()) / "data" / "1661. Average Time of Process per Machine.xlsx"
activity = pd.read_excel(path)
print(get_average_time(activity))
