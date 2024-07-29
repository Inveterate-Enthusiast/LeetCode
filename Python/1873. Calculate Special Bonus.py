# Table: Employees
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | employee_id | int     |
# | name        | varchar |
# | salary      | int     |
# +-------------+---------+
# employee_id is the primary key (column with unique values) for this table.
# Each row of this table indicates the employee ID, employee name, and salary.
#
#
# Write a solution to calculate the bonus of each employee.
# The bonus of an employee is 100% of their salary if the ID of the employee is an odd number
# and the employee's name does not start with the character 'M'.
# The bonus of an employee is 0 otherwise.
#
# Return the result table ordered by employee_id.
import pandas as pd


def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees["bonus"] = employees.apply(lambda x: x["salary"] if (x["employee_id"]%2) and (x["name"][0] != "M") else 0, axis=1)
    return employees.sort_values(by="employee_id", ascending=True).loc[:, ["employee_id", "bonus"]]