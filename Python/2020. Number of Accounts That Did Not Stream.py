# Table: Subscriptions
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | account_id  | int  |
# | start_date  | date |
# | end_date    | date |
# +-------------+------+
# account_id is the primary key column for this table.
# Each row of this table indicates the start and end dates of an account's subscription.
# Note that always start_date < end_date.
#
#
# Table: Streams
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | session_id  | int  |
# | account_id  | int  |
# | stream_date | date |
# +-------------+------+
# session_id is the primary key column for this table.
# account_id is a foreign key from the Subscriptions table.
# Each row of this table contains information about the account and the date associated with a stream session.
#
#
# Write an SQL query to report the number of accounts that bought a subscription in 2021 but did not have any stream session.
import pandas as pd

def find_target_accounts(subscriptions: pd.DataFrame, streams: pd.DataFrame) -> pd.DataFrame:
    tw = 2021
    streams["year"] = pd.to_datetime(streams["stream_date"]).dt.year
    new_grouped = streams.loc[streams["year"] == tw].copy()
    subscriptions["start_year"] = pd.to_datetime(subscriptions["start_date"]).dt.year
    subscriptions["end_year"] = pd.to_datetime(subscriptions["end_date"]).dt.year
    filtered = subscriptions.loc[
        (subscriptions["start_year"] == tw) | (subscriptions["end_year"] == tw)
    ].copy()
    merged = pd.merge(
        left=filtered,
        right=new_grouped,
        how="inner",
        on="account_id"
    )
    new_merged = merged.loc[
        (merged["year"] <= merged["end_year"]) | (merged["year"] >= merged["start_year"])
    ].copy()
    merged_grouped = new_merged.groupby(by="account_id", as_index=False).agg(count=("session_id", "nunique"))
    new_merged = pd.merge(
        left=filtered,
        right=merged_grouped,
        how="left",
        on="account_id"
    )
    return pd.DataFrame({
        "accounts_count": [new_merged.loc[new_merged["count"].isna()].shape[0]]
    })

