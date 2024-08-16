# Table: Spotify
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | track_name  | varchar |
# | artist      | varchar |
# +-------------+---------+
# id is the primary key (column with unique values) for this table.
# Each row contains an id, track_name, and artist.
# Write a solution to find how many times each artist appeared on the Spotify ranking list.
#
# Return the result table having the artist's name along with the corresponding number of occurrences ordered by occurrence count in descending order.
# If the occurrences are equal, then it’s ordered by the artist’s name in ascending order.
import pandas as pd

def count_occurrences(spotify: pd.DataFrame) -> pd.DataFrame:
    return (spotify
            .groupby(by="artist", as_index=False)
            .agg(occurrences=("id", "count"))
            .sort_values(by=["occurrences", "artist"], ascending=[False, True]))

def count_occurrences1(spotify: pd.DataFrame) -> pd.DataFrame:
    spotify["our_rank"] = spotify.groupby(by="artist", as_index=False)["id"].rank(method="dense", ascending=True)
    return (spotify
            .groupby(by="artist", as_index=False).agg(occurrences=("our_rank", "max"))
            .sort_values(by=["occurrences", "artist"], ascending=[False, True]))