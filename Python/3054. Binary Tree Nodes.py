# Table: Tree
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | N           | int  |
# | P           | int  |
# +-------------+------+
# N is the column of unique values for this table.
# Each row includes N and P, where N represents the value of a node in Binary Tree, and P is the parent of N.
# Write a solution to find the node type of the Binary Tree. Output one of the following for each node:
#
# Root: if the node is the root node.
# Leaf: if the node is the leaf node.
# Inner: if the node is neither root nor leaf node.
# Return the result table ordered by node value in ascending order.
import numpy as np
import pandas as pd

def binary_tree_nodes(tree: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(
        left=tree,
        right=tree.rename(columns={"N": "C", "P": "N"}),
        how="left",
        on="N"
    )
    merged["Type"] = np.where(
        merged["P"].isna(), "Root",
        np.where(
            merged["C"].isna(), "Leaf",
            "Inner"
        )
    )
    return merged[["N", "Type"]].drop_duplicates(keep="first").sort_values(by="N", ascending=True)
