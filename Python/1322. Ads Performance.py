# Table: Ads
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | ad_id         | int     |
# | user_id       | int     |
# | action        | enum    |
# +---------------+---------+
# (ad_id, user_id) is the primary key (combination of columns with unique values) for this table.
# Each row of this table contains the ID of an Ad, the ID of a user, and the action taken by this user regarding this Ad.
# The action column is an ENUM (category) type of ('Clicked', 'Viewed', 'Ignored').

# A company is running Ads and wants to calculate the performance of each Ad.
#
# Performance of the Ad is measured using Click-Through Rate (CTR) where:
#
# Write a solution to find the ctr of each Ad. Round ctr to two decimal points.
#
# Return the result table ordered by ctr in descending order and by ad_id in ascending order in case of a tie.
import pandas as pd
from pathlib import Path
import os
from collections import defaultdict

def ads_performance(ads: pd.DataFrame) -> pd.DataFrame:
    c = "Clicked"; v = "Viewed"
    grouped = ads.groupby(by="ad_id", as_index=False).agg(count=("action", lambda x: {i: list(x).count(i) for i in list(x) if i in [c, v]}))
    grouped["ctr"] = grouped["count"].apply(lambda x: 0 if ((y := sum([x.get(c, 0), x.get(v, 0)])) == 0) else (round(((x.get(c, 0)) / (y))*100, 2)))
    return grouped[["ad_id", "ctr"]].sort_values(by=["ctr", "ad_id"], ascending=(False, True), inplace=False)


path = Path(os.getcwd()) / "data" / "1322. Ads Performance.xlsx"
ads = pd.read_excel(path)
print(ads_performance(ads))


