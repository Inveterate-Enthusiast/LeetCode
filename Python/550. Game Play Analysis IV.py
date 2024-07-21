# Table: Activity
#
# +--------------+---------+
# | Column Name  | Type    |
# +--------------+---------+
# | player_id    | int     |
# | device_id    | int     |
# | event_date   | date    |
# | games_played | int     |
# +--------------+---------+
# (player_id, event_date) is the primary key (combination of columns with unique values) of this table.
# This table shows the activity of players of some games.
# Each row is a record of a player who logged in and played a number of games (possibly 0) before logging out on someday using some device.
#
#
# Write a solution to report the fraction of players that logged in again on the day after the day they first logged in,
# rounded to 2 decimal places.
# In other words, you need to count the number of players that logged in for at least two consecutive days starting
# from their first login date, then divide that number by the total number of players.
import pandas as pd


def grouping(df: pd.Series) -> bool:
    return bool((df.min() + pd.Timedelta(value=1, unit="D")) in df.values)


def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    if not activity["player_id"].nunique():
        return pd.DataFrame({
            "fraction": [None]
        })

    grouped = activity.groupby(by="player_id", as_index=False).agg(bool=("event_date", grouping))
    x = round(
        (grouped["bool"].sum())
        /
        (activity["player_id"].nunique()),
        2)
    return pd.DataFrame({
            "fraction": [x]
        })


def gameplay_analysis1(activity: pd.DataFrame) -> pd.DataFrame:
    activity["start"] = activity.groupby(by="player_id")["event_date"].transform(func="min")

    return pd.DataFrame({
        "fraction": [(None if not (x := (activity["player_id"].nunique())) else
                      round(
                          (activity.loc[
                               activity["event_date"] == (activity["start"] + pd.Timedelta(value=1, unit="D")),
                               "player_id"]
                           .nunique())
                          /
                          (x),
                      2))]
    })