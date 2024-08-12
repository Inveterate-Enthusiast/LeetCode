# Table: Olympic
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | country       | varchar |
# | gold_medals   | int     |
# | silver_medals | int     |
# | bronze_medals | int     |
# +---------------+---------+
# In SQL, country is the primary key for this table.
# Each row in this table shows a country name and the number of gold, silver, and bronze medals it won in the Olympic games.
#
#
# The Olympic table is sorted according to the following rules:
#
# The country with more gold medals comes first.
# If there is a tie in the gold medals, the country with more silver medals comes first.
# If there is a tie in the silver medals, the country with more bronze medals comes first.
# If there is a tie in the bronze medals, the countries with the tie are sorted in ascending order lexicographically.
# Write a solution to sort the Olympic table.
import pandas as pd

def sort_table(olympic: pd.DataFrame) -> pd.DataFrame:
    return olympic.sort_values(by=["gold_medals", "silver_medals", "bronze_medals", "country"],
                               ascending=[False, False, False, True])
