# Table: Drivers
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | driver_id   | int     |
# | join_date   | date    |
# +-------------+---------+
# driver_id is the primary key (column with unique values) for this table.
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
# ride_id is the primary key (column with unique values) for this table.
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
# ride_id is the primary key (column with unique values) for this table.
# Each row of this table contains some information about an accepted ride.
# It is guaranteed that each accepted ride exists in the Rides table.
#
#
# Write a solution to report the following statistics for each month of 2020:
#
# The number of drivers currently with the Hopper company by the end of the month (active_drivers).
# The number of accepted rides in that month (accepted_rides).
# Return the result table ordered by month in ascending order, where month is the month's number (January is 1, February is 2, etc.).
import pandas as pd

def hopper_company(drivers: pd.DataFrame, rides: pd.DataFrame, accepted_rides: pd.DataFrame) -> pd.DataFrame:
    months = pd.DataFrame({
        "month": range(1, 12+1, 1)
    })
    drivers["month"] = pd.to_datetime(arg=drivers["join_date"]).dt.month
    filtered_rides = pd.merge(
        left=rides.loc[rides["requested_at"].dt.year == 2020],
        right=accepted_rides,
        how="inner",
        on="ride_id"
    )
    filtered_rides["month"] = pd.to_datetime(arg=filtered_rides["requested_at"]).dt.month
    grouped_rides = filtered_rides.groupby(by="month", as_index=False).agg(accepted_rides=("ride_id", "nunique"))
    grouped_drivers = drivers.loc[drivers["join_date"].dt.year == 2020].groupby(by="month", as_index=False).agg(count=("driver_id", "nunique"))
    merged = pd.merge(
        left=months,
        right=grouped_drivers,
        how="left",
        on="month"
    ).fillna(0).sort_values(by="month", ascending=True)
    merged.loc[merged.index[merged["month"] == 1][0], "count"] += drivers.loc[drivers["join_date"].dt.year < 2020, "driver_id"].nunique()
    merged["active_drivers"] = merged["count"].transform("cumsum")
    result = pd.merge(
        left=merged,
        right=grouped_rides,
        how="left",
        on="month"
    ).fillna(0)
    return result[["month", "active_drivers", "accepted_rides"]].sort_values(by="month", ascending=True)

