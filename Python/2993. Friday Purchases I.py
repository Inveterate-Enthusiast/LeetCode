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
# Output only weeks that include at least one purchase on a Friday.
#
# Return the result table ordered by week of month in ascending order.
import pandas as pd

def friday_purchases(purchases: pd.DataFrame) -> pd.DataFrame:
    filtered = purchases.loc[
        (purchases["purchase_date"].dt.year == 2023)
        & (purchases["purchase_date"].dt.month == 11)
        & (purchases["purchase_date"].dt.weekday == 4)
    ]
    filtered["first_week"] = pd.to_datetime(filtered["purchase_date"].dt.strftime("%Y-%m-01")).dt.isocalendar().week
    filtered["week_of_month"] = filtered["purchase_date"].dt.isocalendar().week - filtered["first_week"] + 1
    grouped = filtered.groupby(by=["week_of_month", "purchase_date"], as_index=False).agg(total_amount=("amount_spend", "sum"))
    return grouped.sort_values(by="week_of_month")