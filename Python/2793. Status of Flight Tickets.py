# Table: Flights
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | flight_id   | int  |
# | capacity    | int  |
# +-------------+------+
# flight_id column contains distinct values.
# Each row of this table contains flight id and capacity.
# Table: Passengers
#
# +--------------+----------+
# | Column Name  | Type     |
# +--------------+----------+
# | passenger_id | int      |
# | flight_id    | int      |
# | booking_time | datetime |
# +--------------+----------+
# passenger_id column contains distinct values.
# booking_time column contains distinct values.
# Each row of this table contains passenger id, booking time, and their flight id.
# Passengers book tickets for flights in advance. If a passenger books a ticket for a flight and there are still empty seats available on the flight,
# the passenger's ticket will be confirmed. However, the passenger will be on a waitlist if the flight is already at full capacity.
#
# Write a solution to determine the current status of flight tickets for each passenger.
#
# Return the result table ordered by passenger_id in ascending order.


import pandas as pd
import numpy as np

def ticket_status(flights: pd.DataFrame, passengers: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(
        left=passengers,
        right=flights,
        how="left",
        on="flight_id"
    ).sort_values(by="booking_time", ascending=True)
    merged["cumcnt"] = merged.groupby(by="flight_id").cumcount() + 1
    merged["Status"] = np.where(merged["cumcnt"] > merged["capacity"], "Waitlist", "Confirmed")
    return merged[["passenger_id", "Status"]].sort_values(by="passenger_id", ascending=True)
