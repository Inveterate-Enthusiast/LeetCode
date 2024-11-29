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
# experience is an ENUM (category) type of values ('Senior', 'Junior').
# Each row of this table indicates the id of a candidate, their monthly salary, and their experience.
#
#
# A company wants to hire new employees. The budget of the company for the salaries is $70000. The company's criteria for hiring are:
#
# Hiring the largest number of seniors.
# After hiring the maximum number of seniors, use the remaining budget to hire the largest number of juniors.
# Write a solution to find the number of seniors and juniors hired under the mentioned criteria.
#
# Return the result table in any order.

import pandas as pd
import numpy as np
from pathlib import Path
import os

def count_seniors_and_juniors(candidates: pd.DataFrame) -> pd.DataFrame:
    budget = 70_000
    seniors = candidates.loc[candidates["experience"] == "Senior"].copy().sort_values(by="salary", ascending=True)
    seniors["cumsum"] = seniors["salary"].transform("cumsum")
    seniors = seniors.loc[seniors["cumsum"] <= budget]
    left_budget = budget - (np.nan_to_num(seniors["cumsum"].max(), nan=0) if seniors.shape[0] > 0 else 0)
    juniors = candidates.loc[candidates["experience"] == "Junior"].copy().sort_values(by="salary", ascending=True)
    juniors["cumsum"] = juniors["salary"].transform("cumsum")
    juniors = juniors.loc[juniors["cumsum"] <= left_budget]
    return pd.DataFrame({
        "experience": ["Senior", "Junior"],
        "accepted_candidates": [seniors["employee_id"].nunique(), juniors["employee_id"].nunique()]
    })

def count_seniors_and_juniors1(candidates: pd.DataFrame) -> pd.DataFrame:
    budget = 70_000
    seniors = candidates.loc[candidates["experience"] == "Senior"].copy().sort_values(by="salary", ascending=True)
    seniors = seniors.assign(cumsum = seniors["salary"].transform("cumsum")).query(f"cumsum <= {budget}")
    juniors = candidates.loc[candidates["experience"] == "Junior"].copy().sort_values(by="salary", ascending=True)
    left_budget = budget - (np.nan_to_num(seniors["cumsum"].max()) if not seniors.empty else 0)
    juniors = juniors.assign(cumsum = juniors["salary"].transform("cumsum")).query(f"cumsum <= {left_budget}")
    return pd.DataFrame({
        "experience": ["Senior", "Junior"],
        "accepted_candidates": [seniors["employee_id"].nunique(), juniors["employee_id"].nunique()]
    })

candidates = pd.read_excel(Path(os.getcwd()) / "data" / "2004. The Number of Seniors and Juniors to Join the Company.xlsx", sheet_name="Candidates")
print(count_seniors_and_juniors1(candidates))