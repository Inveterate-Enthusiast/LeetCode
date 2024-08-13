Table: Elements

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| symbol      | varchar |
| type        | enum    |
| electrons   | int     |
+-------------+---------+
symbol is the primary key (column with unique values) for this table.
Each row of this table contains information of one element.
type is an ENUM (category) of type ('Metal', 'Nonmetal', 'Noble')
 - If type is Noble, electrons is 0.
 - If type is Metal, electrons is the number of electrons that one atom of this element can give.
 - If type is Nonmetal, electrons is the number of electrons that one atom of this element needs.


Two elements can form a bond if one of them is 'Metal' and the other is 'Nonmetal'.

Write a solution to find all the pairs of elements that can form a bond.

Return the result table in any order.



1.
SELECT main.symbol AS metal, sub.symbol AS nonmetal
FROM (SELECT * FROM Elements WHERE type = 'Metal') AS main
CROSS JOIN
(SELECT * FROM Elements WHERE type = 'Nonmetal') AS sub;