# Table: Matches
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | player_id   | int  |
# | match_day   | date |
# | result      | enum |
# +-------------+------+
# (player_id, match_day) is the primary key (combination of columns with unique values) for this table.
# Each row of this table contains the ID of a player, the day of the match they played, and the result of that match.
# The result column is an ENUM (category) type of ('Win', 'Draw', 'Lose').
#
#
# The winning streak of a player is the number of consecutive wins uninterrupted by draws or losses.
#
# Write a solution to count the longest winning streak for each player.
#
# Return the result table in any order.


import pandas as pd
import numpy as np

def longest_winning_streak(matches: pd.DataFrame) -> pd.DataFrame:
    win = "Win"
    matches.sort_values(by="match_day", ascending=True, inplace=True)
    matches["extra_col"] = np.where(matches["result"] != win, 1, 0)
    matches["bool"] = np.where(matches["result"] != win, 0, 1)
    matches["group"] = matches.groupby(by="player_id", as_index=False)["extra_col"].transform("cumsum")
    grouped = matches.groupby(by=["player_id", "group"], as_index=False).agg(cnt=("bool", "sum"))
    return grouped.groupby(by="player_id", as_index=False).agg(longest_streak=("cnt", "max"))