# Table: Flights
#
# +-------------------+------+
# | Column Name       | Type |
# +-------------------+------+
# | departure_airport | int  |
# | arrival_airport   | int  |
# | flights_count     | int  |
# +-------------------+------+
# (departure_airport, arrival_airport) is the primary key column (combination of columns with unique values) for this table.
# Each row of this table indicates that there were flights_count flights that departed from departure_airport and arrived at arrival_airport.
#
#
# Write a solution to report the ID of the airport with the most traffic.
# The airport with the most traffic is the airport that has the largest total number of flights that either
# departed from or arrived at the airport. If there is more than one airport with the most traffic, report them all.
#
# Return the result table in any order.
import pandas as pd

def airport_with_most_traffic(flights: pd.DataFrame) -> pd.DataFrame:
    concated = pd.concat([
        flights.rename(columns={"departure_airport": "airport_id"})[["airport_id", "flights_count"]],
        flights.rename(columns={"arrival_airport": "airport_id"})[["airport_id", "flights_count"]]
    ])
    grouped = concated.groupby(by="airport_id", as_index=False).agg(count=("flights_count", "sum"))
    return grouped.loc[grouped["count"] == grouped["count"].max(), ["airport_id"]]