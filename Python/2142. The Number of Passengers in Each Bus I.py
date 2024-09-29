# Table: Buses
#
# +--------------+------+
# | Column Name  | Type |
# +--------------+------+
# | bus_id       | int  |
# | arrival_time | int  |
# +--------------+------+
# bus_id is the column with unique values for this table.
# Each row of this table contains information about the arrival time of a bus at the LeetCode station.
# No two buses will arrive at the same time.
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
# passenger_id is the column with unique values for this table.
# Each row of this table contains information about the arrival time of a passenger at the LeetCode station.
#
#
# Buses and passengers arrive at the LeetCode station. If a bus arrives at the station at time tbus
# and a passenger arrived at time tpassenger where tpassenger <= tbus and the passenger did not catch any bus,
# the passenger will use that bus.
#
# Write a solution to report the number of users that used each bus.
#
# Return the result table ordered by bus_id in ascending order.
import pandas as pd
from pathlib import Path
import os

def count_passengers_in_bus(buses: pd.DataFrame, passengers: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(
        left=buses,
        right=passengers,
        how="cross",
        suffixes=("_bus", "_pas")
    )
    merged["less"] = merged["arrival_time_pas"] <= merged["arrival_time_bus"]
    copy_merged = merged.loc[merged["less"]].copy()
    copy_merged["our_rank"] = (copy_merged
                               .groupby(by="passenger_id", as_index=False)["arrival_time_bus"]
                               .rank(method="dense", ascending=True))
    grouped = copy_merged.loc[copy_merged["our_rank"] == 1].groupby(by="bus_id", as_index=False).agg(passengers_cnt=("passenger_id", "count"))
    return pd.merge(
        left=buses,
        right=grouped,
        how="left",
        on="bus_id"
    ).fillna(0).sort_values(by="bus_id", ascending=True)[["bus_id", "passengers_cnt"]]

path = Path(os.getcwd()) / "data" / "2142. The Number of Passengers in Each Bus I.xlsx"
buses = pd.read_excel(path, sheet_name="Buses")
passengers = pd.read_excel(path, sheet_name="Passengers")
print(count_passengers_in_bus(buses, passengers))