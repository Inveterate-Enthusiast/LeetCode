Table: Tree

+-------------+------+
| Column Name | Type |
+-------------+------+
| N           | int  |
| P           | int  |
+-------------+------+
N is the column of unique values for this table.
Each row includes N and P, where N represents the value of a node in Binary Tree, and P is the parent of N.
Write a solution to find the node type of the Binary Tree. Output one of the following for each node:

Root: if the node is the root node.
Leaf: if the node is the leaf node.
Inner: if the node is neither root nor leaf node.
Return the result table ordered by node value in ascending order.

1.
WITH with_children AS (
    SELECT
        main.N,
        main.P,
        sub.N AS C
    FROM Tree AS main
    LEFT JOIN Tree AS sub
        ON main.N = sub.P
)
SELECT DISTINCT
    N,
    (CASE
        WHEN P IS NULL THEN 'Root'
        WHEN C IS NULL THEN 'Leaf'
        ELSE 'Inner'
    END) AS Type
FROM with_children
ORDER BY N ASC;