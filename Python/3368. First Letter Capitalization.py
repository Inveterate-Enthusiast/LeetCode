# Table: user_content
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | content_id  | int     |
# | content_text| varchar |
# +-------------+---------+
# content_id is the unique key for this table.
# Each row contains a unique ID and the corresponding text content.
# Write a solution to transform the text in the content_text column by applying the following rules:
#
# Convert the first letter of each word to uppercase
# Keep all other letters in lowercase
# Preserve all existing spaces
# Note: There will be no special character in content_text.
#
# Return the result table that includes both the original content_text and the modified text where each word starts with a capital letter.

import pandas as pd

def process_text(user_content: pd.DataFrame) -> pd.DataFrame:
    user_content["converted_text"] = user_content["content_text"].apply(lambda x: x.title())
    return user_content.rename(columns={"content_text": "original_text"})

def process_text1(user_content: pd.DataFrame) -> pd.DataFrame:
    user_content["converted_text"] = user_content["content_text"].str.title()
    return user_content.rename(columns={"content_text": "original_text"})