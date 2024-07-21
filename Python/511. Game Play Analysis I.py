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

# Write a solution to find the first login date for each player.
#
# Return the result table in any order.
import pandas as pd
from pathlib import Path

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    return activity.groupby(by="player_id", as_index=False).agg(first_login=("event_date", "min"))


path = Path(__file__).parent / "data" / "511. Activity.xlsx"
activity = pd.read_excel(path)
print(game_analysis(activity))

