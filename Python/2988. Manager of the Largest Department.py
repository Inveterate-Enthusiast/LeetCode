# Table: Employees
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | emp_id      | int     |
# | emp_name    | varchar |
# | dep_id      | int     |
# | position    | varchar |
# +-------------+---------+
# emp_id is column of unique values for this table.
# This table contains emp_id, emp_name, dep_id, and position.
# Write a solution to find the name of the manager from the largest department.
# There may be multiple largest departments when the number of employees in those departments is the same.
#
# Return the result table sorted by dep_id in ascending order.
import pandas as pd

def find_manager(employees: pd.DataFrame) -> pd.DataFrame:
    grouped = employees.groupby(by="dep_id", as_index=False).agg(count=("emp_id", "nunique"))
    merged = pd.merge(
        left=grouped,
        right=employees.loc[employees["position"] == "Manager"].rename(columns={"emp_name": "manager_name"}),
        how="left",
        on="dep_id"
    )
    merged["rank"] = merged["count"].rank(method="dense", ascending=False)
    return merged.loc[merged["rank"] == 1, ["manager_name", "dep_id"]].sort_values(by="dep_id", ascending=True)
