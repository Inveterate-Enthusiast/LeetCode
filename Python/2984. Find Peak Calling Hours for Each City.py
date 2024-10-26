# Table: Calls
#
# +--------------+----------+
# | Column Name  | Type     |
# +--------------+----------+
# | caller_id    | int      |
# | recipient_id | int      |
# | call_time    | datetime |
# | city         | varchar  |
# +--------------+----------+
# (caller_id, recipient_id, call_time) is the primary key (combination of columns with unique values) for this table.
# Each row contains caller id, recipient id, call time, and city.
# Write a solution to find the peak calling hour for each city.
# If multiple hours have the same number of calls, all of those hours will be recognized as peak hours for that specific city.
#
# Return the result table ordered by peak calling hour and city in descending order.

import pandas as pd

def peak_calling_hours(calls: pd.DataFrame) -> pd.DataFrame:
    calls["peak_calling_hour"] = calls["call_time"].dt.hour
    grouped = calls.groupby(by=["city", "peak_calling_hour"], as_index=False).agg(number_of_calls=("caller_id", "count"))
    grouped["rank"] = grouped.groupby(by="city", as_index=False)["number_of_calls"].rank(method="min", ascending=False)
    return (grouped
            .loc[grouped["rank"] == 1]
            .drop(labels="rank", axis=1)
            .sort_values(by=["peak_calling_hour", "city"], ascending=[False, False]))