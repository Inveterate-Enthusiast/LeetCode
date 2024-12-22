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
# Convert the first letter of each word to uppercase and the remaining letters to lowercase
# Special handling for words containing special characters:
# For words connected with a hyphen -, both parts should be capitalized (e.g., top-rated → Top-Rated)
# All other formatting and spacing should remain unchanged
# Return the result table that includes both the original content_text and the modified text following the above rules.


import pandas as pd

def capitalize_content(user_content: pd.DataFrame) -> pd.DataFrame:
    user_content["converted_text"] = user_content["content_text"].str.title()
    return user_content.rename(columns={"content_text": "original_text"})