# Table: TeamStats
#
# +------------------+---------+
# | Column Name      | Type    |
# +------------------+---------+
# | team_id          | int     |
# | team_name        | varchar |
# | matches_played   | int     |
# | wins             | int     |
# | draws            | int     |
# | losses           | int     |
# +------------------+---------+
# team_id is the unique key for this table.
# This table contains team id, team name, matches_played, wins, draws, and losses.
# Write a solution to calculate the points and rank for each team in the league. Points are calculated as follows:
#
# 3 points for a win
# 1 point for a draw
# 0 points for a loss
# Note: Teams with the same points must be assigned the same rank.
#
# Return the result table ordered by points in descending, and then by team_name in ascending order.
import pandas as pd

def calculate_team_standings(team_stats: pd.DataFrame) -> pd.DataFrame:
    team_stats["points"] = (team_stats["wins"] * 3) + team_stats["draws"]
    team_stats["position"] = team_stats["points"].rank(method="min", ascending=False)
    return team_stats[["team_id", "team_name", "points", "position"]].sort_values(by=["points", "team_name"], ascending=[False, True])