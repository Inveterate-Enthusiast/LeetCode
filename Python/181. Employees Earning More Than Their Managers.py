# Table: Employee
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | name        | varchar |
# | salary      | int     |
# | managerId   | int     |
# +-------------+---------+
# id is the primary key (column with unique values) for this table.
# Each row of this table indicates the ID of an employee, their name, salary, and the ID of their manager.

# Write a solution to find the employees who earn more than their managers.
# Return the result table in any order.

import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    mergedDF = pd.merge(
        employee,
        employee,
        how = "right",
        left_on = "managerId",
        right_on = "id",
        suffixes = ("_e", "_m")
    )
    return mergedDF[mergedDF["salary_e"] > mergedDF["salary_m"]][["name_e"]].rename(columns={
        "name_e": "Employee"
    })

def find_employees1(employee: pd.DataFrame) -> pd.DataFrame:
    mSalery = employee[["managerId"]].copy()
    mSalery["salary"] = mSalery["managerId"].map(employee.set_index("id")["salary"], na_action="ignore")
    mSalery.dropna(subset=["managerId"], inplace=True)
    mSalery.drop_duplicates(subset=["managerId"], inplace=True, keep='first')
    print(mSalery)
    employee = pd.merge(left=employee, right=mSalery, on="managerId", suffixes=("_e", "_m"), how="inner")
    return employee[employee["salary_e"] > employee["salary_m"]][["name"]].rename(columns={"name": "Employee"})

def find_employees2(employee: pd.DataFrame) -> pd.DataFrame:
    result_df = employee[employee["salary"] > employee["managerId"].map(employee.set_index("id")["salary"])]
    return result_df[["name"]].rename(columns={"name": "Employee"})

Employee = pd.DataFrame({
    "id": [1, 2, 3, 4],
    "name": ["Joe", "Henry", "Sam", "Max"],
    "salary": [70_000, 80_000, 60_000, 90_000],
    "managerId": [3, 4, None, None]
})

# Employee = pd.DataFrame({
#     "id": [1, 3, 2],
#     "name": ["Joe", "Henry", "Sam"],
#     "salary": [40_000, 30_000, 20_000],
#     "managerId": [2, 2, None]
# })

# print(Employee["managerId"].map(Employee.set_index("id")["salary"]))

print(find_employees2(Employee))