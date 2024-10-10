# Table: Weather
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | city_id     | int  |
# | day         | date |
# | degree      | int  |
# +-------------+------+
# (city_id, day) is the primary key (combination of columns with unique values) for this table.
# Each row in this table contains the degree of the weather of a city on a certain day.
# All the degrees are recorded in the year 2022.
#
#
# Write a solution to report the day that has the maximum recorded degree in each city.
# If the maximum degree was recorded for the same city multiple times, return the earliest day among them.
#
# Return the result table ordered by city_id in ascending order.
import pandas as pd

def find_the_first_day(weather: pd.DataFrame) -> pd.DataFrame:
    sorted = weather.sort_values(by=["degree", "day"], ascending=[False, True])
    sorted["rank"] = sorted.groupby(by="city_id", as_index=False)["degree"].rank(method="first", ascending=False)
    return sorted.loc[sorted["rank"] == 1].drop(labels="rank", axis=1).sort_values(by="city_id", ascending=True)

