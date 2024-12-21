# Table: HallEvents
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | hall_id     | int  |
# | start_day   | date |
# | end_day     | date |
# +-------------+------+
# This table may contain duplicates rows.
# Each row of this table indicates the start day and end day of an event and the hall in which the event is held.
#
#
# Write a solution to merge all the overlapping events that are held in the same hall. Two events overlap if they have at least one day in common.
#
# Return the result table in any order.
from heapq import merge

import pandas as pd
import numpy as np
from pathlib import Path
import os

def merge_events(hall_events: pd.DataFrame) -> pd.DataFrame:
    hall_events.sort_values(by=["hall_id", "start_day", "end_day"], ascending=[True, True, True], inplace=True)
    hall_events["end_prev"] = hall_events.groupby(by="hall_id", as_index=False)["end_day"].shift(1)
    hall_events["end_prev_max"] = hall_events.groupby(by="hall_id", as_index=False)["end_prev"].cummax()
    hall_events["bool"] = np.where(hall_events["end_prev_max"].isna()
                                   |
                                   (hall_events["start_day"] > hall_events["end_prev_max"]),
                                   1, 0)
    hall_events["group"] = hall_events.groupby(by="hall_id", as_index=False)["bool"].cumsum()
    return (hall_events
            .groupby(by=["hall_id", "group"], as_index=False)
            .agg(start_day=("start_day", "min"),
                 end_day=("end_day", "max"))
            .drop(labels="group", axis=1))

hall_events = pd.read_excel(Path(os.getcwd()) / "data" / "2494. Merge Overlapping Events in the Same Hall.xlsx", sheet_name="HallEvents")
print(merge_events(hall_events).to_string())