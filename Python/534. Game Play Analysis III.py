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
# (player_id, event_date) is the primary key (column with unique values) of this table.
# This table shows the activity of players of some games.
# Each row is a record of a player who logged in and played a number of games (possibly 0) before logging out on someday using some device.

# Write a solution to report for each player and date, how many games played so far by the player. That is, the total number of games played by the player until that date. Check the example for clarity.
#
# Return the result table in any order.
import pandas as pd
from pathlib import Path

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity.sort_values(by=["player_id", "event_date"], ascending=(True, True), inplace=True)
    activity["games_played_so_far"] = activity.groupby("player_id")["games_played"].cumsum()
    return activity[["player_id", "event_date", "games_played_so_far"]]


path = Path(__file__).parent / "data" / "534. Activity.xlsx"
activity = pd.read_excel(path)
print(gameplay_analysis(activity))
