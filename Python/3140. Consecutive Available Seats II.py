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
# Write a solution to find the length of longest consecutive sequence of available seats in the cinema.
#
# Note:
#
# There will always be at most one longest consecutive sequence.
# If there are multiple consecutive sequences with the same length, include all of them in the output.
# Return the result table ordered by first_seat_id in ascending order.

import pandas as pd
import numpy as np

def consecutive_available_seats(cinema: pd.DataFrame) -> pd.DataFrame:
    filtered = cinema.loc[cinema["free"] == 1].sort_values(by="seat_id", ascending=True).copy()
    filtered["bool"] = np.where((filtered["seat_id"] - filtered["seat_id"].shift(1)) == 1, 1, 0)
    filtered["first"] = np.where(filtered["bool"] == 0, filtered["seat_id"], np.nan)
    filtered["first_id"] = filtered["first"].ffill()
    filtered["len"] = np.where(
        filtered["bool"] == 0,
        1,
        filtered["seat_id"] - filtered["first_id"] + 1
    )

    result_df = filtered.loc[filtered["len"] == filtered["len"].max()]
    return pd.DataFrame({
        "first_seat_id": result_df["first_id"].values,
        "last_seat_id": result_df["seat_id"].values,
        "consecutive_seats_len": result_df["len"].values
    })