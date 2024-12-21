# Table: Project
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | project_id  | int     |
# | employee_id | int     |
# | workload    | int     |
# +-------------+---------+
# employee_id is the primary key (column with unique values) of this table.
# employee_id is a foreign key (reference column) to Employee table.
# Each row of this table indicates that the employee with employee_id is working on the project with project_id and the workload of the project.
# Table: Employees
#
# +------------------+---------+
# | Column Name      | Type    |
# +------------------+---------+
# | employee_id      | int     |
# | name             | varchar |
# | team             | varchar |
# +------------------+---------+
# employee_id is the primary key (column with unique values) of this table.
# Each row of this table contains information about one employee.
# Write a solution to find the employees who are allocated to projects with a workload
# that exceeds the average workload of all employees for their respective teams
#
# Return the result table ordered by employee_id, project_id in ascending order.


import pandas as pd

def employees_with_above_avg_workload(project: pd.DataFrame, employees: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(
        left=project,
        right=employees,
        how="left",
        on="employee_id",
    )
    merged["avg"] = merged.groupby(by="team", as_index=False)["workload"].transform("mean")
    return (merged
            .loc[merged["workload"] > merged["avg"], ["employee_id", "project_id", "name", "workload"]]
            .rename(columns={"name": "employee_name", "workload": "project_workload"})
            .sort_values(by=["employee_id", "project_id"], ascending=[True, True]))
