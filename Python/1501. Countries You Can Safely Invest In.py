# Table Person:
#
# +----------------+---------+
# | Column Name    | Type    |
# +----------------+---------+
# | id             | int     |
# | name           | varchar |
# | phone_number   | varchar |
# +----------------+---------+
# id is the column of unique values for this table.
# Each row of this table contains the name of a person and their phone number.
# Phone number will be in the form 'xxx-yyyyyyy' where xxx is the country code (3 characters) and yyyyyyy is the phone number (7 characters) where x and y are digits. Both can contain leading zeros.
#
#
# Table Country:
#
# +----------------+---------+
# | Column Name    | Type    |
# +----------------+---------+
# | name           | varchar |
# | country_code   | varchar |
# +----------------+---------+
# country_code is the column of unique values for this table.
# Each row of this table contains the country name and its code. country_code will be in the form 'xxx' where x is digits.
#
#
# Table Calls:
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | caller_id   | int  |
# | callee_id   | int  |
# | duration    | int  |
# +-------------+------+
# This table may contain duplicate rows.
# Each row of this table contains the caller id, callee id and the duration of the call in minutes. caller_id != callee_id
#
#
# A telecommunications company wants to invest in new countries. The company intends to invest in the countries where the average call duration of the calls in this country is strictly greater than the global average call duration.
#
# Write a solution to find the countries where this company can invest.
#
# Return the result table in any order.
import pandas as pd
import re

def find_safe_countries(person: pd.DataFrame, country: pd.DataFrame, calls: pd.DataFrame) -> pd.DataFrame:
    pattern = r"(\d{3})-.*"
    person["country_code"] = person["phone_number"].apply(lambda x: re.match(pattern, x).groups()[0])
    calls = pd.concat([calls[["caller_id", "duration"]].rename(columns={"caller_id": "id"}),
                      calls[["callee_id", "duration"]].rename(columns={"callee_id": "id"})])
    merged_calls = pd.merge(
        left=calls,
        right=person[["id", "country_code"]],
        how="left",
        on="id"
    )
    avg_duration = merged_calls["duration"].mean()
    grouped = merged_calls.groupby(by="country_code", as_index=False).agg(duration_avg=("duration", "mean"))
    return pd.merge(
        left=grouped.loc[grouped["duration_avg"] > avg_duration],
        right=country.rename(columns={"name": "country"}),
        how="left",
        on="country_code"
    )[["country"]]

