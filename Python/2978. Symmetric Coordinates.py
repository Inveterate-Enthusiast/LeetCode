# Two coordindates (X1, Y1) and (X2, Y2) are said to be symmetric coordintes if X1 == Y2 and X2 == Y1.
#
# Write a solution that outputs, among all these symmetric coordintes, only those unique coordinates that satisfy the condition X1 <= Y1.
#
# Return the result table ordered by X and Y (respectively) in ascending order.

import pandas as pd

def symmetric_pairs(coordinates: pd.DataFrame) -> pd.DataFrame:
    coordinates = coordinates.reset_index().rename(columns={"index": "row"})
    merged = pd.merge(
        left=coordinates.rename(columns={"X": "X1", "Y": "Y1", "row": "row1"}),
        right=coordinates.rename(columns={"X": "X2","Y": "Y2", "row": "row2"}),
        how="cross"
    )
    filtered = merged.loc[
        (merged["X1"] == merged["Y2"])
        &
        (merged["Y1"] == merged["X2"])
        &
        (merged["X1"] <= merged["Y1"])
        & ~(merged["row1"] == merged["row2"])
    ]
    return (filtered[["X1", "Y1"]]
            .drop_duplicates(keep="first")
            .rename(columns={"X1": "x", "Y1": "y"})
            .sort_values(by=["x", "y"], ascending=[True, True]))
