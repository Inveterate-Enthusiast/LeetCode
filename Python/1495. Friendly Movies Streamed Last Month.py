# Table: TVProgram
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | program_date  | date    |
# | content_id    | int     |
# | channel       | varchar |
# +---------------+---------+
# (program_date, content_id) is the primary key (combination of columns with unique values) for this table.
# This table contains information of the programs on the TV.
# content_id is the id of the program in some channel on the TV.
#
# Table: Content
#
# +------------------+---------+
# | Column Name      | Type    |
# +------------------+---------+
# | content_id       | varchar |
# | title            | varchar |
# | Kids_content     | enum    |
# | content_type     | varchar |
# +------------------+---------+
# content_id is the primary key (column with unique values) for this table.
# Kids_content is an ENUM (category) of types ('Y', 'N') where:
# 'Y' means is content for kids otherwise 'N' is not content for kids.
# content_type is the category of the content as movies, series, etc.

# Write a solution to report the distinct titles of the kid-friendly movies streamed in June 2020.
#
# Return the result table in any order.
import pandas as pd
from datetime import datetime
from pathlib import Path
import os
import numpy as np

def friendly_movies(tv_program: pd.DataFrame, content: pd.DataFrame) -> pd.DataFrame:
    content["content_id"] = pd.to_numeric(content["content_id"])
    merged = pd.merge(
        left=tv_program,
        right=content,
        on="content_id",
        how="left",
        copy=False
    )
    return merged[
        (merged["program_date"].dt.to_period("M") == pd.Period(datetime(2020, 6, 1), freq="M")) &
        (merged["Kids_content"] == "Y") &
        (merged["content_type"] == "Movies")
    ][["title"]].drop_duplicates()

path = Path(os.getcwd()) / "data" / "1495. Friendly Movies Streamed Last Month.xlsx"
tv_program = pd.read_excel(path, sheet_name="TVProgram")
content = pd.read_excel(path, sheet_name="Content")
print(friendly_movies(tv_program, content))


