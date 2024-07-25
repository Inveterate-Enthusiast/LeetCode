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
#
#
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
#
#
# Write a solution to report the most experienced employees in each project. In case of a tie, report all employees with the maximum number of experience years.
#
# Return the result table in any order.
import pandas as pd

def project_employees(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(
        left=project,
        right=employee,
        on="employee_id",
        how="left",
        copy=False
    )
    merged["rank"] = merged.groupby(by="project_id")["experience_years"].rank("min", ascending=False)
    return merged.loc[merged["rank"] == 1, ["project_id", "employee_id"]]
