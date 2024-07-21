# Table: Tree
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | id          | int  |
# | p_id        | int  |
# +-------------+------+
# id is the column with unique values for this table.
# Each row of this table contains information about the id of a node and the id of its parent node in a tree.
# The given structure is always a valid tree.
#
#
# Each node in the tree can be one of three types:
#
# "Leaf": if the node is a leaf node.
# "Root": if the node is the root of the tree.
# "Inner": If the node is neither a leaf node nor a root node.
# Write a solution to report the type of each node in the tree.
#
# Return the result table in any order.
import pandas as pd
import os
from pathlib import Path
import numpy as np

def applying(df: pd.Series) -> str:
    if df["p_id"] is pd.NA:
        return "Root"
    elif df["c_id"]:
        return "Inner"
    else:
        return "Leaf"

def tree_node(tree: pd.DataFrame) -> pd.DataFrame:
    if tree.empty:
        tree["type"] = pd.NA
    else:
        tree["c_id"] = tree["id"].isin(tree["p_id"])
        tree["type"] = tree.apply(applying, axis=1)
    return tree.loc[:, ["id", "type"]]

def tree_node1(tree: pd.DataFrame) -> pd.DataFrame:
    Conditions = [
        tree["p_id"].isna(),
        tree["id"].isin(tree["p_id"])
    ]
    Choices = [
        "Root",
        "Inner"
    ]
    tree["type"] = np.select(Conditions, Choices, default="Leaf")
    return tree.loc[:, ["id", "type"]]


path = Path(os.getcwd()) / "data" / "608. Tree Node.xlsx"
tree = pd.read_excel(path)
print(tree_node1(tree))