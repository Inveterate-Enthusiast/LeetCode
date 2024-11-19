# Table: employees
#
# +------------------+---------+
# | Column Name      | Type    |
# +------------------+---------+
# | emp_id           | int     |
# | salary           | int     |
# | dept             | varchar |
# +------------------+---------+
# emp_id is the unique key for this table.
# Each row of this table contains information about an employee including their ID, salary, and department.
# Write a solution to find the employees who earn the second-highest salary in each department.
# If multiple employees have the second-highest salary, include all employees with that salary.
#
# Return the result table ordered by emp_id in ascending order.

import pandas as pd

def find_second_highest_salary(employees: pd.DataFrame) -> pd.DataFrame:
    employees["rank"] = employees.groupby(by="dept", as_index=False)["salary"].rank(method="dense", ascending=False)
    return employees.loc[employees["rank"] == 2, ["emp_id", "dept"]].sort_values(by="emp_id", ascending=True)
