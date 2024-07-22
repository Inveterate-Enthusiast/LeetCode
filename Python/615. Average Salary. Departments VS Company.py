# Table: Salary
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | id          | int  |
# | employee_id | int  |
# | amount      | int  |
# | pay_date    | date |
# +-------------+------+
# In SQL, id is the primary key column for this table.
# Each row of this table indicates the salary of an employee in one month.
# employee_id is a foreign key (reference column) from the Employee table.
#
#
# Table: Employee
#
# +---------------+------+
# | Column Name   | Type |
# +---------------+------+
# | employee_id   | int  |
# | department_id | int  |
# +---------------+------+
# In SQL, employee_id is the primary key column for this table.
# Each row of this table indicates the department of an employee.
#
#
# Find the comparison result (higher/lower/same) of the average salary of employees in a department to the company's average salary.
#
# Return the result table in any order.
import pandas as pd
from pathlib import Path
import os
import numpy as np

def average_salary(salary: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    salary["pay_month"] = salary["pay_date"].dt.strftime("%Y-%m")
    gr_avg_comp = salary.groupby(by="pay_month", as_index=False).agg(avg=("amount", "mean"))
    gr_avg_dep = pd.merge(
        left=salary,
        right=employee,
        how="left",
        on="employee_id",
        copy=False
    ).groupby(by=["pay_month", "department_id"], as_index=False).agg(avg=("amount", "mean"))

    general = pd.merge(
        left=gr_avg_dep,
        right=gr_avg_comp,
        how="inner",
        on="pay_month",
        suffixes=("_dep", "_comp")
    )
    general["comparison"] = np.where(general["avg_dep"] > general["avg_comp"], "higher",
                                     (np.where(general["avg_dep"] < general["avg_comp"], "lower",
                                               "same")))

    return general.loc[:, ["pay_month", "department_id", "comparison"]]


path = Path(os.getcwd()) / "data" / "615. Average Salary. Departments VS Company.xlsx"
salary = pd.read_excel(path, sheet_name="Salary")
employee = pd.read_excel(path, sheet_name="Employee")
print(average_salary(salary, employee))