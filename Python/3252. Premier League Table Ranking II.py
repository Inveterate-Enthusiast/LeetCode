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
# Write a solution to calculate the points, position, and tier for each team in the league. Points are calculated as follows:
#
# 3 points for a win
# 1 point for a draw
# 0 points for a loss
# Note: Teams with the same points must be assigned the same position.
#
# Tier ranking:
#
# Divide the league into 3 tiers based on points:
# Tier 1: Top 33% of teams
# Tier 2: Middle 33% of teams
# Tier 3: Bottom 34% of teams
# In case of ties at tier boundaries, place tied teams in the higher tier.
# Return the result table ordered by points in descending, and then by team_name in ascending order.
import pandas as pd
import numpy as np

def calculate_team_tiers(team_stats: pd.DataFrame) -> pd.DataFrame:
    team_stats["points"] = (team_stats["wins"] * 3) + (team_stats["draws"])
    team_stats["position"] = team_stats["points"].rank(method="min", ascending=False)
    max_pos = team_stats["team_id"].nunique()
    team_stats["tier"] = np.where(
        team_stats["position"] <= np.ceil(max_pos * 0.33), "Tier 1",
        (np.where(
            team_stats["position"] > np.ceil(max_pos * (1-0.33)), "Tier 3",
            "Tier 2"
        ))
    )
    return team_stats[["team_name", "points", "position", "tier"]].sort_values(by=["points", "team_name"], ascending=[False, True])
