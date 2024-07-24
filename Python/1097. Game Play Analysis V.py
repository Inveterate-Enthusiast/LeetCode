# Table: Activity
#
# +--------------+---------+
# | Column Name  | Type    |
# +--------------+---------+
# | player_id    | int     |
# | device_id    | int     |
# | event_date   | date    |
# | games_played | int     |
# +--------------+---------+
# (player_id, event_date) is the primary key (combination of columns with unique values) of this table.
# This table shows the activity of players of some games.
# Each row is a record of a player who logged in and played a number of games (possibly 0) before logging out on someday using some device.
#
#
# The install date of a player is the first login day of that player.
#
# We define day one retention of some date x to be the number of players whose install date is x and they logged back in on the day right after x, divided by the number of players whose install date is x, rounded to 2 decimal places.
#
# Write a solution to report for each install date, the number of players that installed the game on that day, and the day one retention.
#
# Return the result table in any order.
import pandas as pd
import os
from pathlib import Path

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    grouped = activity.groupby(by="player_id", as_index=False).agg(install_dt=("event_date", "min"), second_date=("event_date", lambda x: x[x > x.min()].min()))
    grouped["bool"] = grouped.apply(lambda x: x["second_date"] == (x["install_dt"] + pd.Timedelta(days=1)), axis=1)
    grouped = grouped.groupby(by="install_dt", as_index=False, dropna=False).agg(installs=("player_id", "nunique"), second_count=("bool", "sum"))
    grouped["Day1_retention"] = grouped.apply(lambda x: round((x["second_count"] / x["installs"] + 1e-9), 2), axis=1)
    return grouped[["install_dt", "installs", "Day1_retention"]]

activity = pd.read_excel(Path(os.getcwd()) / "data" / "1097. Game Play Analysis V.xlsx")
print(gameplay_analysis(activity))