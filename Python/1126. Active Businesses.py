# Table: Events
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | business_id   | int     |
# | event_type    | varchar |
# | occurrences   | int     |
# +---------------+---------+
# (business_id, event_type) is the primary key (combination of columns with unique values) of this table.
# Each row in the table logs the info that an event of some type occurred at some business for a number of times.
# The average activity for a particular event_type is the average occurrences across all companies that have this event.
#
# An active business is a business that has more than one event_type such that their occurrences is strictly greater than the average activity for that event.
#
# Write a solution to find all active businesses.
#
# Return the result table in any order.
import pandas as pd

def active_businesses(events: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(
        left=events,
        right=(events.groupby(by="event_type", as_index=False).agg(sum=("occurrences", "sum"), count=("event_type", "count"))),
        on="event_type",
        how="inner",
        copy=False
    )
    merged["bool"] = merged["occurrences"] > (merged["sum"] / merged["count"])
    return merged.groupby(by="business_id", as_index=False).agg(result=("bool", "sum")).query("result > 1")[["business_id"]]

def active_businesses1(events: pd.DataFrame) -> pd.DataFrame:
    events["our_avg"] = events.groupby(by="event_type", as_index=False)["occurrences"].transform("mean")
    events["bool"] = events["occurrences"] > events["our_avg"]
    return events.groupby(by="business_id", as_index=False).agg(result=("bool", "sum")).query("result > 1")[["business_id"]]