# Table: Views
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | article_id    | int     |
# | author_id     | int     |
# | viewer_id     | int     |
# | view_date     | date    |
# +---------------+---------+
# This table may have duplicate rows.
# Each row of this table indicates that some viewer viewed an article (written by some author) on some date.
# Note that equal author_id and viewer_id indicate the same person.
#
#
# Write a solution to find all the people who viewed more than one article on the same date.
#
# Return the result table sorted by id in ascending order.
import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    views["bool"] = views.groupby(by=["viewer_id", "view_date"], as_index=False)["article_id"].transform(lambda x: x.nunique() > 1)
    return views.loc[views["bool"], ["viewer_id"]].drop_duplicates(subset="viewer_id", keep="first").sort_values(by="viewer_id", ascending=True).rename(columns={"viewer_id": "id"})

def article_views1(views: pd.DataFrame) -> pd.DataFrame:
    grouped = (views
               .groupby(by=["viewer_id", "view_date"], as_index=False)
               .agg(our_bool=("article_id", "nunique")))
    return (grouped
            .loc[grouped["our_bool"] > 1, ["viewer_id"]]
            .drop_duplicates(subset="viewer_id", keep="first")
            .rename(columns={"viewer_id": "id"})
            .sort_values(by="id", ascending=True))