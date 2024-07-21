# Table: Employees
#
# +-------------+----------+
# | Column Name | Type     |
# +-------------+----------+
# | employee_id | int      |
# | name        | varchar  |
# | reports_to  | int      |
# | age         | int      |
# +-------------+----------+
# employee_id is the column with unique values for this table.
# This table contains information about the employees and the id of the manager they report to. Some employees do not report to anyone (reports_to is null).
#
#
# For this problem, we will consider a manager an employee who has at least 1 other employee reporting to them.
#
# Write a solution to report the ids and the names of all managers, the number of employees who report directly to them, and the average age of the reports rounded to the nearest integer.
#
# Return the result table ordered by employee_id.
import pandas as pd
from math import modf

def count_employees(employees: pd.DataFrame) -> pd.DataFrame:
    grouped = (employees
               .groupby(
        by="reports_to",
        as_index=False,
        dropna=True)
               .agg(
        reports_count=("employee_id", "nunique"),
        average_age=("age", lambda x: round(x.mean()+1e-10, 0)))
               .rename(columns={"reports_to": "employee_id"}))
    return grouped.merge(
        right=employees.loc[:, ["employee_id", "name"]],
        on="employee_id"
    ).loc[:,["employee_id", "name", "reports_count", "average_age"]]

