# Table: Employees
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | employee_id | int     |
# | name        | varchar |
# +-------------+---------+
# employee_id is the column with unique values for this table.
# Each row of this table indicates the name of the employee whose ID is employee_id.
#
#
# Table: Salaries
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | employee_id | int     |
# | salary      | int     |
# +-------------+---------+
# employee_id is the column with unique values for this table.
# Each row of this table indicates the salary of the employee whose ID is employee_id.
#
#
# Write a solution to report the IDs of all the employees with missing information. The information of an employee is missing if:
#
# The employee's name is missing, or
# The employee's salary is missing.
# Return the result table ordered by employee_id in ascending order.
import pandas as pd

def find_employees(employees: pd.DataFrame, salaries: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(
        left=employees,
        right=salaries,
        on="employee_id",
        how="outer",
        copy=False
    )
    return merged.loc[(merged["name"].isna()) | (merged["salary"].isna()), ["employee_id"]].sort_values(by="employee_id", ascending=True)
