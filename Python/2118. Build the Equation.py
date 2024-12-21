# You have a very powerful program that can solve any equation of one variable in the world.
# The equation passed to the program must be formatted as follows:
#
# The left-hand side (LHS) should contain all the terms.
# The right-hand side (RHS) should be zero.
# Each term of the LHS should follow the format "<sign><fact>X^<pow>" where:
# <sign> is either "+" or "-".
# <fact> is the absolute value of the factor.
# <pow> is the value of the power.
# If the power is 1, do not add "^<pow>".
# For example, if power = 1 and factor = 3, the term will be "+3X".
# If the power is 0, add neither "X" nor "^<pow>".
# For example, if power = 0 and factor = -3, the term will be "-3".
# The powers in the LHS should be sorted in descending order.
# Write a solution to build the equation.


import pandas as pd
import numpy as np
from pathlib import Path
import os

def build_the_equation(terms: pd.DataFrame) -> pd.DataFrame:
    if terms.empty:
        return pd.DataFrame({"equation": [pd.NA]})
    terms.sort_values(by="power", ascending=False, inplace=True)
    result = []
    for index, row in terms.iterrows():
        sign, abs = "-" if row["factor"] < 0 else "+", np.abs(row["factor"])
        if row["power"] == 1:
            result.append(f"{sign}{abs}X")
        elif row["power"] == 0:
            result.append(f"{sign}{abs}")
        else:
            result.append(f"{sign}{abs}X^{row['power']}")
    else:
        if result:
            result.append("=0")
    return pd.DataFrame({
        "equation": ["".join(map(str, result))]
    })

terms = pd.read_excel(Path(os.getcwd()) / "data" / "2118. Build the Equation.xlsx")
print(build_the_equation(terms))