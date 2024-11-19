# Table: EmployeeShifts
#
# +------------------+---------+
# | Column Name      | Type    |
# +------------------+---------+
# | employee_id      | int     |
# | start_time       | time    |
# | end_time         | time    |
# +------------------+---------+
# (employee_id, start_time) is the unique key for this table.
# This table contains information about the shifts worked by employees, including the start and end times on a specific date.
# Write a solution to count the number of overlapping shifts for each employee.
# Two shifts are considered overlapping if one shift’s end_time is later than another shift’s start_time.
#
# Return the result table ordered by employee_id in ascending order.

import pandas as pd
import numpy as np

def find_overlapping_shifts(employee_shifts: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(
        left=employee_shifts,
        right=employee_shifts,
        how="inner",
        on="employee_id",
        suffixes=("_1", "_2")
    ).query("(start_time_1 < start_time_2) & (end_time_1 > start_time_2)")
    grouped = merged.groupby(by="employee_id", as_index=False).agg(overlapping_shifts=("employee_id", "count"))
    return grouped.loc[grouped["overlapping_shifts"] > 0].sort_values(by="employee_id", ascending=True)