# Table: Failed
#
# +--------------+---------+
# | Column Name  | Type    |
# +--------------+---------+
# | fail_date    | date    |
# +--------------+---------+
# fail_date is the primary key (column with unique values) for this table.
# This table contains the days of failed tasks.
#
#
# Table: Succeeded
#
# +--------------+---------+
# | Column Name  | Type    |
# +--------------+---------+
# | success_date | date    |
# +--------------+---------+
# success_date is the primary key (column with unique values) for this table.
# This table contains the days of succeeded tasks.
#
#
# A system is running one task every day. Every task is independent of the previous tasks. The tasks can fail or succeed.
#
# Write a solution to report the period_state for each continuous interval of days in the period from 2019-01-01 to 2019-12-31.
#
# period_state is 'failed' if tasks in this interval failed or 'succeeded' if tasks in this interval succeeded.
# Interval of days are retrieved as start_date and end_date.
#
# Return the result table ordered by start_date.
import pandas as pd
from pathlib import Path
import os

def report_contiguous_dates(failed: pd.DataFrame, succeeded: pd.DataFrame) -> pd.DataFrame:
    failed = failed.loc[(failed["fail_date"] >= pd.Timestamp(year=2019, month=1, day=1)) & (failed["fail_date"] <= pd.Timestamp(year=2019, month=12, day=31))].sort_values(by="fail_date", ascending=True)
    succeeded = succeeded.loc[(succeeded["success_date"] >= pd.Timestamp(year=2019, month=1, day=1)) & (succeeded["success_date"] <= pd.Timestamp(year=2019, month=12, day=31))].sort_values(by="success_date", ascending=True)
    result = pd.DataFrame({
        "period_state": [],
        "start_date": [],
        "end_date": []
    })
    i = j = 0
    while i < failed.shape[0] or j < succeeded.shape[0]:
        if (i < failed.shape[0]) and ((not j < succeeded.shape[0]) or (failed.iloc[i, 0] < succeeded.iloc[j, 0])):
            if result.empty or result.iloc[result.shape[0] - 1]["period_state"] != "failed":
                result.loc[result.shape[0], "period_state"] = "failed"
                result.loc[result.shape[0] - 1, "start_date"] = failed.iloc[i, 0].strftime("%Y-%m-%d")
            result.loc[result.shape[0] - 1, "end_date"] = failed.iloc[i, 0].strftime("%Y-%m-%d")
            i += 1
        else:
            if result.empty or result.iloc[result.shape[0] - 1]["period_state"] != "succeeded":
                result.loc[result.shape[0], "period_state"] = "succeeded"
                result.loc[result.shape[0] - 1, "start_date"] = succeeded.iloc[j, 0].strftime("%Y-%m-%d")
            result.loc[result.shape[0] - 1, "end_date"] = succeeded.iloc[j, 0].strftime("%Y-%m-%d")
            j += 1

    return result


path = Path(os.getcwd()) / "data" / "1225. Report Contiguous Dates.xlsx"
failed = pd.read_excel(path, sheet_name="Failed")
succeeded = pd.read_excel(path, sheet_name="Succeeded")
print(report_contiguous_dates(failed, succeeded))