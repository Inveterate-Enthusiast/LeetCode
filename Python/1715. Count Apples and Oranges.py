# Table: Boxes
#
# +--------------+------+
# | Column Name  | Type |
# +--------------+------+
# | box_id       | int  |
# | chest_id     | int  |
# | apple_count  | int  |
# | orange_count | int  |
# +--------------+------+
# box_id is the column with unique values for this table.
# chest_id is a foreign key (reference column) of the chests table.
# This table contains information about the boxes and the number of oranges and apples they have.
# Each box may include a chest, which also can contain oranges and apples.
#
#
# Table: Chests
#
# +--------------+------+
# | Column Name  | Type |
# +--------------+------+
# | chest_id     | int  |
# | apple_count  | int  |
# | orange_count | int  |
# +--------------+------+
# chest_id is the column with unique values for this table.
# This table contains information about the chests and the corresponding number of oranges and apples they have.
#
#
# Write a solution to count the number of apples and oranges in all the boxes.
# If a box contains a chest, you should also include the number of apples and oranges it has.
import pandas as pd

def count_apples_and_oranges(boxes: pd.DataFrame, chests: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(
        left=boxes,
        right=chests,
        how="left",
        on="chest_id",
        suffixes=("_box", "_chest")
    )
    apples = (merged["apple_count_box"].sum() + merged["apple_count_chest"].sum())
    oranges = (merged["orange_count_box"].sum() + merged["orange_count_chest"].sum())
    return pd.DataFrame({
        "apple_count": [apples],
        "orange_count": [oranges]
    })

