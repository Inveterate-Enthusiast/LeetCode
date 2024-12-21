# Table: Wineries
#
# +-------------+----------+
# | Column Name | Type     |
# +-------------+----------+
# | id          | int      |
# | country     | varchar  |
# | points      | int      |
# | winery      | varchar  |
# +-------------+----------+
# id is column of unique values for this table.
# This table contains id, country, points, and winery.
# Write a solution to find the top three wineries in each country based on their total points.
# If multiple wineries have the same total points, order them by winery name in ascending order.
# If there's no second winery, output 'No second winery,' and if there's no third winery, output 'No third winery.'
#
# Return the result table ordered by country in ascending order.


import pandas as pd
import numpy as np

def top_three_wineries(wineries: pd.DataFrame) -> pd.DataFrame:
    grouped = (wineries
               .groupby(by=["winery", "country"], as_index=False)
               .agg(total_points=("points", "sum"))
               .sort_values(by=["total_points", "winery"], ascending=[False, True]))
    grouped["rank"] = grouped.groupby(by="country", as_index=False).transform("cumcount") + 1
    grouped["title"] = np.where(
        grouped["rank"] == 1, "top_winery",
        np.where(
            grouped["rank"] == 2, "second_winery",
            np.where(
                grouped["rank"] == 3, "third_winery",
                "0"
            )
        )
    )
    grouped["value"] = grouped.apply(lambda x: x["winery"] + " (" + str(x["total_points"]) + ")", axis=1)
    titles = ["top_winery", "second_winery", "third_winery"]
    pivot = grouped.loc[grouped["title"] != "0"].pivot_table(values="value", index="country", columns="title", aggfunc="max")
    for col in titles:
        if not pivot.get(col):
            pivot[col] = pd.NA
    pivot["second_winery"] = pivot.second_winery.fillna("No second winery")
    pivot["third_winery"] = pivot.third_winery.fillna("No third winery")
    pivot = pivot[titles]
    return pivot.reset_index().sort_values(by="country", ascending=True)