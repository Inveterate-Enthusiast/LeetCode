# Table: Candidates
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | employee_id | int  |
# | experience  | enum |
# | salary      | int  |
# +-------------+------+
# employee_id is the column with unique values for this table.
# experience is an ENUM (category) of types ('Senior', 'Junior').
# Each row of this table indicates the id of a candidate, their monthly salary, and their experience.
# The salary of each candidate is guaranteed to be unique.
#
#
# A company wants to hire new employees. The budget of the company for the salaries is $70000. The company's criteria for hiring are:
#
# Keep hiring the senior with the smallest salary until you cannot hire any more seniors.
# Use the remaining budget to hire the junior with the smallest salary.
# Keep hiring the junior with the smallest salary until you cannot hire any more juniors.
# Write a solution to find the ids of seniors and juniors hired under the mentioned criteria.
#
# Return the result table in any order.


import pandas as pd
import numpy as np

def number_of_joiners(candidates: pd.DataFrame) -> pd.DataFrame:
    budget = 70_000
    seniors = candidates.loc[candidates["experience"] == "Senior"].sort_values(by="salary", ascending=True)
    seniors = seniors.assign(cum_salary = seniors["salary"].transform("cumsum")).query(f"cum_salary <= {budget}")
    left_budget = budget - ((np.nan_to_num(seniors["cum_salary"].max())) if not seniors.empty else 0)
    juniors = candidates.loc[candidates["experience"] == "Junior"].sort_values(by="salary", ascending=True)
    juniors = juniors.assign(cum_salary = juniors["salary"].transform("cumsum")).query(f"cum_salary <= {left_budget}")
    result = pd.concat([
        seniors[["employee_id"]],
        juniors[["employee_id"]]
    ])
    return result