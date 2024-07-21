# Table: Insurance
#
# +-------------+-------+
# | Column Name | Type  |
# +-------------+-------+
# | pid         | int   |
# | tiv_2015    | float |
# | tiv_2016    | float |
# | lat         | float |
# | lon         | float |
# +-------------+-------+
# pid is the primary key (column with unique values) for this table.
# Each row of this table contains information about one policy where:
# pid is the policyholder's policy ID.
# tiv_2015 is the total investment value in 2015 and tiv_2016 is the total investment value in 2016.
# lat is the latitude of the policy holder's city. It's guaranteed that lat is not NULL.
# lon is the longitude of the policy holder's city. It's guaranteed that lon is not NULL.
#
#
# Write a solution to report the sum of all total investment values in 2016 tiv_2016, for all policyholders who:
#
# have the same tiv_2015 value as one or more other policyholders, and
# are not located in the same city as any other policyholder (i.e., the (lat, lon) attribute pairs must be unique).
# Round tiv_2016 to two decimal places.
import pandas as pd
from pathlib import Path
import os

def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:
    return insurance.loc[
        (~insurance.duplicated(subset=["lat", "lon"], keep=False))
        &
        (insurance.duplicated(subset="tiv_2015", keep=False))
    ][["tiv_2016"]].sum().to_frame().round(2).T

path = Path(os.getcwd()) / "data" / "585. Investments in 2016.xlsx"
insurance = pd.read_excel(path)
print(find_investments(insurance))