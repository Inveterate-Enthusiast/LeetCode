# Table: Cinema
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | seat_id     | int  |
# | free        | bool |
# +-------------+------+
# seat_id is an auto-increment column for this table.
# Each row of this table indicates whether the ith seat is free or not. 1 means free while 0 means occupied.

# Find all the consecutive available seats in the cinema.
#
# Return the result table ordered by seat_id in ascending order.
#
# The test cases are generated so that more than two seats are consecutively available.

import pandas as pd

def consecutive_available_seats(cinema: pd.DataFrame) -> pd.DataFrame:
    cinema.sort_values(
        by="seat_id",
        ascending=True,
        inplace=True,
        na_position="first"
    )
    cinema.drop(axis=0, index=cinema[cinema["free"] == 0].index, inplace=True)
    return cinema[
        (cinema["seat_id"].diff(periods=1) == 1) |
        (cinema["seat_id"].diff(periods=(-1)) == (-1))][["seat_id"]]

def consecutive_available_seats1(cinema: pd.DataFrame) -> pd.DataFrame:
    cinema = cinema[cinema["free"] == 1].sort_values(
        by="seat_id",
        inplace=False,
        ascending=True,
        na_position="first"
    )
    return cinema[
        (cinema["seat_id"].diff(periods = 1) == 1) |
        (cinema["seat_id"].diff(periods = (-1)) == (-1))
    ][["seat_id"]]

def consecutive_available_seats3(cinema: pd.DataFrame) -> pd.DataFrame:
    cinema["before"] = cinema["free"].shift(-1)
    cinema["after"] = cinema["free"].shift(1)
    return cinema[
        (
            (cinema["before"] == 1) |
            (cinema["after"] == 1)
        ) &
        (cinema["free"] == 1)
    ][["seat_id"]].sort_values(by="seat_id", ascending=True, na_position="first", inplace=False)


cinema = pd.DataFrame({
    "seat_id": [1, 2, 3, 4, 5],
    "free": [1, 0, 1, 1, 1]
})
print(consecutive_available_seats3(cinema))