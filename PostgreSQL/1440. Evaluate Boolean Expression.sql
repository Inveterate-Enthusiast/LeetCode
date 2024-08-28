Table Variables:

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| name          | varchar |
| value         | int     |
+---------------+---------+
In SQL, name is the primary key for this table.
This table contains the stored variables and their values.


Table Expressions:

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| left_operand  | varchar |
| operator      | enum    |
| right_operand | varchar |
+---------------+---------+
In SQL, (left_operand, operator, right_operand) is the primary key for this table.
This table contains a boolean expression that should be evaluated.
operator is an enum that takes one of the values ('<', '>', '=')
The values of left_operand and right_operand are guaranteed to be in the Variables table.


Evaluate the boolean expressions in Expressions table.

Return the result table in any order.



1.
SELECT main.*,
(CASE
    WHEN main.operator = '>' THEN (sub1.value > sub2.value)::TEXT
    WHEN main.operator = '<' THEN (sub1.value < sub2.value)::TEXT
    ELSE (sub1.value = sub2.value)::TEXT
END) AS value
FROM Expressions AS main
LEFT JOIN
Variables AS sub1
ON main.left_operand = sub1.name
LEFT JOIN
Variables AS sub2
ON main.right_operand = sub2.name;