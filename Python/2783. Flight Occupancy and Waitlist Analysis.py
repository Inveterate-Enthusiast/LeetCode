# Table: Flights
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | flight_id   | int  |
# | capacity    | int  |
# +-------------+------+
# flight_id is the column with unique values for this table.
# Each row of this table contains flight id and its capacity.
# Table: Passengers
#
# +--------------+------+
# | Column Name  | Type |
# +--------------+------+
# | passenger_id | int  |
# | flight_id    | int  |
# +--------------+------+
# passenger_id is the column with unique values for this table.
# Each row of this table contains passenger id and flight id.
# Passengers book tickets for flights in advance. If a passenger books a ticket for
# a flight and there are still empty seats available on the flight, the passenger ticket will be confirmed.
# However, the passenger will be on a waitlist if the flight is already at full capacity.
#
# Write a solution to report the number of passengers who successfully booked a flight (got a seat)
# and the number of passengers who are on the waitlist for each flight.
#
# Return the result table ordered by flight_id in ascending order.
import pandas as pd

def waitlist_analysis(flights: pd.DataFrame, passengers: pd.DataFrame) -> pd.DataFrame:
    passengers["rank"] = passengers.groupby(by="flight_id", as_index=False)["passenger_id"].rank(method="dense")
    merged = pd.merge(
        left=passengers,
        right=flights,
        how="left",
        on="flight_id"
    )
    merged["bool_1"] = merged["rank"] <= merged["capacity"]
    merged["bool_2"] = merged["rank"] > merged["capacity"]
    grouped = merged.groupby(by="flight_id", as_index=False).agg(booked_cnt=("bool_1", "sum"), waitlist_cnt=("bool_2", "sum"))
    return pd.merge(left=flights, right=grouped, how="left", on="flight_id").fillna(0).drop(labels="capacity", axis=1).sort_values(by="flight_id", ascending=True)

