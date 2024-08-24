# Table: Tweets
#
# +----------------+---------+
# | Column Name    | Type    |
# +----------------+---------+
# | tweet_id       | int     |
# | content        | varchar |
# +----------------+---------+
# tweet_id is the primary key (column with unique values) for this table.
# This table contains all the tweets in a social media app.
# Write a solution to find invalid tweets. A tweet is considered invalid if it meets any of the following criteria:
#
# It exceeds 140 characters in length.
# It has more than 3 mentions.
# It includes more than 3 hashtags.
# Return the result table ordered by tweet_id in ascending order.
import pandas as pd
from pathlib import Path
import os
import re

def find_invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    mentions_pattern = r".*?@.+@.+@.+@.+"
    hashtags_pattern = r".*?#.+#.+#.+#.+"
    tweets[["len", "mentions", "hashtags"]] = tweets["content"].apply(lambda x: pd.Series(data=[len(x) > 140,
                                                                                                bool(re.match(mentions_pattern, x)),
                                                                                                bool(re.match(hashtags_pattern, x))]))
    return tweets.loc[tweets["len"] | tweets["mentions"] | tweets["hashtags"], ["tweet_id"]].sort_values(by="tweet_id", ascending=True)

def find_invalid_tweets1(tweets: pd.DataFrame) -> pd.DataFrame:
    return tweets.loc[
        (tweets["content"].str.len() > 140) |
        (tweets["content"].str.count("@") > 3) |
        (tweets["content"].str.count("#") > 3),
        ["tweet_id"]
    ].sort_values(by="tweet_id", ascending=True)


tweets = pd.read_excel(Path(os.getcwd()) / "data" / "3150. Invalid Tweets II.xlsx")
print(find_invalid_tweets1(tweets).to_string())