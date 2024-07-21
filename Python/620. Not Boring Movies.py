# Table: Cinema
#
# +----------------+----------+
# | Column Name    | Type     |
# +----------------+----------+
# | id             | int      |
# | movie          | varchar  |
# | description    | varchar  |
# | rating         | float    |
# +----------------+----------+
# id is the primary key (column with unique values) for this table.
# Each row contains information about the name of a movie, its genre, and its rating.
# rating is a 2 decimal places float in the range [0, 10]

# Write a solution to report the movies with an odd-numbered ID and a description that is not "boring".
#
# Return the result table ordered by rating in descending order.
import pandas as pd
from pathlib import Path

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    return cinema[
        (cinema["description"] != "boring") &
        (~cinema["id"]%2)
    ].sort_values(by="rating", ascending=False)

path = Path(__file__).parent / "data" / "620. Cinema.xlsx"
cinema = pd.read_excel(path)
print(not_boring_movies(cinema))
