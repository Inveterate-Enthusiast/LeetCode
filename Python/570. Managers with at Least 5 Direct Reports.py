# Table: Employee
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | name        | varchar |
# | department  | varchar |
# | managerId   | int     |
# +-------------+---------+
# id is the primary key (column with unique values) for this table.
# Each row of this table indicates the name of an employee, their department, and the id of their manager.
# If managerId is null, then the employee does not have a manager.
# No employee will be the manager of themself.
#
# Write a solution to find managers with at least five direct reports.
#
# Return the result table in any order.
import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    grouped = employee.groupby(by="managerId", as_index=False).agg(count=("id", lambda x: len(x.unique())))
    return pd.merge(
        left=grouped[grouped["count"] >= 5],
        right=employee.loc[:, ["id", "name"]],
        left_on="managerId",
        right_on="id",
        how="inner"
    ).loc[:, ["name"]]



