# Table: Employee
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | id          | int  |
# | salary      | int  |
# +-------------+------+
# id is the primary key (column with unique values) for this table.
# Each row of this table contains information about the salary of an employee.

# Write a solution to find the second highest salary from the Employee table.
# If there is no second highest salary, return null (return None in Pandas).
import pandas as pd
from pathlib import Path
import numpy as np

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee.drop_duplicates(subset="salary", inplace=True)

    if len(employee) < 2:
        return pd.DataFrame({
            "SecondHighestSalary": [np.nan]
        })

    employee.sort_values(by="salary", inplace=True, na_position="first", ascending=False)

    return pd.DataFrame({
        "SecondHighestSalary": [employee.iloc[1]["salary"]]
    })

def second_highest_salary1(employee: pd.DataFrame) -> pd.DataFrame:
    employee.drop_duplicates(subset="salary", inplace=True)

    our_lambda = lambda x: employee[employee["salary"] < x]["salary"].max() if employee["salary"].lt(x).any() else np.nan

    employee["SecondHighestSalary"] = employee["salary"].apply(our_lambda)

    return employee[employee["salary"] == employee["salary"].max()][["SecondHighestSalary"]]

def second_highest_salary2(employee: pd.DataFrame) -> pd.DataFrame:
    employee.drop_duplicates(subset="salary", inplace=True)
    second_largest = employee["salary"].nlargest(2).iloc[-1] if len(employee) >= 2 else np.nan
    return pd.DataFrame({
        "SecondHighestSalary": [second_largest]
    })

path = Path(__file__).parent / "data" / "176. Second Highest Salary.xlsx"
employee = pd.read_excel(path)
print(second_highest_salary2(employee))



