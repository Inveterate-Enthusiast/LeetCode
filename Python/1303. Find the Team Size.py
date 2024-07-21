# Table: Employee
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | employee_id   | int     |
# | team_id       | int     |
# +---------------+---------+
# employee_id is the primary key (column with unique values) for this table.
# Each row of this table contains the ID of each employee and their respective team.

# Write a solution to find the team size of each of the employees.
#
# Return the result table in any order.
import pandas as pd

def team_size(employee: pd.DataFrame) -> pd.DataFrame:
    grouped = employee.groupby(by="team_id", as_index=False).agg(team_size=("employee_id", "count"))
    return pd.merge(
        left=employee,
        right=grouped,
        how="left",
        on="team_id",
    )[["employee_id", "team_size"]]

def team_size1(employee: pd.DataFrame) -> pd.DataFrame:
    employee["team_size"] = employee["team_id"].apply(lambda x: (employee["team_id"] == x).sum())
    return employee[["employee_id", "team_size"]]
