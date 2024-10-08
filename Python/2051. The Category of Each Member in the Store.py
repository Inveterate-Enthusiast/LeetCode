# Table: Members
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | member_id   | int     |
# | name        | varchar |
# +-------------+---------+
# member_id is the column with unique values for this table.
# Each row of this table indicates the name and the ID of a member.
#
#
# Table: Visits
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | visit_id    | int  |
# | member_id   | int  |
# | visit_date  | date |
# +-------------+------+
# visit_id is the column with unique values for this table.
# member_id is a foreign key (reference column) to member_id from the Members table.
# Each row of this table contains information about the date of a visit to the store and the member who visited it.
#
#
# Table: Purchases
#
# +----------------+------+
# | Column Name    | Type |
# +----------------+------+
# | visit_id       | int  |
# | charged_amount | int  |
# +----------------+------+
# visit_id is the column with unique values for this table.
# visit_id is a foreign key (reference column) to visit_id from the Visits table.
# Each row of this table contains information about the amount charged in a visit to the store.
#
#
# A store wants to categorize its members. There are three tiers:
#
# "Diamond": if the conversion rate is greater than or equal to 80.
# "Gold": if the conversion rate is greater than or equal to 50 and less than 80.
# "Silver": if the conversion rate is less than 50.
# "Bronze": if the member never visited the store.
# The conversion rate of a member is (100 * total number of purchases for the member) / total number of visits for the member.
#
# Write a solution to report the id, the name, and the category of each member.
#
# Return the result table in any order.
import pandas as pd
import numpy as np

def find_categories(members: pd.DataFrame, visits: pd.DataFrame, purchases: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(
        left=visits,
        right=purchases,
        how="left",
        on="visit_id"
    )
    merged["bool"] = ~merged["charged_amount"].isna()
    grouped = merged.groupby(by="member_id", as_index=False).agg(
        vis_count=("visit_id", "count"),
        pur_count=("bool", "sum")
    )
    grouped["rate"] = (100 * grouped["pur_count"]) / grouped["vis_count"]
    grouped["category"] = np.where(grouped["rate"] >= 80, "Diamond",
                                   np.where(grouped["rate"] < 50, "Silver", "Gold"))
    result = pd.merge(
        left=members,
        right=grouped[["member_id", "category"]],
        how="left",
        on="member_id"
    ).fillna("Bronze")
    return result[["member_id", "name", "category"]]

