# Table: Teams
#
# +---------------+----------+
# | Column Name   | Type     |
# +---------------+----------+
# | team_id       | int      |
# | team_name     | varchar  |
# +---------------+----------+
# team_id is the column with unique values of this table.
# Each row of this table represents a single football team.
#
#
# Table: Matches
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | match_id      | int     |
# | host_team     | int     |
# | guest_team    | int     |
# | host_goals    | int     |
# | guest_goals   | int     |
# +---------------+---------+
# match_id is the column of unique values of this table.
# Each row is a record of a finished match between two different teams.
# Teams host_team and guest_team are represented by their IDs in the Teams table (team_id),
# and they scored host_goals and guest_goals goals, respectively.
#
#
# You would like to compute the scores of all teams after all matches. Points are awarded as follows:
# A team receives three points if they win a match (i.e., Scored more goals than the opponent team).
# A team receives one point if they draw a match (i.e., Scored the same number of goals as the opponent team).
# A team receives no points if they lose a match (i.e., Scored fewer goals than the opponent team).
# Write a solution that selects the team_id, team_name and num_points of each team in the tournament after all described matches.
#
# Return the result table ordered by num_points in decreasing order.
# In case of a tie, order the records by team_id in increasing order.
import pandas as pd
import os
from pathlib import Path
import numpy as np

def team_scores(teams: pd.DataFrame, matches: pd.DataFrame) -> pd.DataFrame:
    matches["win"] = np.where(matches["host_goals"] > matches["guest_goals"], "left", np.where(matches["host_goals"] < matches["guest_goals"], "right", None))
    grouped = pd.concat([
        matches.rename(columns={"host_team": "team_id"}).groupby(by="team_id", as_index=False).agg(num_points=("win", lambda x: ((x == "left").sum() * 3) + ((x.isna()).sum()))),
        matches.rename(columns={"guest_team": "team_id"}).groupby(by="team_id", as_index=False).agg(num_points=("win", lambda x: ((x == "right").sum() * 3) + ((x.isna()).sum())))
    ]).groupby(by="team_id", as_index=False).agg(num_points=("num_points", "sum"))

    return pd.merge(
        left=teams,
        right=grouped,
        on="team_id",
        how="left"
    ).fillna(0).sort_values(by=["num_points", "team_id"], ascending=[False, True])[["team_id", "team_name", "num_points"]]

path = Path(os.getcwd()) / "data" / "1212. Team Scores in Football Tournament.xlsx"
teams = pd.read_excel(path, sheet_name="Teams")
matches = pd.read_excel(path, sheet_name="Matches")
print(team_scores(teams, matches))