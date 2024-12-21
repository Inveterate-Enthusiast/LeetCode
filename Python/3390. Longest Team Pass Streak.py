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
# Table: Passes
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | pass_from   | int     |
# | time_stamp  | varchar |
# | pass_to     | int     |
# +-------------+---------+
# (pass_from, time_stamp) is the unique key for this table.
# pass_from is a foreign key to player_id from Teams table.
# Each row represents a pass made during a match, time_stamp represents the time in minutes (00:00-90:00) when the pass was made,
# pass_to is the player_id of the player receiving the pass.
# Write a solution to find the longest successful pass streak for each team during the match. The rules are as follows:
#
# A successful pass streak is defined as consecutive passes where:
# Both the pass_from and pass_to players belong to the same team
# A streak breaks when either:
# The pass is intercepted (received by a player from the opposing team)
# Return the result table ordered by team_name in ascending order.

import pandas as pd
import numpy as np

def calculate_longest_streaks(teams: pd.DataFrame, passes: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(
        left=passes,
        right=teams.rename(columns={"player_id": "pass_from", "team_name": "team_from"}),
        how="left",
        on="pass_from"
    )
    merged = pd.merge(
        left=merged,
        right=teams.rename(columns={"player_id": "pass_to", "team_name": "team_to"}),
        how="left",
        on="pass_to"
    )
    merged["bool"] = np.where(merged["team_from"] == merged["team_to"], 0, 1)
    merged["groups"] = merged.groupby(by="team_from", as_index=False)["bool"].cumsum() + 1
    merged["streak"] = merged.groupby(by=["team_from", "team_to", "groups"], as_index=False)["groups"].transform("count")
    grouped = (merged
               .loc[merged["team_from"] == merged["team_to"]]
               .groupby(by="team_from", as_index=False)
               .agg(longest_streak=("streak", "max"))
               .rename(columns={"team_from": "team_name"}))
    return grouped.sort_values(by="team_name", ascending=True)
