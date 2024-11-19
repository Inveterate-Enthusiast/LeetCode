# Table: cities
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | state       | varchar |
# | city        | varchar |
# +-------------+---------+
# (state, city) is the combination of columns with unique values for this table.
# Each row of this table contains the state name and the city name within that state.
# Write a solution to find all the cities in each state and analyze them based on the following requirements:
#
# Combine all cities into a comma-separated string for each state.
# Only include states that have at least 3 cities.
# Only include states where at least one city starts with the same letter as the state name.
# Return the result table ordered by the count of matching-letter cities in descending order and then by state name in ascending order.

import pandas as pd

def state_city_analysis(cities: pd.DataFrame) -> pd.DataFrame:
    cities["count"] = cities.groupby(by="state", as_index=False)["city"].transform("count")
    cities["first_letter_match"] = cities["city"].str[0] == cities["state"].str[0]
    grouped = (cities
               .loc[cities["count"] >= 3]
               .groupby(by="state", as_index=False)
               .agg(
        cities=("city", lambda x: ", ".join(sorted(x))),
        matching_letter_count=("first_letter_match", "sum")))
    return grouped.loc[grouped["matching_letter_count"] > 0].sort_values(by=["matching_letter_count", "state"], ascending=[False, True])