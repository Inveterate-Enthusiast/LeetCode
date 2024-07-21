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

# Write a solution to report the device that is first logged in for each player.
#
# Return the result table in any order.
import pandas as pd
from pathlib import Path

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    grouped = activity.groupby(by="player_id", as_index=False).agg(event_date=("event_date", "min"))
    return pd.merge(
        left=grouped,
        right=activity[["player_id", "device_id", "event_date"]],
        how="left",
        on=["player_id", "event_date"]
    )[["player_id", "device_id"]]

def game_analysis1(activity: pd.DataFrame) -> pd.DataFrame:
    return activity.loc[
        activity.groupby(by="player_id")["event_date"].idxmin()
    ][["player_id", "device_id"]]

path = Path(__file__).parent / "data" / "512. Activity.xlsx"
activity = pd.read_excel(path)
print(game_analysis1(activity))