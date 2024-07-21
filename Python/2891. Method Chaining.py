# Write a solution to list the names of animals that weigh strictly more than 100 kilograms.
#
# Return the animals sorted by weight in descending order.
#
# The result format is in the following example.

import pandas as pd

def findHeavyAnimals1(animals: pd.DataFrame) -> pd.DataFrame:
    OurAnimals = {"name":[], "weight": []}
    for index, row in animals.iterrows():
        if row["weight"] >= 100:
            OurAnimals["name"].append(row["name"])
            OurAnimals["weight"].append(row["weight"])
    for i in range(len(OurAnimals["weight"])):
        for j in range(len(OurAnimals["weight"])-i-1):
            if OurAnimals["weight"][j+1] > OurAnimals["weight"][j]:
                OurAnimals["weight"][j], OurAnimals["weight"][j+1] = OurAnimals["weight"][j+1], OurAnimals["weight"][j]
                OurAnimals["name"][j], OurAnimals["name"][j+1] = OurAnimals["name"][j+1], OurAnimals["name"][j]
    OurAnimals = pd.DataFrame(OurAnimals)
    return OurAnimals[["name"]]


def findHeavyAnimals2(animals: pd.DataFrame) -> pd.DataFrame:
    return animals[animals["weight"] > 100].sort_values("weight", ascending= False)[["name"]]


data = {
    "name": ["Tatiana", "Khaleg", "Alex", "Jonathan", "Stefan", "Tommy"],
    "species": ["Snake", "Giraffe", "Leopard", "Monkey", "Bear", "Panda"],
    "age": [98, 50, 6, 45, 100, 26],
    "weight": [464, 41, 328, 463, 50, 349]
}
data = pd.DataFrame(data)
print(findHeavyAnimals2(data))