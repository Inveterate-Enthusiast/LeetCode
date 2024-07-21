# Write a solution to pivot the data so that each row represents temperatures for a specific month, and each city is a separate column.
#
# The result format is in the following example.

import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    newDataFrame = weather.pivot(index= "month", columns= "city", values= "temperature")
    return newDataFrame

data = {
    "city": ["Jacksonville", "Jacksonville", "Jacksonville", "Jacksonville", "ElPaso", "ElPaso"],
    "month": ["January", "February", "March", "April", "May", "January"],
    "temperature": [13, 23, 38, 5, 34, 20]
}
data = pd.DataFrame(data)
print(pivotTable(data))