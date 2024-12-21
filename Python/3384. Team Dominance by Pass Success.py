# Table: Teams
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | player_id   | int     |
# | team_name   | varchar |
# +-------------+---------+
# player_id is the unique key for this table.
# Each row contains the unique identifier for player and the name of one of the teams participating in that match.
#
# Table: Passes
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | pass_from   | int     |
# | time_stamp  | varchar |
# | pass_to     | int     |
# +-------------+---------+
# (pass_from, time_stamp) is the primary key for this table.
# pass_from is a foreign key to player_id from Teams table.
# Each row represents a pass made during a match, time_stamp represents the time in minutes (00:00-90:00) when the pass was made,
# pass_to is the player_id of the player receiving the pass.
#
# Write a solution to calculate the dominance score for each team in both halves of the match. The rules are as follows:
#
# A match is divided into two halves: first half (00:00-45:00 minutes) and second half (45:01-90:00 minutes)
# The dominance score is calculated based on successful and intercepted passes:
# When pass_to is a player from the same team: +1 point
# When pass_to is a player from the opposing team (interception): -1 point
# A higher dominance score indicates better passing performance
# Return the result table ordered by team_name and half_number in ascending order.


import pandas as pd
import numpy as np

def calculate_team_dominance(teams: pd.DataFrame, passes: pd.DataFrame) -> pd.DataFrame:
    passes["half_number"] = np.where(passes["time_stamp"] <= "45:00", 1, 2)
    merged = pd.merge(
        left=passes,
        right=teams.rename(columns={"team_name": "team_from", "player_id": "pass_from"}),
        how="left",
        on="pass_from"
    )
    merged = pd.merge(
        left=merged,
        right=teams.rename(columns={"team_name": "team_to", "player_id": "pass_to"})
    )
    merged["bool"] = np.where(merged["team_from"] == merged["team_to"], 1, (-1))
    grouped = merged.groupby(by=["team_from", "half_number"], as_index=False).agg(dominance=("bool", "sum"))
    return (grouped[["team_from", "half_number", "dominance"]]
            .rename(columns={"team_from": "team_name"})
            .sort_values(by=["team_name", "half_number"], ascending=[True, True]))