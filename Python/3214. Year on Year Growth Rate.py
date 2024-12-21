# Table: user_transactions
#
# +------------------+----------+
# | Column Name      | Type     |
# +------------------+----------+
# | transaction_id   | integer  |
# | product_id       | integer  |
# | spend            | decimal  |
# | transaction_date | datetime |
# +------------------+----------+
# The transaction_id column uniquely identifies each row in this table.
# Each row of this table contains the transaction ID, product ID, the spend amount, and the transaction date.
# Write a solution to calculate the year-on-year growth rate for the total spend for each product.
#
# The result table should include the following columns:
#
# year: The year of the transaction.
# product_id: The ID of the product.
# curr_year_spend: The total spend for the current year.
# prev_year_spend: The total spend for the previous year.
# yoy_rate: The year-on-year growth rate percentage, rounded to 2 decimal places.
# Return the result table ordered by product_id,year in ascending order.


import pandas as pd
import numpy as np

def calculate_yoy_growth(user_transactions: pd.DataFrame) -> pd.DataFrame:
    user_transactions["year"] = user_transactions["transaction_date"].dt.year
    grouped = user_transactions.groupby(by=["product_id", "year"], as_index=False).agg(curr_year_spend=("spend", "sum"))
    grouped["prev_year"] = grouped["year"] - 1
    merged = pd.merge(
        left=grouped,
        right=grouped[["product_id", "year", "curr_year_spend"]].rename(columns={"year": "prev_year", "curr_year_spend": "prev_year_spend"}),
        how="left",
        on=["prev_year", "product_id"]
    )
    merged["yoy_rate"] = np.where(
        merged["prev_year_spend"].isna(),
        pd.NA,
        ((((merged["curr_year_spend"]) - merged["prev_year_spend"]) / merged["prev_year_spend"].abs()) * 100 + 1e-9).round(2)
    )
    return merged[["year", "product_id", "curr_year_spend", "prev_year_spend", "yoy_rate"]].sort_values(by=["product_id", "year"], ascending=[True, True])
