# Table: Employee
#
# +--------------+---------+
# | Column Name  | Type    |
# +--------------+---------+
# | id           | int     |
# | name         | varchar |
# | salary       | int     |
# | departmentId | int     |
# +--------------+---------+
# id is the primary key (column with unique values) for this table.
# departmentId is a foreign key (reference columns) of the ID from the Department table.
# Each row of this table indicates the ID, name, and salary of an employee. It also contains the ID of their department.
#
#
# Table: Department
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | name        | varchar |
# +-------------+---------+
# id is the primary key (column with unique values) for this table. It is guaranteed that department name is not NULL.
# Each row of this table indicates the ID of a department and its name.
#
#
# Write a solution to find employees who have the highest salary in each of the departments.
#
# Return the result table in any order.
import pandas as pd
from pathlib import Path
import os


def get_max_salary(df: pd.DataFrame) -> pd.DataFrame:
    return df.loc[
        (df["salary"] == df["salary"].max()),
        ["name", "salary"]]


def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    grouped = employee.groupby(by="departmentId", as_index=True, dropna=False).apply(get_max_salary, include_groups=False).reset_index()
    return pd.merge(
        left=grouped.rename(columns={"name": "Employee", "salary": "Salary"}),
        right=department.rename(columns={"name": "Department"}),
        left_on="departmentId",
        right_on="id",
        how="left"
    ).loc[:, ["Department", "Employee", "Salary"]]

path = Path(os.getcwd()) / "data" / "184. Department Highest Salary.xlsx"
employee = pd.read_excel(path, sheet_name="Employee")
department = pd.read_excel(path, sheet_name="Department")
print(department_highest_salary(employee, department))