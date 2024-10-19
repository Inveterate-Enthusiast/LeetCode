# Table: Files
#
# +-------------+---------+
# | Column Name | Type    |
# +-- ----------+---------+
# | file_name   | varchar |
# | content     | text    |
# +-------------+---------+
# file_name is the column with unique values of this table.
# Each row contains file_name and the content of that file.
# Write a solution to find the number of files that have at least one occurrence of the words 'bull' and 'bear' as a standalone word,
# respectively, disregarding any instances where it appears without space on either side (e.g. 'bullet', 'bears', 'bull.', or 'bear'
# at the beginning or end of a sentence will not be considered)
#
# Return the word 'bull' and 'bear' along with the corresponding number of occurrences in any order.
import pandas as pd
import re

def count_occurrences(files: pd.DataFrame) -> pd.DataFrame:
    bull = r".* bull .*"
    bear = r".* bear .*"
    files["bull"] = files["content"].apply(lambda x: len(re.findall(bull, x)))
    files["bear"] = files["content"].apply(lambda x: len(re.findall(bear, x)))
    return pd.DataFrame({
        "word": ["bull", "bear"],
        "count": [files["bull"].sum(), files["bear"].sum()]
    })
