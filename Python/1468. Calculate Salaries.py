# Table Salaries:
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | company_id    | int     |
# | employee_id   | int     |
# | employee_name | varchar |
# | salary        | int     |
# +---------------+---------+
# In SQL,(company_id, employee_id) is the primary key for this table.
# This table contains the company id, the id, the name, and the salary for an employee.
#
#
# Find the salaries of the employees after applying taxes. Round the salary to the nearest integer.
#
# The tax rate is calculated for each company based on the following criteria:
#
# 0% If the max salary of any employee in the company is less than $1000.
# 24% If the max salary of any employee in the company is in the range [1000, 10000] inclusive.
# 49% If the max salary of any employee in the company is greater than $10000.
# Return the result table in any order.
import pandas as pd

def calculate_salaries(salaries: pd.DataFrame) -> pd.DataFrame:
    grouped = salaries.groupby(by="company_id", as_index=False).agg(max=("salary", "max"))
    grouped["tax"] = grouped["max"].apply(lambda x: 0 if x < 1000 else (49 if x > 10_000 else 24))
    merged = pd.merge(
        left=salaries,
        right=grouped,
        how="left",
        on="company_id"
    )
    merged["salary"] = (merged["salary"] - (merged["salary"] * merged["tax"] / 100) + 1e-9).round(0)
    return merged[salaries.columns]

