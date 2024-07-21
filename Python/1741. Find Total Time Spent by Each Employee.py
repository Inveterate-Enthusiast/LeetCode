# Table: Employees
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | emp_id      | int  |
# | event_day   | date |
# | in_time     | int  |
# | out_time    | int  |
# +-------------+------+
# (emp_id, event_day, in_time) is the primary key (combinations of columns with unique values) of this table.
# The table shows the employees' entries and exits in an office.
# event_day is the day at which this event happened, in_time is the minute at which the employee entered the office, and out_time is the minute at which they left the office.
# in_time and out_time are between 1 and 1440.
# It is guaranteed that no two events on the same day intersect in time, and in_time < out_time.
#
#
# Write a solution to calculate the total time in minutes spent by each employee on each day at the office. Note that within one day, an employee can enter and leave more than once. The time spent in the office for a single entry is out_time - in_time.
#
# Return the result table in any order.
import pandas as pd
from pathlib import Path
import os


def grouping(df: pd.DataFrame) -> int:
    return df.apply(lambda x: x["out_time"] - x["in_time"], axis=1).sum()

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    return (employees
            .groupby(by=["event_day", "emp_id"], as_index=True)
            .apply(grouping, include_groups=False)
            .reset_index()
            .rename(columns={0: "total_time", "event_day": "day"}))

path = Path(os.getcwd()) / "data" / "1741. Find Total Time Spent by Each Employee.xlsx"
employees = pd.read_excel(path)
print(total_time(employees))