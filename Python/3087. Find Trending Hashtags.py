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
# Write a solution to find the top 3 trending hashtags in February 2024. Each tweet only contains one hashtag.
#
# Return the result table orderd by count of hashtag, hashtag in descending order.
import pandas as pd
import re

def find_trending_hashtags(tweets: pd.DataFrame) -> pd.DataFrame:
    pattern = r"#\w+"
    tweets["hashtag"] = tweets["tweet"].apply(lambda x: re.search(pattern, x).group() if re.search(pattern, x) else None)
    grouped = tweets.groupby(by="hashtag", as_index=False).agg(hashtag_count=("hashtag", "count"))
    grouped["rank"] = grouped["hashtag_count"].rank(method="dense", ascending=False)
    return grouped.loc[grouped["rank"] <= 3].drop(labels="rank", axis=1).sort_values(by=["hashtag_count", "hashtag"], ascending=[False, False]).head(3)

