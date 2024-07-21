# Table: Weather
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | id            | int     |
# | recordDate    | date    |
# | temperature   | int     |
# +---------------+---------+
# id is the column with unique values for this table.
# There are no different rows with the same recordDate.
# This table contains information about the temperature on a certain day.

# Write a solution to find all dates' Id with higher temperatures compared to its previous dates (yesterday).
#
# Return the result table in any order.

import pandas as pd
from datetime import datetime
from typing import Optional

def find_prev_date(current_date: pd.DataFrame, all_dates: pd.DataFrame) -> Optional[datetime]:
    prev_dates = all_dates[all_dates < current_date]
    if not prev_dates.empty:
        return prev_dates.max()
    else:
        return None

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame: # хорошее решение, но неправильное для этой задачи
    weather["prev_recordDate"] = weather["recordDate"].apply(find_prev_date, all_dates=weather["recordDate"])
    weather["prev_temperature"] = pd.merge(left=weather[["recordDate", "temperature"]], right=weather["prev_recordDate"], left_on="recordDate", right_on="prev_recordDate", how="right")[["temperature"]]
    return weather[weather["temperature"] > weather["prev_temperature"]][["id"]]

def rising_temperature1(weather: pd.DataFrame) -> pd.DataFrame:
    weather["prev_recordDate"] = weather["recordDate"].apply(lambda x: x - pd.Timedelta(1, "D"))
    weather["prev_temperature"] = pd.merge(
        left=weather[["recordDate", "temperature"]],
        right=weather[["prev_recordDate"]],
        left_on="recordDate",
        right_on="prev_recordDate",
        how="right"
    )[["temperature"]]
    return weather[weather["temperature"] > weather["prev_temperature"]][["id"]]

def rising_temperature2(weather: pd.DataFrame) -> pd.DataFrame:
    weather.sort_values(by="recordDate", inplace=True, ascending=True, na_position="first")
    return weather[
        (weather["temperature"].diff(periods=1) > 0) &
        (weather["recordDate"].diff(periods=1).dt.days == 1)
    ][["id"]]

Weather = pd.DataFrame({
    "id": [1, 2, 3, 4],
    "recordDate": [datetime(2015,1,1), datetime(2015,1,2), datetime(2015,1,3), datetime(2015,1,4)],
    "temperature": [10, 25, 20, 30]
})

# Weather["recordDate"] = pd.to_datetime(Weather["recordDate"])

print(rising_temperature2(Weather))