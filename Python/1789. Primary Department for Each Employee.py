# Table: Employee
#
# +---------------+---------+
# | Column Name   |  Type   |
# +---------------+---------+
# | employee_id   | int     |
# | department_id | int     |
# | primary_flag  | varchar |
# +---------------+---------+
# (employee_id, department_id) is the primary key (combination of columns with unique values) for this table.
# employee_id is the id of the employee.
# department_id is the id of the department to which the employee belongs.
# primary_flag is an ENUM (category) of type ('Y', 'N'). If the flag is 'Y',
# the department is the primary department for the employee. If the flag is 'N', the department is not the primary.
#
#
# Employees can belong to multiple departments. When the employee joins other departments,
# they need to decide which department is their primary department. Note that when an employee belongs to only one department,
# their primary column is 'N'.
#
# Write a solution to report all the employees with their primary department. For employees who belong to one department,
# report their only department.
#
# Return the result table in any order.
import pandas as pd

def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    prim = employee.loc[employee["primary_flag"] == "Y"]
    prim_set = set(prim["employee_id"])
    not_prim = employee.loc[~employee["employee_id"].isin(prim_set)].groupby(by="employee_id", as_index=False).agg(department_id=("department_id", lambda x: x if len(x) == 1 else None)).query("~department_id.isna()")
    return pd.concat([
        prim[["employee_id", "department_id"]],
        not_prim
    ])

def find_primary_department1(employee: pd.DataFrame) -> pd.DataFrame:
    employee["our_rank"] = employee.groupby(by="employee_id", as_index=False)["primary_flag"].rank(method="dense", ascending=False)
    employee["bool"] = employee.groupby(by="employee_id", as_index=False)["primary_flag"].transform(lambda x: True if len(x) == 1 or "Y" in set(x) else False)
    return employee.loc[(employee["our_rank"] == 1) & employee["bool"] == True, ["employee_id", "department_id"]]