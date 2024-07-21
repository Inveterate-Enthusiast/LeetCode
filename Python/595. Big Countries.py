# Table: World
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | name        | varchar |
# | continent   | varchar |
# | area        | int     |
# | population  | int     |
# | gdp         | bigint  |
# +-------------+---------+
# name is the primary key (column with unique values) for this table.
# Each row of this table gives information about the name of a country,
# the continent to which it belongs, its area, the population, and its GDP value.

# A country is big if:
#
# it has an area of at least three million (i.e., 3000000 km2), or
# it has a population of at least twenty-five million (i.e., 25000000).
# Write a solution to find the name, population, and area of the big countries.
#
# Return the result table in any order.
import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    return world[(world["area"] >= 3_000_000) | (world["population"] >= 25_000_000)][["name", "population", "area"]]

def big_countries1(world: pd.DataFrame) -> pd.DataFrame:
    world.drop(index=world[(world["area"] < 3_000_000) & (world["population"] < 25_000_000)].index, axis=0, inplace=True)
    return world[["name", "population", "area"]]

World = pd.DataFrame({
    "name": ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola"],
    "continent": ["Asia", "Europe", "Africa", "Europe", "Africa"],
    "area": [652_234, 28_748, 2_381_741, 468, 1_246_700],
    "population": [25_500_100, 2_831_741, 37_100_000, 78_115, 20_609_294],
    "gdp": [20343000000, 12960000000, 188681000000, 3712000000, 100990000000]
})

print(big_countries1(World))