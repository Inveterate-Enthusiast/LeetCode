# Table: Calls
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | from_id     | int     |
# | to_id       | int     |
# | duration    | int     |
# +-------------+---------+
# This table does not have a primary key (column with unique values), it may contain duplicates.
# This table contains the duration of a phone call between from_id and to_id.
# from_id != to_id
#
#
# Write a solution to report the number of calls and the total call duration
# between each pair of distinct persons (person1, person2) where person1 < person2.
#
# Return the result table in any order.
import pandas as pd
from pathlib import Path
import os

def number_of_calls(calls: pd.DataFrame) -> pd.DataFrame:
    calls["our_set"] = calls.apply(lambda x: tuple(sorted([x["from_id"], x["to_id"]])), axis=1)
    grouped = calls.groupby(by="our_set", as_index=False).agg(call_count=("duration", "count"), total_duration=("duration", "sum"))
    grouped[["person1", "person2"]] = pd.DataFrame(grouped["our_set"].to_list(), index=grouped.index)
    return grouped[["person1", "person2", "call_count", "total_duration"]]

calls = pd.read_excel(Path(os.getcwd()) / "data" / "1699. Number of Calls Between Two Persons.xlsx")
print(number_of_calls(calls))