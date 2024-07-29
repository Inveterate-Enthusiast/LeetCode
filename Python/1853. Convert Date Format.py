# Table: Days
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | day         | date |
# +-------------+------+
# day is the column with unique values for this table.
#
#
# Write a solution to convert each date in Days into a string formatted as "day_name, month_name day, year".
#
# Return the result table in any order.
import pandas as pd

def convert_date_format(days: pd.DataFrame) -> pd.DataFrame:
    days["day"] = days["day"].dt.strftime("%A, %B %-d, %Y")
    return days