# Table: Tweets
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | user_id     | int     |
# | tweet_id    | int     |
# | tweet_date  | date    |
# | tweet       | varchar |
# +-------------+---------+
# tweet_id is the primary key (column with unique values) for this table.
# Each row of this table contains user_id, tweet_id, tweet_date and tweet.
# It is guaranteed that all tweet_date are valid dates in February 2024.
#
# Write a solution to find the top 3 trending hashtags in February 2024. Every tweet may contain several hashtags.
#
# Return the result table ordered by count of hashtag, hashtag in descending order.


import pandas as pd
import re
from pathlib import Path
import os

def find_trending_hashtags(tweets: pd.DataFrame) -> pd.DataFrame:
    pattern = r"#[\w]+"
    tweets["hashtag"] = tweets["tweet"].apply(lambda x: list(re.findall(pattern, x)))
    exploded = tweets.explode(["hashtag"])
    grouped = exploded.loc[(exploded["tweet_date"].dt.year == 2024) & (exploded["tweet_date"].dt.month == 2)].groupby(by="hashtag", as_index=False).agg(count=("hashtag", "count"))
    return grouped.sort_values(by=["count", "hashtag"], ascending=[False, False]).head(3)

tweets = pd.read_excel(Path(os.getcwd()) / "data" / "3103. Find Trending Hashtags II.xlsx")
print(find_trending_hashtags(tweets))