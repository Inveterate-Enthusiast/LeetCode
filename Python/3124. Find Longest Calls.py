# Table: Contacts
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | first_name  | varchar |
# | last_name   | varchar |
# +-------------+---------+
# id is the primary key (column with unique values) of this table.
# id is a foreign key (reference column) to Calls table.
# Each row of this table contains id, first_name, and last_name.
# Table: Calls
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | contact_id  | int  |
# | type        | enum |
# | duration    | int  |
# +-------------+------+
# (contact_id, type, duration) is the primary key (column with unique values) of this table.
# type is an ENUM (category) type of ('incoming', 'outgoing').
# Each row of this table contains information about calls, comprising of contact_id, type, and duration in seconds.
# Write a solution to find the three longest incoming and outgoing calls.
#
# Return the result table ordered by type, duration, and first_name in descending order and duration must be formatted as HH:MM:SS.
import pandas as pd

def find_longest_calls(contacts: pd.DataFrame, calls: pd.DataFrame) -> pd.DataFrame:
    calls["rank"] = calls.groupby(by="type", as_index=False)["duration"].rank(method="min", ascending=False)
    merged = pd.merge(
        left=calls.loc[calls["rank"] <= 3].rename(columns={"contact_id": "id"}),
        right=contacts,
        how="left",
        on="id"
    )
    merged["duration_formatted"] = pd.to_datetime(merged["duration"], unit="s").dt.time
    return merged[["first_name", "type", "duration_formatted"]].sort_values(by=["type", "duration_formatted", "first_name"], ascending=[False, False, False])

