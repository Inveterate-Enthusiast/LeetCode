# Table: Employees
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | employee_id | int     |
# | name        | varchar |
# | salary      | int     |
# +-------------+---------+
# employee_id is the column with unique values for this table.
# Each row of this table indicates the employee ID, employee name, and salary.
#
#
# A company wants to divide the employees into teams such that all the members on each team have the same salary. The teams should follow these criteria:
#
# Each team should consist of at least two employees.
# All the employees on a team should have the same salary.
# All the employees of the same salary should be assigned to the same team.
# If the salary of an employee is unique, we do not assign this employee to any team.
# A team's ID is assigned based on the rank of the team's salary relative to the other teams' salaries,
# where the team with the lowest salary has team_id = 1. Note that the salaries for employees not on a team are not included in this ranking.
# Write a solution to get the team_id of each employee that is in a team.
#
# Return the result table ordered by team_id in ascending order. In case of a tie, order it by employee_id in ascending order.
import pandas as pd

def employees_of_same_salary(employees: pd.DataFrame) -> pd.DataFrame:
    grouped_salary = employees.groupby(by="salary", as_index=False).agg(count=("salary", "count"))
    merged = pd.merge(
        left=employees,
        right=grouped_salary,
        how="left",
        on="salary"
    )
    filtered = merged.loc[merged["count"] >= 2].copy()
    filtered["team_id"] = filtered["salary"].rank(method="dense", ascending=True)
    return filtered.drop(labels="count", axis=1).sort_values(by=["team_id", "employee_id"], ascending=[True, True])

def employees_of_same_salary1(employees: pd.DataFrame) -> pd.DataFrame:
    employees["count"] = employees.groupby(by="salary", as_index=False)["employee_id"].transform("count")
    filtered = employees.loc[employees["count"] >= 2].copy()
    filtered["team_id"] = filtered["salary"].rank(method="dense", ascending=True)
    return filtered.drop(labels="count", axis=1).sort_values(by=["team_id", "employee_id"], ascending=[True, True])