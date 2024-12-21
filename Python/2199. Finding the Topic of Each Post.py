# Table: Keywords
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | topic_id    | int     |
# | word        | varchar |
# +-------------+---------+
# (topic_id, word) is the primary key (combination of columns with unique values) for this table.
# Each row of this table contains the id of a topic and a word that is used to express this topic.
# There may be more than one word to express the same topic and one word may be used to express multiple topics.
#
#
# Table: Posts
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | post_id     | int     |
# | content     | varchar |
# +-------------+---------+
# post_id is the primary key (column with unique values) for this table.
# Each row of this table contains the ID of a post and its content.
# Content will consist only of English letters and spaces.
#
#
# Leetcode has collected some posts from its social media website and is interested in finding the topics of each post.
# Each topic can be expressed by one or more keywords. If a keyword of a certain topic exists in the content of a post
# (case insensitive) then the post has this topic.
#
# Write a solution to find the topics of each post according to the following rules:
#
# If the post does not have keywords from any topic, its topic should be "Ambiguous!".
# If the post has at least one keyword of any topic, its topic should be a string of the IDs of its topics sorted
# in ascending order and separated by commas ','. The string should not contain duplicate IDs.
# Return the result table in any order.

import pandas as pd
from pathlib import Path
import os

def find_topic(keywords: pd.DataFrame, posts: pd.DataFrame) -> pd.DataFrame:
    posts["set"] = posts["content"].apply(lambda x: set([i.lower() for i in x.split()]))
    merged = pd.merge(
        left=posts,
        right=keywords,
        how="cross"
    )
    merged["bool"] = merged.apply(lambda x: 1 if x["word"].lower() in x["set"] else 0, axis=1)
    grouped = merged.loc[merged["bool"] != 0].groupby(by="post_id", as_index=False).agg(topic=("topic_id", lambda x: ",".join(map(str, x.sort_values().drop_duplicates()))))
    return pd.merge(
        left=posts[["post_id"]],
        right=grouped,
        how="left",
        on="post_id"
    ).fillna("Ambiguous!")


path = Path(os.getcwd()) / "data" / "2199. Finding the Topic of Each Post.xlsx"
keywords = pd.read_excel(path, sheet_name="Keywords")
posts = pd.read_excel(path, sheet_name="Posts")
print(find_topic(keywords, posts).to_string())