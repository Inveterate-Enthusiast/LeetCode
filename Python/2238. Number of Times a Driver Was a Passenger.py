# Table: Rides
#
# +--------------+------+
# | Column Name  | Type |
# +--------------+------+
# | ride_id      | int  |
# | driver_id    | int  |
# | passenger_id | int  |
# +--------------+------+
# ride_id is the column with unique values for this table.
# Each row of this table contains the ID of the driver and the ID of the passenger that rode in ride_id.
# Note that driver_id != passenger_id.
#
#
# Write a solution to report the ID of each driver and the number of times they were a passenger.
#
# Return the result table in any order.
import pandas as pd

def driver_passenger(rides: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(
        left=rides[["driver_id"]].drop_duplicates(subset="driver_id", keep="first"),
        right=rides[["passenger_id", "ride_id"]],
        how="left",
        left_on="driver_id",
        right_on="passenger_id"
    )
    grouped = merged.groupby(by="driver_id", as_index=False).agg(cnt=("ride_id", "count"))
    return grouped

