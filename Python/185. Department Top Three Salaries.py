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
# departmentId is a foreign key (reference column) of the ID from the Department table.
# Each row of this table indicates the ID, name, and salary of an employee. It also contains the ID of their department.
#
# Table: Department
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | name        | varchar |
# +-------------+---------+
# id is the primary key (column with unique values) for this table.
# Each row of this table indicates the ID of a department and its name.
#
# A company's executives are interested in seeing who earns the most money in each of the company's departments.
# A high earner in a department is an employee who has a salary in the top three unique salaries for that department.
#
# Write a solution to find the employees who are high earners in each of the departments.
#
# Return the result table in any order.
import pandas as pd
from pathlib import Path
import os

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    grouped = employee.groupby(by="departmentId", as_index=False).agg(our_set=("salary", lambda x: set(sorted(x.unique(), reverse=True)[:2+1])))
    grouped = grouped.merge(right=department, left_on="departmentId", right_on="id").drop(columns=["id"]).rename(columns={"name": "Department"})
    merged = pd.merge(
        left=employee.rename(columns={"name": "Employee", "salary": "Salary"}),
        right=grouped,
        on="departmentId",
        how="inner",
        suffixes=("_emp", "_dep"),
        copy=False
    )
    
    return merged[
        merged.apply(lambda x: x["Salary"] in x["our_set"], axis=1)
    ].sort_values(by="Salary", ascending=False)[["Department", "Employee", "Salary"]]

def top_three_salaries1(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    employee["salary_rank"] = employee.groupby(by="departmentId", as_index=False)["salary"].rank(ascending=False, method="dense")
    return pd.merge(
        left=employee[
            employee["salary_rank"].isin(list([1, 2, 3]))
        ].rename(columns={
            "name": "Employee",
            "salary": "Salary"
        }),
        right=department.rename(columns={
            "id": "departmentId",
            "name": "Department"
        }),
        on="departmentId",
        how="left"
    ).sort_values(by="Salary", ascending=False)[["Department", "Employee", "Salary"]]

path = Path(os.getcwd()) / "data" / "185. Department Top Three Salaries.xlsx"
employee = pd.read_excel(path, sheet_name="Employee")
department = pd.read_excel(path, sheet_name="Department")
print(top_three_salaries1(employee, department))