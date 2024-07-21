# Table: Employee
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | id          | int  |
# | month       | int  |
# | salary      | int  |
# +-------------+------+
# (id, month) is the primary key (combination of columns with unique values) for this table.
# Each row in the table indicates the salary of an employee in one month during the year 2020.
#
# Write a solution to calculate the cumulative salary summary for every employee in a single unified table.
#
# The cumulative salary summary for an employee can be calculated as follows:
#
# For each month that the employee worked, sum up the salaries in that month and the previous two months.
# This is their 3-month sum for that month. If an employee did not work for the company in previous months,
# their effective salary for those months is 0.
# Do not include the 3-month sum for the most recent month that the employee worked for in the summary.
# Do not include the 3-month sum for any month the employee did not work.
# Return the result table ordered by id in ascending order. In case of a tie, order it by month in descending order.
import pandas as pd
from pathlib import Path
import os
from collections import defaultdict

def cumsum(df: pd.DataFrame) -> pd.DataFrame:
    df.sort_values(by="month", ascending=True)
    df["salary"] = df.loc[:, "salary"].rolling(window=3, min_periods=1).sum().fillna(0)
    return df

def cumulative_salary(employee: pd.DataFrame) -> pd.DataFrame:
    months = pd.DataFrame({
        "month": pd.Series(range(1, 12+1, 1))
    })

    months = pd.merge(
        left=months,
        right=employee.loc[:, ["id"]].drop_duplicates(),
        how="cross"
    )

    months = pd.merge(
        left=employee,
        right=months,
        on=["id", "month"],
        how="right"
    ).assign(salary=lambda x: x["salary"].fillna(0))

    months = months.groupby(by="id", as_index=True).apply(cumsum, include_groups=False).reset_index()
    indices = employee.groupby(by="id")["month"].idxmax()

    return pd.merge(
        left=employee.drop(index=indices).loc[:, ["id", "month"]],
        right=months.loc[:, ["id", "month", "salary"]],
        on=["id", "month"],
        how="left"
    ).sort_values(by=["id", "month"], ascending=[True, False])

def cumsum1(df: pd.DataFrame) -> pd.DataFrame:
    our_dict = defaultdict(int)
    for index, row in df.iterrows():
        our_dict[row["month"]] = row["salary"]
        df.loc[index, "salary"] = sum(
         [row["salary"],
          our_dict.get((row["month"]-1), 0),
          our_dict.get((row["month"]-2), 0)]
        )
    return df

def cumulative_salary1(employee: pd.DataFrame) -> pd.DataFrame:
    indices = employee.groupby(by="id")["month"].idxmax()
    grouped = employee.drop(index=indices).groupby(by="id", as_index=True).apply(cumsum1, include_groups=False).reset_index()
    return grouped.loc[:, ["id", "month", "salary"]].sort_values(by=["id", "month"], ascending=[True, False])



path = Path(os.getcwd()) / "data" / "579. Find Cumulative Salary of an Employee.xlsx"
employee = pd.read_excel(path)
print(cumulative_salary1(employee))


