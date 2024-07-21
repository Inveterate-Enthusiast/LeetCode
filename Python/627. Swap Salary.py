# Table: Salary
#
# +-------------+----------+
# | Column Name | Type     |
# +-------------+----------+
# | id          | int      |
# | name        | varchar  |
# | sex         | ENUM     |
# | salary      | int      |
# +-------------+----------+
# id is the primary key (column with unique values) for this table.
# The sex column is ENUM (category) value of type ('m', 'f').
# The table contains information about an employee.
import pandas as pd
import numpy as np
from pathlib import Path

def swap_salary(salary: pd.DataFrame) -> pd.DataFrame:
    salary["sex"] = salary["sex"].apply(lambda x: {"f": "m", "m":"f"}.get(x, x))
    return salary

def swap_salary1(salary: pd.DataFrame) -> pd.DataFrame:
    salary["sex"] = salary["sex"].replace({"f": "m", "m":"f"})
    return salary

def swap_salary2(salary: pd.DataFrame) -> pd.DataFrame:
    salary["sex"] = np.where(salary["sex"] == "f", "m", "f")
    return salary

path = Path(__file__).parent / "data" / "627. Salary.xlsx"
salary = pd.read_excel(path)
print(swap_salary2(salary))

