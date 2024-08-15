# Table: Salary
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | emp_id        | int     |
# | firstname     | varchar |
# | lastname      | varchar |
# | salary        | varchar |
# | department_id | varchar |
# +---------------+---------+
# (emp_id, salary) is the primary key (combination of columns with unique values) for this table.
# Each row contains employees details and their yearly salaries, however,
# some of the records are old and contain outdated salary information.
# Write a solution to find the current salary of each employee assuming that salaries increase each year.
# Output their emp_id, firstname, lastname, salary, and department_id.
#
# Return the result table ordered by emp_id in ascending order.
import pandas as pd

def find_latest_salaries(salary: pd.DataFrame) -> pd.DataFrame:
    salary["our_rank"] = salary.groupby(by="emp_id", as_index=False)["salary"].rank(method="dense", ascending=False)
    return salary.loc[salary["our_rank"] == 1, ["emp_id", "firstname", "lastname", "salary", "department_id"]].sort_values(by="emp_id", ascending=True)

def find_latest_salaries1(salary: pd.DataFrame) -> pd.DataFrame:
    return salary.sort_values(by=["emp_id", "salary"], ascending=[True, False]).drop_duplicates(subset="emp_id", keep="first")