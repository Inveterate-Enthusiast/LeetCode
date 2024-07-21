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

# Write a solution to find the nth highest salary from the Employee table. If there is no nth highest salary, return null.
import pandas as pd
from pathlib import Path
import numpy as np

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee.drop_duplicates(subset="salary", inplace=True)

    nth_largest = np.nan if N < 1 else ((employee["salary"].nlargest(N).iloc[-1]) if len(employee) >= N else np.nan)

    return pd.DataFrame({
        f"getNthHighestSalary({N})": [nth_largest]
    })


path = Path(__file__).parent / "data" / "177. Nth Highest Salary.xlsx"
employee = pd.read_excel(path)
N = -1
print(nth_highest_salary(employee, N))
