# Table: Employee
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | empId       | int     |
# | name        | varchar |
# | supervisor  | int     |
# | salary      | int     |
# +-------------+---------+
# empId is the column with unique values for this table.
# Each row of this table indicates the name and the ID of an employee in addition to their salary and the id of their manager.

# Table: Bonus
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | empId       | int  |
# | bonus       | int  |
# +-------------+------+
# empId is the column of unique values for this table.
# empId is a foreign key (reference column) to empId from the Employee table.
# Each row of this table contains the id of an employee and their respective bonus.

# Write a solution to report the name and bonus amount of each employee with a bonus less than 1000.
#
# Return the result table in any order.
import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    merged_table = pd.merge(
        left = employee,
        right = bonus,
        on = "empId",
        how = "left",
        copy = False,
        suffixes = ("_emp", "_bon")
    )[["name", "bonus"]]
    print(merged_table)
    return merged_table[(merged_table["bonus"] < 1000) | (merged_table["bonus"].isna())]

def employee_bonus1(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    return employee.merge(
        right = bonus,
        on = "empId",
        how = "left"
    ).query("(bonus < 1000) | (bonus.isna())")[["name", "bonus"]]

def employee_bonus2(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(
        left = employee,
        right = bonus,
        on = "empId",
        how = "left",
        copy = False
    )[["name", "bonus"]]
    merged.drop(index=merged[merged["bonus"] >= 1000].index, axis=0, inplace=True)
    return merged

Employee = pd.DataFrame({
    "empId": [3, 1, 2, 4],
    "name": ["Brad", "John", "Dan", "Thomas"],
    "supervisor": [None, 3, 3, 3],
    "salary": [4000, 1000, 2000, 4000]
})

Bonus = pd.DataFrame({
    "empId": [2, 4],
    "bonus": [500, 2000]
})

print(employee_bonus2(Employee, Bonus))