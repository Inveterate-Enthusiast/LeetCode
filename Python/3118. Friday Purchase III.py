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
# Each row contains user_id, purchase_date, and amount_spend.
# Table: Users
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | user_id     | int  |
# | membership  | enum |
# +-------------+------+
# user_id is the primary key for this table.
# membership is an ENUM (category) type of ('Standard', 'Premium', 'VIP').
# Each row of this table indicates the user_id, membership type.
# Write a solution to calculate the total spending by Premium and VIP members on each Friday of every week in November 2023.
# If there are no purchases on a particular Friday by Premium or VIP members, it should be considered as 0.
#
# Return the result table ordered by week of the month,  and membership in ascending order.
import pandas as pd
from datetime import datetime

def friday_purchases(purchases: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    start_date = datetime(2023, 11, 1)
    end_date = start_date + pd.offsets.MonthEnd(0)
    calendar = pd.DataFrame({
        "date": pd.date_range(start_date, end_date)
    })
    calendar["friday"] = calendar["date"].dt.day_name() == "Friday"
    calendar["first_date"] = calendar["date"].min()
    calendar["first_week"] = calendar["first_date"].dt.isocalendar().week
    calendar["week_of_month"] = calendar["date"].dt.isocalendar().week - calendar["first_week"] + 1
    calendar_merged = pd.merge(
        left=calendar.loc[calendar["friday"], ["date", "week_of_month"]],
        right=pd.DataFrame({"membership": ["VIP", "Premium"]}),
        how="cross"
    )

    purchases["friday"] = purchases["purchase_date"].dt.day_name() == "Friday"
    merged = pd.merge(
        left=purchases.loc[purchases["friday"]],
        right=users,
        how="left",
        on="user_id"
    )
    merged["membership"] = merged["membership"].astype("str")
    grouped = (merged
               .loc[merged["membership"].isin({"Premium", "VIP"})]
               .groupby(by=["membership", "purchase_date"], as_index=False).agg(total_amount=("amount_spend", "sum"))
               .rename(columns={"purchase_date": "date"}))

    result = pd.merge(
        left=calendar_merged,
        right=grouped,
        how="left",
        on=["date", "membership"]
    ).fillna(0)

    return result.drop(labels="date", axis=1).sort_values(by=["week_of_month", "membership"], ascending=[True, True])

start_date = datetime(2023,11,1)
end_date = start_date + pd.offsets.MonthEnd(0)
calendar = pd.DataFrame({
    "date": pd.date_range(start_date, end_date)
})
calendar["friday"] = calendar["date"].dt.day_name() == "Friday"
calendar["first_date"] = calendar["date"].min()
calendar["first_week"] = calendar["first_date"].dt.isocalendar().week
calendar["week_of_month"] = calendar["date"].dt.isocalendar().week - calendar["first_week"] + 1
print(calendar.loc[calendar["friday"]])