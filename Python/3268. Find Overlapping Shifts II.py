# Table: EmployeeShifts
#
# +------------------+----------+
# | Column Name      | Type     |
# +------------------+----------+
# | employee_id      | int      |
# | start_time       | datetime |
# | end_time         | datetime |
# +------------------+----------+
# (employee_id, start_time) is the unique key for this table.
# This table contains information about the shifts worked by employees, including the start time, and end time.
# Write a solution to analyze overlapping shifts for each employee.
# Two shifts are considered overlapping if they occur on the same date and one shift's end_time is later than another shift's start_time.
#
# For each employee, calculate the following:
#
# The maximum number of shifts that overlap at any given time.
# The total duration of all overlaps in minutes.
# Return the result table ordered by employee_id in ascending order.

import pandas as pd
import numpy as np

def calculate_shift_overlaps(employee_shifts: pd.DataFrame) -> pd.DataFrame:
    shifts = pd.concat([
        employee_shifts.assign(bool=1)[["employee_id", "start_time", "bool"]].rename(columns={"start_time": "time"}),
        employee_shifts.assign(bool=-1)[["employee_id", "end_time", "bool"]].rename(columns={"end_time": "time"})
    ]).sort_values(by=["time", "bool"], ascending=[True, False])
    shifts["cum_shifts"] = shifts.groupby(by="employee_id", as_index=False)["bool"].cumsum()
    grouped_shifts = (shifts
                      .groupby(by="employee_id", as_index=False)
                      .agg(max_overlapping_shifts=("cum_shifts", "max")))
    employee_shifts["id"] = employee_shifts.index + 1
    crossed = pd.merge(
        left=employee_shifts,
        right=employee_shifts,
        how="cross",
        suffixes=("_left", "_right")
    ).query("(employee_id_left == employee_id_right) & (id_left != id_right) & (start_time_left <= start_time_right) & (start_time_right < end_time_left)").rename(columns={"employee_id_left": "employee_id"})
    crossed["min_end"] = np.minimum(crossed["end_time_left"], crossed["end_time_right"])
    crossed["diff"] = (crossed["min_end"] - crossed["start_time_right"]).dt.total_seconds()
    grouped_duration = crossed.groupby(by="employee_id", as_index=False).agg(total_overlap_duration=("diff", "sum"))
    grouped_duration["total_overlap_duration"] = np.floor(grouped_duration["total_overlap_duration"] / 60)
    return pd.merge(
        left=grouped_shifts,
        right=grouped_duration,
        how="left",
        on="employee_id"
    )[["employee_id", "max_overlapping_shifts", "total_overlap_duration"]].fillna(0).sort_values(by="employee_id", ascending=True)