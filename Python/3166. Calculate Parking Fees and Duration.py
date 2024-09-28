# Table: ParkingTransactions
#
# +--------------+-----------+
# | Column Name  | Type      |
# +--------------+-----------+
# | lot_id       | int       |
# | car_id       | int       |
# | entry_time   | datetime  |
# | exit_time    | datetime  |
# | fee_paid     | decimal   |
# +--------------+-----------+
# (lot_id, car_id, entry_time) is the primary key (combination of columns with unique values) for this table.
# Each row of this table contains the ID of the parking lot, the ID of the car, the entry and exit times, and the fee paid for the parking duration.
# Write a solution to find the total parking fee paid by each car across all parking lots, and the average hourly fee
# (rounded to 2 decimal places) paid by each car. Also, find the parking lot where each car spent the most total time.
#
# Return the result table ordered by car_id in ascending order.
#
# Note: Test cases are generated in such a way that an individual car cannot be in multiple parking lots at the same time.
import pandas as pd

def grouping(df: pd.DataFrame) -> pd.Series:
    total_fee_paid = df["fee_paid"].sum()
    df["hour"] = (df["exit_time"] - df["entry_time"]).dt.total_seconds() / (60*60)
    avg_hourly_fee = (total_fee_paid / (df["hour"].sum())).round(2)
    gr = df.groupby(by="lot_id", as_index=False).agg(hour=("hour", "sum"))
    most_time_lot = gr.loc[gr["hour"] == gr["hour"].max(), "lot_id"].iloc[0]
    return pd.Series(data=[total_fee_paid, avg_hourly_fee, most_time_lot],
                     index=["total_fee_paid", "avg_hourly_fee", "most_time_lot"])


def calculate_fees_and_duration(parking_transactions: pd.DataFrame) -> pd.DataFrame:
    if parking_transactions.empty:
        return pd.DataFrame({
            "car_id": list(),
            "total_fee_paid": list(),
            "avg_hourly_fee": list(),
            "most_time_lot": list()
        })
    grouped = parking_transactions.groupby(by="car_id", as_index=True).apply(grouping, include_groups=False).reset_index()
    return grouped.sort_values(by="car_id", ascending=True)

