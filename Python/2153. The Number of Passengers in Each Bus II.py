# Table: Buses
#
# +--------------+------+
# | Column Name  | Type |
# +--------------+------+
# | bus_id       | int  |
# | arrival_time | int  |
# | capacity     | int  |
# +--------------+------+
# bus_id contains unique values.
# Each row of this table contains information about the arrival time of a bus at the LeetCode station and its capacity
# (the number of empty seats it has).
# No two buses will arrive at the same time and all bus capacities will be positive integers.
#
#
# Table: Passengers
#
# +--------------+------+
# | Column Name  | Type |
# +--------------+------+
# | passenger_id | int  |
# | arrival_time | int  |
# +--------------+------+
# passenger_id contains unique values.
# Each row of this table contains information about the arrival time of a passenger at the LeetCode station.
#
#
# Buses and passengers arrive at the LeetCode station. If a bus arrives at the station at a time tbus and
# a passenger arrived at a time tpassenger where tpassenger <= tbus and the passenger did not catch any bus, the passenger will use that bus.
# In addition, each bus has a capacity. If at the moment the bus arrives at the station there are more passengers waiting than
# its capacity capacity, only capacity passengers will use the bus.
#
# Write a solution to report the number of users that used each bus.
#
# Return the result table ordered by bus_id in ascending order.



import pandas as pd
from pathlib import Path
import os

def number_of_passengers(buses: pd.DataFrame, passengers: pd.DataFrame) -> pd.DataFrame:
    merged = (pd.merge(
        left=buses.rename(columns={"arrival_time": "bus_time"}),
        right=passengers.rename(columns={"arrival_time": "pas_time"}),
        how="cross"
    ).query("pas_time <= bus_time")
     .sort_values(by=["bus_time", "pas_time", "bus_id", "passenger_id"], ascending=[True, True, True, True]))
    merged["bool"] = 0
    our_dict = dict()
    our_set = set()
    for index, row in merged.iterrows():
        if (not row["passenger_id"] in our_set) and (our_dict.get(row["bus_id"], 0) + 1 <= row["capacity"]):
            merged.loc[index, "bool"] = 1
            our_dict[row["bus_id"]] = our_dict.get(row["bus_id"], 0) + 1
            our_set.add(row["passenger_id"])
    grouped = merged.loc[merged["bool"] == 1].groupby(by="bus_id", as_index=False).agg(passengers_cnt=("passenger_id", "nunique"))
    result = pd.merge(
        left=buses,
        right=grouped,
        how="left",
        on="bus_id"
    ).fillna(0)
    return result[["bus_id", "passengers_cnt"]].sort_values(by="bus_id", ascending=True)


path = Path(os.getcwd()) / "data" / "2153. The Number of Passengers in Each Bus II.xlsx"
buses = pd.read_excel(path, sheet_name="Buses")
passengers = pd.read_excel(path, sheet_name="Passengers")
print(number_of_passengers(buses, passengers))