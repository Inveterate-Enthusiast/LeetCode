# Table: Employees
#
# +-------------+----------+
# | Column Name | Type     |
# +-------------+----------+
# | employee_id | int      |
# | name        | varchar  |
# | manager_id  | int      |
# | salary      | int      |
# +-------------+----------+
# In SQL, employee_id is the primary key for this table.
# This table contains information about the employees, their salary, and the ID of their manager. Some employees do not have a manager (manager_id is null).
#
#
# Find the IDs of the employees whose salary is strictly less than $30000 and whose manager left the company.
# When a manager leaves the company, their information is deleted from the Employees table,
# but the reports still have their manager_id set to the manager that left.
#
# Return the result table ordered by employee_id.
import pandas as pd

def find_employees(employees: pd.DataFrame) -> pd.DataFrame:
    return pd.merge(
        left=employees.loc[(employees["salary"] < 30_000) & (~employees["manager_id"].isna()),
                            ["employee_id", "manager_id", "salary"]],
        right=employees.loc[:, ["employee_id", "name"]].rename(columns={"employee_id": "manager_id"}),
        on="manager_id",
        how="left"
    ).query("name.isna()").sort_values(by="employee_id", ascending=True)[["employee_id"]]
