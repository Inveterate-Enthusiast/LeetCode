# Table: Teams
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | team_name   | varchar |
# +-------------+---------+
# team_name is the column with unique values of this table.
# Each row of this table shows the name of a team.
#
#
# Write a solution to report all the possible matches of the league.
# Note that every two teams play two matches with each other,
# with one team being the home_team once and the other time being the away_team.
#
# Return the result table in any order.
import pandas as pd

def find_all_matches(teams: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(
        left=teams.rename(columns={"team_name": "home_team"}),
        right=teams.rename(columns={"team_name": "away_team"}),
        how="cross"
    )
    return merged.drop(index=merged.loc[merged["home_team"] == merged["away_team"]].index)