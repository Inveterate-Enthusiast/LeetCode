# Table: Employees
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | employee_id   | int     |
# | employee_name | varchar |
# | manager_id    | int     |
# | salary        | int     |
# +---------------+---------+
# employee_id is the unique identifier for this table.
# manager_id is the employee_id of the employee's manager. The CEO has a NULL manager_id.
# Write a solution to find subordinates of the CEO (both direct and indirect), along with their level in the hierarchy and their salary difference from the CEO.
#
# The result should have the following columns:
#
# The query result format is in the following example.
#
# subordinate_id: The employee_id of the subordinate
# subordinate_name: The name of the subordinate
# hierarchy_level: The level of the subordinate in the hierarchy (1 for direct reports, 2 for their direct reports, and so on)
# salary_difference: The difference between the subordinate's salary and the CEO's salary
# Return the result table ordered by hierarchy_level ascending, and then by subordinate_id ascending.

import pandas as pd
import numpy as np
from collections import deque
from pathlib import Path
import os

def find_subordinates(employees: pd.DataFrame) -> pd.DataFrame:
    ceo_id = employees.loc[employees["manager_id"].isna(), "employee_id"][0]
    ceo_salary = employees.loc[employees["employee_id"] == ceo_id, "salary"][0]

    cur_level = 1
    employees["level"] = np.where(employees["manager_id"].notna() & (employees["manager_id"] == ceo_id), cur_level, pd.NA)
    while employees.loc[(~(employees["employee_id"] == ceo_id)) & (employees["level"].isna())].shape[0] > 0:
        employees["level"] = np.where(
            employees["manager_id"].isin(set(employees.loc[employees["level"].notna() & (employees["level"] == cur_level), "employee_id"])),
            (cur_level := cur_level + 1),
            employees["level"]
        )

    employees["salary_difference"] = employees["salary"] - ceo_salary

    return (employees
            .loc[employees["employee_id"] != ceo_id, ["employee_id", "employee_name", "level", "salary_difference"]]
            .rename(columns={"employee_id": "subordinate_id",
                             "employee_name": "subordinate_name",
                             "level": "hierarchy_level"})
            .sort_values(by=["hierarchy_level", "subordinate_id"], ascending=[True, True]))


def find_subordinates1(employees: pd.DataFrame) -> pd.DataFrame:
    ceo_id = employees.loc[employees["manager_id"].isna(), "employee_id"][0]
    ceo_salary = employees.loc[employees["employee_id"] == ceo_id, "salary"][0]

    cur_level = 1
    employees["level"] = np.where(employees["manager_id"].notna() & (employees["manager_id"] == ceo_id), cur_level, pd.NA)
    queue = deque()
    queue.extend([[i, cur_level] for i in employees.loc[(employees["level"].notna()) & (employees["level"] == cur_level), "employee_id"].tolist()])
    while queue:
        cur_manager, cur_level = queue.popleft()
        employees.loc[(employees["manager_id"].notna()) & (employees["manager_id"] == cur_manager), "level"] = (cur_level := cur_level+1)
        queue.extend([[i, cur_level] for i in employees.loc[(employees["level"].notna()) & (employees["level"] == cur_level), "employee_id"].tolist()])

    employees["salary_difference"] = employees["salary"] - ceo_salary

    return (employees
            .loc[(employees["employee_id"] != ceo_id) & (employees["level"].notna()), ["employee_id", "employee_name", "level", "salary_difference"]]
            .rename(columns={"employee_id": "subordinate_id",
                             "employee_name": "subordinate_name",
                             "level": "hierarchy_level"})
            .sort_values(by=["hierarchy_level", "subordinate_id"], ascending=[True, True]))

employees = pd.read_excel(Path(os.getcwd()) / "data" / "3236. CEO Subordinate Hierarchy.xlsx")
print(find_subordinates1(employees))