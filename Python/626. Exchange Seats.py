# Table: Seat
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | student     | varchar |
# +-------------+---------+
# id is the primary key (unique value) column for this table.
# Each row of this table indicates the name and the ID of a student.
# id is a continuous increment.
#
#
# Write a solution to swap the seat id of every two consecutive students. If the number of students is odd, the id of the last student is not swapped.
#
# Return the result table ordered by id in ascending order.
import pandas as pd
import os
from pathlib import Path

def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    seat.set_index("id", inplace=True)
    i = 1
    for index, row in seat.iterrows():
        if i % 2:
            prev_index = index
        else:
            seat.loc[prev_index, "student"], seat.loc[index, "student"] \
                = seat.loc[index, "student"], seat.loc[prev_index, "student"]
        i += 1

    return seat.sort_index(ascending=True).reset_index()

path = Path(os.getcwd()) / "data" / "626. Exchange Seats.xlsx"
seat = pd.read_excel(path)
print(exchange_seats(seat))