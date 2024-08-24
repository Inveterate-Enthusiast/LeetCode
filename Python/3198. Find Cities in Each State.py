# Table: cities
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | state       | varchar |
# | city        | varchar |
# +-------------+---------+
# (state, city) is the primary key (combination of columns with unique values) for this table.
# Each row of this table contains the state name and the city name within that state.
# Write a solution to find all the cities in each state and combine them into a single comma-separated string.
#
# Return the result table ordered by state in ascending order.
import pandas as pd

def find_cities(cities: pd.DataFrame) -> pd.DataFrame:
    return (cities
            .groupby(by="state", as_index=False)
            .agg(cities=("city", lambda x: ", ".join(sorted(list(x), reverse=False))))
            .sort_values(by="state", ascending=True))