# Table: MyNumbers
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | num         | int  |
# +-------------+------+
# This table may contain duplicates (In other words, there is no primary key for this table in SQL).
# Each row of this table contains an integer.

# A single number is a number that appeared only once in the MyNumbers table.
#
# Find the largest single number. If there is no single number, report null.
import pandas as pd
from pathlib import Path

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    grouped = my_numbers.groupby(by="num", as_index=False).size()
    grouped.drop(index=grouped[grouped["size"] != 1].index, inplace = True)
    return pd.DataFrame({
        "num": [grouped["num"].max()]
    })

def biggest_single_number1(my_numbers: pd.DataFrame) -> pd.DataFrame:
    return my_numbers.drop_duplicates(subset="num", keep=False, inplace=False).max().to_frame(name="num")

path = Path(__file__).parent / "data" / "619. MyNumbers.xlsx"
my_numbers = pd.read_excel(path)
print(biggest_single_number1(my_numbers))
