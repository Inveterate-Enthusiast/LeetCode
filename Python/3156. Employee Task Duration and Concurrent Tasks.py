# Write a solution to find the total duration of tasks for each employee
# and the maximum number of concurrent tasks an employee handled at any point in time.
# The total duration should be rounded down to the nearest number of full hours.
#
# Return the result table ordered by employee_id ascending order.

import pandas as pd
import numpy as np

def find_total_duration(tasks: pd.DataFrame) -> pd.DataFrame:
    tasks["duration"] = (tasks["end_time"] - tasks["start_time"]).dt.total_seconds()
    tasks.sort_values(by=["start_time", "end_time"], ascending=[True, True], inplace=True)
    tasks["prev_end"] = tasks.groupby(by="employee_id", as_index=False)["end_time"].shift(1)
    tasks["overlap"] = (tasks["prev_end"] - tasks["start_time"]).dt.total_seconds()
    tasks["duration"] = np.where(tasks["overlap"] > 0, tasks["duration"] - tasks["overlap"], tasks["duration"])
    grouped = tasks.groupby(by="employee_id", as_index=False).agg(total_seconds=("duration", "sum"))
    grouped["total_task_hours"] = np.floor(grouped["total_seconds"] / (60**2) + 1e-9)

    concated = pd.concat([
        tasks.assign(change = 1)[["employee_id", "task_id", "start_time", "change"]].rename(columns={"start_time": "time"}),
        tasks.assign(change = -1)[["employee_id", "task_id", "end_time", "change"]].rename(columns={"end_time": "time"})
    ]).sort_values(by=["time", "task_id", "change"], ascending=[True, True, False])
    concated["active_tasks"] = concated.groupby(by="employee_id", as_index=False)["change"].cumsum()
    grouped_1 = concated.groupby(by="employee_id", as_index=False).agg(max_concurrent_tasks=("active_tasks", "max"))
    merged = pd.merge(
        left=grouped,
        right=grouped_1,
        how="inner",
        on="employee_id"
    )
    return merged.sort_values(by="employee_id", ascending=True)[["employee_id", "total_task_hours", "max_concurrent_tasks"]]