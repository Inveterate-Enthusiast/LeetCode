# Table: Trips
#
# +-------------+----------+
# | Column Name | Type     |
# +-------------+----------+
# | id          | int      |
# | client_id   | int      |
# | driver_id   | int      |
# | city_id     | int      |
# | status      | enum     |
# | request_at  | varchar  |
# +-------------+----------+
# id is the primary key (column with unique values) for this table.
# The table holds all taxi trips. Each trip has a unique id, while client_id and driver_id are foreign keys to the users_id at the Users table.
# Status is an ENUM (category) type of ('completed', 'cancelled_by_driver', 'cancelled_by_client').
#
# Table: Users
#
# +-------------+----------+
# | Column Name | Type     |
# +-------------+----------+
# | users_id    | int      |
# | banned      | enum     |
# | role        | enum     |
# +-------------+----------+
# users_id is the primary key (column with unique values) for this table.
# The table holds all users. Each user has a unique users_id, and role is an ENUM type of ('client', 'driver', 'partner').
# banned is an ENUM (category) type of ('Yes', 'No').
#
# The cancellation rate is computed by dividing the number of canceled (by client or driver) requests
# with unbanned users by the total number of requests with unbanned users on that day.
#
# Write a solution to find the cancellation rate of requests with unbanned users (both client and driver must not be banned)
# each day between "2013-10-01" and "2013-10-03". Round Cancellation Rate to two decimal points.
#
# Return the result table in any order.
import pandas as pd
from pathlib import Path
import os
from datetime import datetime as dt
from IPython.display import display

def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    not_banned = users[users["banned"] == "No"]
    left_border = dt(2013,10,1)
    right_border = dt(2013,10,3)
    trips["request_at"] = trips["request_at"].apply(lambda x: pd.to_datetime(x))

    grouped = trips[
        pd.to_datetime(trips["request_at"]).between(left=left_border, right=right_border, inclusive="both") &
        trips["client_id"].isin(not_banned["users_id"]) &
        trips["driver_id"].isin(not_banned["users_id"])
    ].groupby(
        by="request_at", as_index=False
    ).agg(status=("status",
                  lambda x:
                  round(((sum(x != "completed") / x.shape[0]) if x.shape[0] != 0 else 0), 2)
                  )).rename(columns={"request_at": "Day", "status": "Cancellation rate"})

    return grouped.infer_objects(copy=False).fillna(0)[["Day", "Cancellation rate"]]

path = Path(os.getcwd()) / "data" / "262. Trips and Users.xlsx"
trips = pd.read_excel(path, sheet_name="Trips")
users = pd.read_excel(path, sheet_name="Users")
print(trips_and_users(trips, users))

