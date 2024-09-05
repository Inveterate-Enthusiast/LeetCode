# Table: Players
#
# +----------------+---------+
# | Column Name    | Type    |
# +----------------+---------+
# | player_id      | int     |
# | player_name    | varchar |
# +----------------+---------+
# player_id is the primary key (column with unique values) for this table.
# Each row in this table contains the name and the ID of a tennis player.
#
#
# Table: Championships
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | year          | int     |
# | Wimbledon     | int     |
# | Fr_open       | int     |
# | US_open       | int     |
# | Au_open       | int     |
# +---------------+---------+
# year is the primary key (column with unique values) for this table.
# Each row of this table contains the IDs of the players who won one each tennis tournament of the grand slam.
#
#
# Write a solution to report the number of grand slam tournaments won by each player. Do not include the players who did not win any tournament.
#
# Return the result table in any order.
import pandas as pd

def grand_slam_titles(players: pd.DataFrame, championships: pd.DataFrame) -> pd.DataFrame:
    concated = pd.concat([
        championships[["year", "Wimbledon"]].rename(columns={"Wimbledon": "player_id"}),
        championships[["year", "Fr_open"]].rename(columns={"Fr_open": "player_id"}),
        championships[["year", "US_open"]].rename(columns={"US_open": "player_id"}),
        championships[["year", "Au_open"]].rename(columns={"Au_open": "player_id"}),
    ])
    grouped = concated.groupby(by="player_id", as_index=False).agg(grand_slams_count=("player_id", "count"))
    return pd.merge(
        left=grouped,
        right=players,
        how="left",
        on="player_id"
    )[["player_id", "player_name", "grand_slams_count"]]


