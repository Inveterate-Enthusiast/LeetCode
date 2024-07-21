# Table: DailySales
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | date_id     | date    |
# | make_name   | varchar |
# | lead_id     | int     |
# | partner_id  | int     |
# +-------------+---------+
# There is no primary key (column with unique values) for this table. It may contain duplicates.
# This table contains the date and the name of the product sold and the IDs of the lead and partner it was sold to.
# The name consists of only lowercase English letters.
#
#
# For each date_id and make_name, find the number of distinct lead_id's and distinct partner_id's.
#
# Return the result table in any order.

import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    return (daily_sales.groupby(
        by=["date_id", "make_name"],
        as_index=False)
            .agg(
        unique_leads=("lead_id", "nunique"),
        unique_partners=("partner_id", "nunique")))