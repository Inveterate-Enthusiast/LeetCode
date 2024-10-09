# Table: Tasks
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | task_id     | int  |
# | assignee_id | int  |
# | submit_date | date |
# +-------------+------+
# task_id is the primary key (column with unique values) for this table.
# Each row in this table contains the ID of a task, the id of the assignee, and the submission date.
#
#
# Write a solution to report:
#
# the number of tasks that were submitted during the weekend (Saturday, Sunday) as weekend_cnt, and
# the number of tasks that were submitted during the working days as working_cnt.
# Return the result table in any order.
import pandas as pd

def count_tasks(tasks: pd.DataFrame) -> pd.DataFrame:
    tasks["day_name"] = pd.to_datetime(tasks["submit_date"]).dt.day_name()
    days = {"Saturday", "Sunday"}
    return pd.DataFrame({
        "weekend_cnt": [tasks.loc[tasks["day_name"].isin(days), "task_id"].nunique()],
        "working_cnt": [tasks.loc[~tasks["day_name"].isin(days), "task_id"].nunique()]
    })

