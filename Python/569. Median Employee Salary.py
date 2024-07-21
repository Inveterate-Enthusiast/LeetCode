# Table: Employee
#
# +--------------+---------+
# | Column Name  | Type    |
# +--------------+---------+
# | id           | int     |
# | company      | varchar |
# | salary       | int     |
# +--------------+---------+
# id is the primary key (column with unique values) for this table.
# Each row of this table indicates the company and the salary of one employee.
#
# Write a solution to find the rows that contain the median salary of each company. While calculating the median,
# when you sort the salaries of the company, break the ties by id.
#
# Return the result table in any order.
import pandas as pd
from pathlib import Path
import os

def grouping(x:pd.DataFrame) -> pd.Series:
    x_max = x["rank"].max()
    if x_max % 2:
        median_salary = x.loc[x["rank"] == ((x_max // 2) + 1), ["id", "salary"]]
    else:
        median_salary = x.loc[x["rank"].isin([
            (x_max // 2),
            ((x_max // 2) + 1)
        ]), ["id", "salary"]]
    return median_salary


def median_employee_salary(employee: pd.DataFrame) -> pd.DataFrame: # решение, которое удовлетворило LeetCode, но не меня
    employee["rank"] = employee.groupby(by="company")["salary"].rank(ascending=True, method="first", na_option="top")
    grouped = employee.groupby(
        by="company", as_index=False
    ).apply(
        func=grouping
    )

    return pd.merge(
        left=grouped,
        right=employee,
        on=["id", "salary"]
    )[["id", "company", "salary"]]


def median_employee_salary1(employee: pd.DataFrame) -> pd.DataFrame: # решение, которое удовлетворило меня, но не LeetCode
    employee["rank"] = employee.groupby(by="company")["salary"].rank(ascending=True, method="first", na_option="top")
    grouped = employee.groupby(
        by="company", as_index=True, group_keys=True
    ).apply(
        func=grouping, include_groups=False
    ).reset_index()

    return grouped[["id", "company", "salary"]]



path = Path(os.getcwd()) / "data" / "569. Median Employee Salary.xlsx"
employee = pd.read_excel(path, sheet_name="Employee")
print(median_employee_salary1(employee))
#