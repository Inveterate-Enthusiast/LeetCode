# Table: Employees
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | employee_id   | int     |
# | employee_name | varchar |
# | manager_id    | int     |
# +---------------+---------+
# employee_id is the column of unique values for this table.
# Each row of this table indicates that the employee with ID employee_id and name employee_name reports his work to his/her direct manager with manager_id
# The head of the company is the employee with employee_id = 1.
#
#
# Write a solution to find employee_id of all employees that directly or indirectly report their work to the head of the company.
#
# The indirect relation between managers will not exceed three managers as the company is small.
#
# Return the result table in any order.
import pandas as pd
from pathlib import Path
import os

def find_reporting_people(employees: pd.DataFrame) -> pd.DataFrame:
    our_set = set()
    our_set = our_set.union(set(employees.loc[(employees["manager_id"] == 1) & (employees["employee_id"] != 1), "employee_id"].values))
    our_set = our_set.union(set(employees.loc[employees["manager_id"].isin(our_set), "employee_id"].values))
    our_set = our_set.union(set(employees.loc[employees["manager_id"].isin(our_set), "employee_id"].values))
    return pd.DataFrame({
        "employee_id": list(our_set)
    })

path = Path(os.getcwd()) / "data" / "1270. All People Report to the Given Manager.xlsx"
employees = pd.read_excel(path)
print(find_reporting_people(employees))