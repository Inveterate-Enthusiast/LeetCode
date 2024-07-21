Table: Tree

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| p_id        | int  |
+-------------+------+
id is the column with unique values for this table.
Each row of this table contains information about the id of a node and the id of its parent node in a tree.
The given structure is always a valid tree.


Each node in the tree can be one of three types:

"Leaf": if the node is a leaf node.
"Root": if the node is the root of the tree.
"Inner": If the node is neither a leaf node nor a root node.
Write a solution to report the type of each node in the tree.

Return the result table in any order.

1.
WITH added AS
    (SELECT id, p_id, (CASE WHEN id IN (SELECT p_id FROM Tree) THEN TRUE ELSE FALSE END) AS c_id
    FROM Tree)
SELECT id, (CASE
                WHEN p_id IS NULL THEN 'Root'
                WHEN c_id IS TRUE THEN 'Inner'
                ELSE 'Leaf'
                END) AS type
FROM added;