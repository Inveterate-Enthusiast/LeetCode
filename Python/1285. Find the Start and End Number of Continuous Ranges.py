# Table: Logs
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | log_id        | int     |
# +---------------+---------+
# log_id is the column of unique values for this table.
# Each row of this table contains the ID in a log Table.
#
#
# Write a solution to find the start and end number of continuous ranges in the table Logs.
#
# Return the result table ordered by start_id.
import pandas as pd
from pathlib import Path
import os

def find_continuous_ranges(logs: pd.DataFrame) -> pd.DataFrame:
    result = pd.DataFrame({
        "start_id": list(),
        "end_id": list()
    })

    logs.sort_values(by="log_id", ascending=True, inplace=True)

    i = 0
    while i < logs.shape[0]:
        if not result.empty and i < logs.shape[0] and (logs.iloc[i, 0] - result.loc[result.shape[0] - 1, "end_id"]) == 1:
            result.loc[result.shape[0] - 1, "end_id"] = logs.iloc[i, 0]
        else:
            result.loc[result.shape[0], "start_id"] = logs.iloc[i, 0]
            result.loc[result.shape[0] - 1, "end_id"] = logs.iloc[i, 0]
        i += 1

    return result

path = Path(os.getcwd()) / "data" / "1285. Find the Start and End Number of Continuous Ranges.xlsx"
logs = pd.read_excel(path)
print(find_continuous_ranges(logs))