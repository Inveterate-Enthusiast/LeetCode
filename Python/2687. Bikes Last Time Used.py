# Table: Bikes
#
# +-------------+----------+
# | Column Name | Type     |
# +-------------+----------+
# | ride_id     | int      |
# | bike_number | int      |
# | start_time  | datetime |
# | end_time    | datetime |
# +-------------+----------+
# ride_id column contains unique values.
# Each row contains a ride information that includes ride_id, bike number, start and end time of the ride.
# Write a solution to find the last time when each bike was used.
#
# Return the result table ordered by the bikes that were most recently used.
import pandas as pd

def last_used_time(bikes: pd.DataFrame) -> pd.DataFrame:
    grouped = bikes.groupby(by="bike_number", as_index=False).agg(end_time=("end_time","max"))
    return grouped.sort_values(by="end_time", ascending=False)

