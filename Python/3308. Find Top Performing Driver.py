# Table: Drivers
#
# +--------------+---------+
# | Column Name  | Type    |
# +--------------+---------+
# | driver_id    | int     |
# | name         | varchar |
# | age          | int     |
# | experience   | int     |
# | accidents    | int     |
# +--------------+---------+
# (driver_id) is the unique key for this table.
# Each row includes a driver's ID, their name, age, years of driving experience, and the number of accidents they’ve had.
# Table: Vehicles
#
# +--------------+---------+
# | vehicle_id   | int     |
# | driver_id    | int     |
# | model        | varchar |
# | fuel_type    | varchar |
# | mileage      | int     |
# +--------------+---------+
# (vehicle_id, driver_id, fuel_type) is the unique key for this table.
# Each row includes the vehicle's ID, the driver who operates it, the model, fuel type, and mileage.
# Table: Trips
#
# +--------------+---------+
# | trip_id      | int     |
# | vehicle_id   | int     |
# | distance     | int     |
# | duration     | int     |
# | rating       | int     |
# +--------------+---------+
# (trip_id) is the unique key for this table.
# Each row includes a trip's ID, the vehicle used, the distance covered (in miles), the trip duration (in minutes), and the passenger's rating (1-5).
# Uber is analyzing drivers based on their trips. Write a solution to find the top-performing driver for each fuel type based on the following criteria:
#
# A driver's performance is calculated as the average rating across all their trips. Average rating should be rounded to 2 decimal places.
# If two drivers have the same average rating, the driver with the longer total distance traveled should be ranked higher.
# If there is still a tie, choose the driver with the fewest accidents.
# Return the result table ordered by fuel_type in ascending order.

import pandas as pd

def get_top_performing_drivers(drivers: pd.DataFrame, vehicles: pd.DataFrame, trips: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(
        left=(
            pd.merge(
                left=trips,
                right=vehicles,
                how="left",
                on="vehicle_id"
            )
        ),
        right=drivers,
        how="left",
        on="driver_id"
    )
    grouped = ((merged
                 .groupby(by=["driver_id", "fuel_type"], as_index=False)
                 .agg(
                        rating=("rating", lambda x: round(x.mean(), 2)),
                        distance=("distance", "sum"),
                        accidents=("accidents", "max")
                    ))
                 .sort_values(by=["rating", "distance", "accidents"], ascending=[False, False, True])
                 .groupby(by="fuel_type", as_index=False).first())
    return grouped[["fuel_type", "driver_id", "rating", "distance"]].sort_values(by="fuel_type", ascending=True)
