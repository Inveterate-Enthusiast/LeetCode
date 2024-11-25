# Table: Tasks
#
# +----------------+---------+
# | Column Name    | Type    |
# +----------------+---------+
# | task_id        | int     |
# | subtasks_count | int     |
# +----------------+---------+
# task_id is the column with unique values for this table.
# Each row in this table indicates that task_id was divided into subtasks_count subtasks labeled from 1 to subtasks_count.
# It is guaranteed that 2 <= subtasks_count <= 20.
#
#
# Table: Executed
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | task_id       | int     |
# | subtask_id    | int     |
# +---------------+---------+
# (task_id, subtask_id) is the combination of columns with unique values for this table.
# Each row in this table indicates that for the task task_id, the subtask with ID subtask_id was executed successfully.
# It is guaranteed that subtask_id <= subtasks_count for each task_id.
#
#
# Write a solution to report the IDs of the missing subtasks for each task_id.
#
# Return the result table in any order.

import pandas as pd

def find_subtasks(tasks: pd.DataFrame, executed: pd.DataFrame) -> pd.DataFrame:
    tasks["set_origin"] = tasks["subtasks_count"].apply(lambda x: set(range(1, x+1, 1)))
    grouped = executed.groupby(by="task_id", as_index=False).agg(set=("subtask_id", lambda x: set(x)))
    merged = pd.merge(
        left=tasks,
        right=grouped,
        how="left",
        on="task_id"
    )
    merged["missing"] = merged.apply(lambda x: list(x["set_origin"].difference(x["set"])) if pd.notna(x["set"]) else list(x["set_origin"]), axis=1)
    result = merged[["task_id", "missing"]].explode("missing", ignore_index=True)
    return result.loc[~result["missing"].isna()].rename(columns={"missing": "subtask_id"})