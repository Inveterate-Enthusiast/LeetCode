# Table: Purchases
#
# +---------------+------+
# | Column Name   | Type |
# +---------------+------+
# | user_id       | int  |
# | purchase_date | date |
# | amount_spend  | int  |
# +---------------+------+
# (user_id, purchase_date, amount_spend) is the primary key (combination of columns with unique values) for this table.
# purchase_date will range from November 1, 2023, to November 30, 2023, inclusive of both dates.
# Each row contains user id, purchase date, and amount spend.
# Write a solution to calculate the total spending by users on each Friday of every week in November 2023.
# If there are no purchases on a particular Friday of a week, it will be considered as 0.
#
# Return the result table ordered by week of month in ascending order.


import pandas as pd
from datetime import datetime

def friday_purchases(purchases: pd.DataFrame) -> pd.DataFrame:
    dates = pd.DataFrame({
        "purchase_date": pd.date_range(start=datetime(2023, 11, 1),
                                       end=(datetime(2023,12,1) - pd.Timedelta(value=1, unit="day")),
                                       freq="d")
    })
    dates["day_of_week"] = dates["purchase_date"].dt.dayofweek
    dates["week_of_year"] = dates["purchase_date"].dt.isocalendar().week
    dates["start_time"] = dates["purchase_date"].dt.to_period("M").dt.start_time
    dates["first_week"] = dates["start_time"].dt.isocalendar().week
    dates["week_of_month"] = dates["week_of_year"] - dates["first_week"] + 1
    grouped = purchases.groupby(by="purchase_date", as_index=False).agg(total_amount=("amount_spend", "sum"))
    merged = pd.merge(
        left=dates.loc[dates["day_of_week"] == 4, ["week_of_month", "purchase_date"]],
        right=grouped,
        how="left",
        on="purchase_date"
    ).fillna(0)
    return merged.sort_values(by="week_of_month", ascending=True)