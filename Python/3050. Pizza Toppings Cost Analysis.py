# Table: Toppings
#
# +--------------+---------+
# | Column Name  | Type    |
# +--------------+---------+
# | topping_name | varchar |
# | cost         | decimal |
# +--------------+---------+
# topping_name is the primary key for this table.
# Each row of this table contains topping name and the cost of the topping.
# Write a solution to calculate the total cost of all possible 3-topping pizza combinations from a given list of toppings.
# The total cost of toppings must be rounded to 2 decimal places.
#
# Note:
#
# Do not include the pizzas where a topping is repeated. For example, ‘Pepperoni, Pepperoni, Onion Pizza’.
# Toppings must be listed in alphabetical order. For example, 'Chicken, Onions, Sausage'. 'Onion, Sausage, Chicken' is not acceptable.
# Return the result table ordered by total cost in descending order and combination of toppings in ascending order.
import pandas as pd
from pathlib import Path
import os
import itertools
import functools

def cost_analysis(toppings: pd.DataFrame) -> pd.DataFrame:
    toppings.sort_values(by="topping_name", ascending=True, inplace=True)
    our_dict = dict()
    for index, row in toppings.iterrows():
        our_dict[row["topping_name"]] = row["cost"]

    comb = list(itertools.combinations(toppings["topping_name"], 3))
    result = pd.DataFrame({
        "pizza": list(map(lambda x: ",".join(x), comb)),
        "total_cost": list(round(functools.reduce(lambda acc, x: acc + our_dict[x], i, 0), 2) for i in comb)
    })

    return result.sort_values(by=["total_cost", "pizza"], ascending=[False, True])

toppings = pd.read_excel(Path(os.getcwd()) / "data" / "3050. Pizza Toppings Cost Analysis.xlsx")
print(cost_analysis(toppings))