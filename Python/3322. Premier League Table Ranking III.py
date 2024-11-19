# Table: SeasonStats
#
# +------------------+---------+
# | Column Name      | Type    |
# +------------------+---------+
# | season_id        | int     |
# | team_id          | int     |
# | team_name        | varchar |
# | matches_played   | int     |
# | wins             | int     |
# | draws            | int     |
# | losses           | int     |
# | goals_for        | int     |
# | goals_against    | int     |
# +------------------+---------+
# (season_id, team_id) is the unique key for this table.
# This table contains season id, team id, team name, matches played, wins, draws, losses, goals scored (goals_for),
# and goals conceded (goals_against) for each team in each season.
# Write a solution to calculate the points, goal difference, and rank for each team in each season.
# The ranking should be determined as follows:
#
# Teams are first ranked by their total points (highest to lowest)
# If points are tied, teams are then ranked by their goal difference (highest to lowest)
# If goal difference is also tied, teams are then ranked alphabetically by team name
# Points are calculated as follows:
#
# 3 points for a win
# 1 point for a draw
# 0 points for a loss
# Goal difference is calculated as: goals_for - goals_against
#
# Return the result table ordered by season_id in ascending order, then by rank in ascending order, and finally by team_name in ascending order.

import pandas as pd

def process_team_standings(season_stats: pd.DataFrame) -> pd.DataFrame:
    season_stats["points"] = (season_stats["wins"] * 3) + season_stats["draws"]
    season_stats["goal_difference"] = season_stats["goals_for"] - season_stats["goals_against"]
    season_stats.sort_values(by=["season_id", "points", "goal_difference", "team_name"], ascending=[True, False, False, True], inplace=True)
    season_stats["position"] = season_stats.groupby(by="season_id", as_index=False).cumcount() + 1
    return season_stats[["season_id", "team_id", "team_name", "points", "goal_difference", "position"]]
