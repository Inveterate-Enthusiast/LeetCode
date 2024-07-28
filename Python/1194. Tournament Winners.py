# Table: Players
#
# +-------------+-------+
# | Column Name | Type  |
# +-------------+-------+
# | player_id   | int   |
# | group_id    | int   |
# +-------------+-------+
# player_id is the primary key (column with unique values) of this table.
# Each row of this table indicates the group of each player.
# Table: Matches
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | match_id      | int     |
# | first_player  | int     |
# | second_player | int     |
# | first_score   | int     |
# | second_score  | int     |
# +---------------+---------+
# match_id is the primary key (column with unique values) of this table.
# Each row is a record of a match, first_player and second_player contain the player_id of each match.
# first_score and second_score contain the number of points of the first_player and second_player respectively.
# You may assume that, in each match, players belong to the same group.
#
#
# The winner in each group is the player who scored the maximum total points within the group. In the case of a tie, the lowest player_id wins.
#
# Write a solution to find the winner in each group.
#
# Return the result table in any order.
import pandas as pd
import os
from pathlib import Path

def tournament_winners(players: pd.DataFrame, matches: pd.DataFrame) -> pd.DataFrame:
    players_scores = (pd.concat([
        (matches.groupby(by="first_player", as_index=False).agg(scores=("first_score", "sum")).rename(columns={"first_player": "player_id"})),
        (matches.groupby(by="second_player", as_index=False).agg(scores=("second_score", "sum")).rename(columns={"second_player": "player_id"}))
    ])
                      .groupby(by="player_id", as_index=False).agg(total=("scores", "sum")))

    merged = pd.merge(
        left=players_scores,
        right=players,
        on="player_id",
        how="left"
    )
    merged.sort_values(by=["group_id", "total", "player_id"], ascending=[True, False, True], inplace=True)
    merged["our_rank"] = merged.groupby(by="group_id").cumcount() + 1
    return merged.loc[merged["our_rank"] == 1, ["group_id", "player_id"]]

path = Path(os.getcwd()) / "data" / "1194. Tournament Winners.xlsx"
players = pd.read_excel(path, sheet_name="Players")
matches = pd.read_excel(path, sheet_name="Matches")
print(tournament_winners(players, matches))