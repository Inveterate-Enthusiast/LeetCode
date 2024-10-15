# Table: Employees
#
# +--------------+------+
# | Column Name  | Type |
# +--------------+------+
# | employee_id  | int  |
# | needed_hours | int  |
# +--------------+------+
# employee_id is column with unique values for this table.
# Each row contains the id of an employee and the minimum number of hours needed for them to work to get their salary.
#
#
# Table: Logs
#
# +-------------+----------+
# | Column Name | Type     |
# +-------------+----------+
# | employee_id | int      |
# | in_time     | datetime |
# | out_time    | datetime |
# +-------------+----------+
# (employee_id, in_time, out_time) is the primary key (combination of columns with unique values) for this table.
# Each row of this table shows the time stamps for an employee. in_time is the time the employee started to work, and out_time is the time the employee ended work.
# All the times are in October 2022. out_time can be one day after in_time which means the employee worked after the midnight.
#
#
# In a company, each employee must work a certain number of hours every month. Employees work in sessions.
# The number of hours an employee worked can be calculated from the sum of the number of minutes the employee worked in all of their sessions.
# The number of minutes in each session is rounded up.
#
# For example, if the employee worked for 51 minutes and 2 seconds in a session, we consider it 52 minutes.
# Write a solution to report the IDs of the employees that will be deducted. In other words, report the IDs of the employees that did not work the needed hours.
#
# Return the result table in any order.
import pandas as pd
import numpy as np

def employees_with_deductions(employees: pd.DataFrame, logs: pd.DataFrame) -> pd.DataFrame:
    logs["sec"] = (logs["out_time"] - logs["in_time"]).dt.total_seconds()
    logs["min"] = np.ceil((logs["sec"] / 60))
    logs["hour"] = (logs["min"] / 60)
    grouped = logs.groupby(by="employee_id", as_index=False).agg(hours=("hour", "sum"))
    merged = pd.merge(
        left=employees,
        right=grouped,
        how="left",
        on="employee_id"
    ).fillna(0)
    return merged.loc[(merged["needed_hours"] > merged["hours"]), ["employee_id"]]


