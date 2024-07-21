# Table: Stadium
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | id            | int     |
# | visit_date    | date    |
# | people        | int     |
# +---------------+---------+
# visit_date is the column with unique values for this table.
# Each row of this table contains the visit date and visit id to the stadium with the number of people during the visit.
# As the id increases, the date increases as well.
#
#
# Write a solution to display the records with three or more rows with consecutive id's, and the number of people is greater than or equal to 100 for each.
#
# Return the result table ordered by visit_date in ascending order.
import pandas as pd
from pathlib import Path
import os

def human_traffic(stadium: pd.DataFrame) -> pd.DataFrame:
    stadium.drop(index=stadium[stadium["people"] < 100].index, inplace=True)
    stadium["rank"] = stadium["id"].rank(method="dense")
    stadium["dif"] = stadium.apply(lambda x: x["id"] - x["rank"], axis=1)
    print(stadium)
    return (stadium
            .groupby(by="dif", as_index=False)
            .filter(lambda x: len(x) >= 3)
            .sort_values(by="visit_date", ascending=True)
            .loc[:, ["id", "visit_date", "people"]])

path = Path(os.getcwd()) / "data" / "601. Human Traffic of Stadium.xlsx"
stadium = pd.read_excel(path)
print(human_traffic(stadium))