# Table: TeamPoints
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | team_id     | int     |
# | name        | varchar |
# | points      | int     |
# +-------------+---------+
# team_id contains unique values.
# Each row of this table contains the ID of a national team, the name of the country it represents,
# and the points it has in the global rankings. No two teams will represent the same country.
#
#
# Table: PointsChange
#
# +---------------+------+
# | Column Name   | Type |
# +---------------+------+
# | team_id       | int  |
# | points_change | int  |
# +---------------+------+
# team_id contains unique values.
# Each row of this table contains the ID of a national team and the change in its points in the global rankings.
# points_change can be:
# - 0: indicates no change in points.
# - positive: indicates an increase in points.
# - negative: indicates a decrease in points.
# Each team_id that appears in TeamPoints will also appear in this table.
#
#
# The global ranking of a national team is its rank after sorting all the teams by their points in descending order.
# If two teams have the same points, we break the tie by sorting them by their name in lexicographical order.
#
# The points of each national team should be updated based on its corresponding points_change value.
#
# Write a solution to calculate the change in the global rankings after updating each team's points.
#
# Return the result table in any order.
import pandas as pd

def global_ratings_change(team_points: pd.DataFrame, points_change: pd.DataFrame) -> pd.DataFrame:
    first_ranking = team_points.sort_values(by=["points", "name"], ascending=[False, True]).reset_index(drop=True)
    first_ranking["row"] = first_ranking.index + 1

    second_ranking = pd.merge(
        left=team_points,
        right=points_change,
        how="outer",
        on="team_id"
    )
    second_ranking["points"] = second_ranking["points"] + second_ranking["points_change"]
    second_ranking = second_ranking.sort_values(by=["points", "name"], ascending=[False, True]).reset_index(drop=True)
    second_ranking["row"] = second_ranking.index + 1

    merged = pd.merge(
        left=first_ranking,
        right=second_ranking,
        how="outer",
        on="team_id",
        suffixes=("_first", "_sec")
    ).fillna(0)
    merged["rank_diff"] = merged["row_first"] - merged["row_sec"]
    merged["name"] = merged.apply(lambda x: x["name_first"] if x["name_first"] else x["name_sec"], axis=1)
    return merged[["team_id", "name", "rank_diff"]]
