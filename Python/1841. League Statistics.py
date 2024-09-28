# Table: Teams
#
# +----------------+---------+
# | Column Name    | Type    |
# +----------------+---------+
# | team_id        | int     |
# | team_name      | varchar |
# +----------------+---------+
# team_id is the column with unique values for this table.
# Each row contains information about one team in the league.
#
#
# Table: Matches
#
# +-----------------+---------+
# | Column Name     | Type    |
# +-----------------+---------+
# | home_team_id    | int     |
# | away_team_id    | int     |
# | home_team_goals | int     |
# | away_team_goals | int     |
# +-----------------+---------+
# (home_team_id, away_team_id) is the primary key (combination of columns with unique values) for this table.
# Each row contains information about one match.
# home_team_goals is the number of goals scored by the home team.
# away_team_goals is the number of goals scored by the away team.
# The winner of the match is the team with the higher number of goals.
#
#
# Write a solution to report the statistics of the league.
# The statistics should be built using the played matches where the winning team gets three points and the losing team gets no points.
# If a match ends with a draw, both teams get one point.
#
# Each row of the result table should contain:
#
# team_name - The name of the team in the Teams table.
# matches_played - The number of matches played as either a home or away team.
# points - The total points the team has so far.
# goal_for - The total number of goals scored by the team across all matches.
# goal_against - The total number of goals scored by opponent teams against this team across all matches.
# goal_diff - The result of goal_for - goal_against.
# Return the result table ordered by points in descending order. If two or more teams have the same points,
# order them by goal_diff in descending order. If there is still a tie, order them by team_name in lexicographical order.
import pandas as pd
import numpy as np
from pathlib import Path
import os

def league_statistics(teams: pd.DataFrame, matches: pd.DataFrame) -> pd.DataFrame:
    matches["home_team_points"] = np.where(
        matches["home_team_goals"] > matches["away_team_goals"], 3,
        np.where(
            matches["home_team_goals"] < matches["away_team_goals"], 0, 1
        )
    )
    matches["away_team_points"] = np.where(
        matches["home_team_goals"] > matches["away_team_goals"], 0,
        np.where(
            matches["home_team_goals"] < matches["away_team_goals"], 3, 1
        )
    )
    concated = pd.concat([
        matches[["home_team_id", "home_team_goals", "home_team_points", "away_team_goals"]].rename(columns={
            "home_team_id": "team_id",
            "home_team_goals": "goal_for",
            "home_team_points": "points",
            "away_team_goals": "goal_against"
        }),
        matches[["away_team_id", "away_team_goals", "away_team_points", "home_team_goals"]].rename(columns={
            "away_team_id": "team_id",
            "away_team_goals": "goal_for",
            "away_team_points": "points",
            "home_team_goals": "goal_against"
        }),
    ])
    grouped = concated.groupby(by="team_id", as_index=False).agg(
        matches_played=("team_id", "count"),
        points=("points", "sum"),
        goal_for=("goal_for", "sum"),
        goal_against=("goal_against", "sum")
    )
    grouped["goal_diff"] = grouped["goal_for"] - grouped["goal_against"]
    merged = pd.merge(
        left=grouped,
        right=teams,
        how="left",
        on="team_id"
    )
    merged.insert(merged.columns.get_loc("team_id") + 1, "team_name", merged.pop("team_name"))
    return merged.drop(labels="team_id", axis=1).sort_values(by=["points", "goal_diff", "team_name"], ascending=[False, False, True])

path = Path(os.getcwd()) / "data" / "1841. League Statistics.xlsx"
teams = pd.read_excel(path, sheet_name="Teams")
matches = pd.read_excel(path, sheet_name="Matches")
print(league_statistics(teams, matches))