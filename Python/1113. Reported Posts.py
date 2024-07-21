# Table: Actions
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | user_id       | int     |
# | post_id       | int     |
# | action_date   | date    |
# | action        | enum    |
# | extra         | varchar |
# +---------------+---------+
# This table may have duplicate rows.
# The action column is an ENUM (category) type of ('view', 'like', 'reaction', 'comment', 'report', 'share').
# The extra column has optional information about the action, such as a reason for the report or a type of reaction.
# extra is never NULL.
import pandas as pd
from pathlib import Path
import os
from datetime import datetime

def reported_posts(actions: pd.DataFrame) -> pd.DataFrame:
    today = datetime(2019,7,5)
    actions = actions[
        (actions["action_date"] == (today - pd.DateOffset(days=1))) &
        (actions["action"] == "report")
    ].drop_duplicates(subset=["post_id", "extra"])
    return actions.groupby(by="extra", as_index=False).agg(report_count=("extra", "count")).rename(columns={"extra":"report_reason"})




