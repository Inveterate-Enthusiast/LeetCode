# Table: Project
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | project_id  | int     |
# | employee_id | int     |
# +-------------+---------+
# (project_id, employee_id) is the primary key (combination of columns with unique values) of this table.
# employee_id is a foreign key (reference column) to Employee table.
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
# employee_id is the primary key (column with unique values) of this table.
# Each row of this table contains information about one employee.

# Write a solution to report all the projects that have the most employees.
#
# Return the result table in any order.
import pandas as pd
from pathlib import Path

def project_employees_ii(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    grouped = project.groupby(by="project_id", as_index=False).agg(count=("employee_id", "size"))
    return grouped[grouped["count"] == grouped["count"].max()][["project_id"]]

path = Path(__file__).parent / "data" / "1076. Project Employees II.xlsx"
project = pd.read_excel(path, sheet_name="Project")
employee = pd.read_excel(path, sheet_name="Employee")
print(project_employees_ii(project, employee))

