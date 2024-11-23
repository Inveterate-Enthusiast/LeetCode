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
# Write a solution to report the percentage of working drivers (working_percentage) for each month of 2020 where:
#
#
# Note that if the number of available drivers during a month is zero, we consider the working_percentage to be 0.
#
# Return the result table ordered by month in ascending order, where month is the month's number (January is 1, February is 2, etc.).
# Round working_percentage to the nearest 2 decimal places.

import pandas as pd

def hopper_company_queries(drivers: pd.DataFrame, rides: pd.DataFrame, accepted_rides: pd.DataFrame) -> pd.DataFrame:
    months = pd.DataFrame({
        "month": range(1, 12+1, 1)
    })
    rides_merged = pd.merge(
        left=rides.loc[rides["requested_at"].dt.year == 2020],
        right=accepted_rides,
        how="inner",
        on="ride_id"
    )
    rides_merged["month"] = rides_merged["requested_at"].dt.month
    drivers_merged = pd.merge(
        left=drivers,
        right=rides_merged,
        how="left",
        on="driver_id"
    )
    drivers_merged["driver_month"] = drivers_merged["join_date"].dt.month
    drivers["month"] = drivers["join_date"].dt.month
    drivers_all_grouped = drivers.loc[drivers["join_date"].dt.year == 2020].groupby(by="month", as_index=False).agg(count=("driver_id", "nunique")).sort_values(by="month", ascending=True)
    drivers_all_grouped = pd.merge(
        left=months,
        right=drivers_all_grouped,
        how="left",
        on="month"
    ).fillna(0)
    drivers_all_grouped.loc[drivers_all_grouped.index[drivers_all_grouped["month"] == 1][0], "count"] += drivers.loc[drivers["join_date"].dt.year < 2020, "driver_id"].nunique()
    drivers_all_grouped["available"] = drivers_all_grouped["count"].transform("cumsum")
    drivers_accepted_grouped = drivers_merged.loc[~drivers_merged["month"].isna()].groupby(by="month", as_index=False).agg(accepted=("driver_id", "nunique"))
    result = pd.merge(
        left=drivers_all_grouped,
        right=drivers_accepted_grouped,
        how="left",
        on="month"
    ).fillna(0)
    result["working_percentage"] = ((result["accepted"] / result["available"] * 100) + 1e-9).round(2)
    return result[["month", "working_percentage"]].sort_values(by="month", ascending=True).fillna(0)