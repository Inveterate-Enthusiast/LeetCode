# Table: Drivers
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | driver_id   | int     |
# | join_date   | date    |
# +-------------+---------+
# driver_id is the column with unique values for this table.
# Each row of this table contains the driver's ID and the date they joined the Hopper company.
#
#
# Table: Rides
#
# +--------------+---------+
# | Column Name  | Type    |
# +--------------+---------+
# | ride_id      | int     |
# | user_id      | int     |
# | requested_at | date    |
# +--------------+---------+
# ride_id is the column with unique values for this table.
# Each row of this table contains the ID of a ride, the user's ID that requested it, and the day they requested it.
# There may be some ride requests in this table that were not accepted.
#
#
# Table: AcceptedRides
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | ride_id       | int     |
# | driver_id     | int     |
# | ride_distance | int     |
# | ride_duration | int     |
# +---------------+---------+
# ride_id is the column with unique values for this table.
# Each row of this table contains some information about an accepted ride.
# It is guaranteed that each accepted ride exists in the Rides table.
#
#
# Write a solution to compute the average_ride_distance and average_ride_duration of every 3-month window starting
# from January - March 2020 to October - December 2020. Round average_ride_distance and average_ride_duration
# to the nearest two decimal places.
#
# The average_ride_distance is calculated by summing up the total ride_distance values from the three months and dividing it by 3.
# The average_ride_duration is calculated in a similar way.
#
# Return the result table ordered by month in ascending order, where month is the starting month's number (January is 1, February is 2, etc.).

import pandas as pd

def hopper_company_queries(drivers: pd.DataFrame, rides: pd.DataFrame, accepted_rides: pd.DataFrame) -> pd.DataFrame:
    months = pd.DataFrame({
        "month": range(1, 12+1, 1)
    })
    rides_merged = pd.merge(
        left=rides,
        right=accepted_rides,
        how="inner",
        on="ride_id"
    ).query("requested_at.dt.year == 2020")
    rides_merged["month"] = rides_merged["requested_at"].dt.month
    merged = pd.merge(
        left=months,
        right=rides_merged,
        how="left",
        on="month"
    )[["month", "ride_distance", "ride_duration"]].fillna(0)
    grouped = (merged
               .groupby(by="month", as_index=False)
               .agg(distance_sum=("ride_distance", "sum"), duration_sum=("ride_duration", "sum"))
               .sort_values(by="month", ascending=True))
    grouped["average_ride_distance"] = grouped["distance_sum"].rolling(window=3, min_periods=3).mean().shift(-2).round(2)
    grouped["average_ride_duration"] = grouped["duration_sum"].rolling(window=3, min_periods=3).mean().shift(-2).round(2)
    return grouped.loc[grouped["month"] <= 10, ["month", "average_ride_distance", "average_ride_duration"]]

