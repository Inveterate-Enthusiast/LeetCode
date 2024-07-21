# Write a solution to fill in the missing value as 0 in the quantity column.
#
# The result format is in the following example.

import pandas as pd
import math

def fillMissingValues1(products: pd.DataFrame) -> pd.DataFrame:
    products["quantity"] = products["quantity"].fillna(0)
    return products

data = {
    "name": ["Wristwatch", "WirelessEarbuds", "GolfClubs", "Printer"],
    "quantity": [None, None, 779, 849],
    "price": [135, 821, 9319, 3051]
}
data = pd.DataFrame(data)
print(fillMissingValues1(data))