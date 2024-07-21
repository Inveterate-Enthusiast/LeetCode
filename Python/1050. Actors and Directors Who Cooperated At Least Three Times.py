# Table: ActorDirector
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | actor_id    | int     |
# | director_id | int     |
# | timestamp   | int     |
# +-------------+---------+
# timestamp is the primary key (column with unique values) for this table.

# Write a solution to find all the pairs (actor_id, director_id) where the actor has cooperated
# with the director at least three times.
#
# Return the result table in any order.
import pandas as pd
from pathlib import Path

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    grouped = actor_director.groupby(by=["actor_id", "director_id"], as_index=False).agg(count=("timestamp", "size"))
    return grouped.drop(
        index = grouped[grouped["count"] < 3].index,
        axis = 0,
        errors = "ignore"
    )[["actor_id", "director_id"]]

def actors_and_directors1(actor_director: pd.DataFrame) -> pd.DataFrame:
    grouped = actor_director.groupby(by=["actor_id", "director_id"]).size().reset_index(name="counts")
    return grouped[grouped["counts"] >= 3][["actor_id", "director_id"]]

def actors_and_directors2(actor_director: pd.DataFrame) -> pd.DataFrame:
    grouped = actor_director.groupby(by=["actor_id", "director_id"]).agg(
        counts=("timestamp", "size"),
        our_sum=("timestamp", "sum")
    ).reset_index()
    return grouped


path = Path(__file__).parent / "data" / "1050. ActorDirector.xlsx"
actor_director = pd.read_excel(path)
print(actors_and_directors2(actor_director))