# Table: Project
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | project_id  | int     |
# | employee_id | int     |
# +-------------+---------+
# (project_id, employee_id) is the primary key of this table.
# employee_id is a foreign key to Employee table.
# Each row of this table indicates that the employee with employee_id is working on the project with project_id.

# Table: Employee
#
# +------------------+---------+
# | Column Name      | Type    |
# +------------------+---------+
# | employee_id      | int     |
# | name             | varchar |
# | experience_years | int     |
# +------------------+---------+
# employee_id is the primary key of this table. It's guaranteed that experience_years is not NULL.
# Each row of this table contains information about one employee.

# Write an SQL query that reports the average experience years of all the employees for each project, rounded to 2 digits.
#
# Return the result table in any order.
import pandas as pd
from pathlib import Path

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(
        left=project,
        right=employee,
        on="employee_id",
        how="left",
        copy=False,
        suffixes=("_prod", "_emp")
    )
    return merged.groupby(by="project_id", as_index=False).agg(average_years=("experience_years", "mean")).round(2)

path = Path(__file__).parent / "data" / "1075. Project Employees I.xlsx"
project = pd.read_excel(path, sheet_name="Project")
employee = pd.read_excel(path, sheet_name="Employee")
print(project_employees_i(project, employee))

