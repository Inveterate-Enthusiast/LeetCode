Table: Coordinates

+-------------+------+
| Column Name | Type |
+-------------+------+
| X           | int  |
| Y           | int  |
+-------------+------+
Each row includes X and Y, where both are integers. Table may contain duplicate values.
Two coordindates (X1, Y1) and (X2, Y2) are said to be symmetric coordintes if X1 == Y2 and X2 == Y1.

Write a solution that outputs, among all these symmetric coordintes, only those unique coordinates that satisfy the condition X1 <= Y1.

Return the result table ordered by X and Y (respectively) in ascending order.



1.
WITH with_row AS (
    SELECT
        *,
        ROW_NUMBER() OVER() AS our_row
    FROM Coordinates
)
SELECT DISTINCT
    our_1.X,
    our_1.Y
FROM with_row AS our_1

INNER JOIN with_row AS our_2
ON our_2.X = our_1.Y
AND our_2.Y = our_1.X
AND our_2.our_row <> our_1.our_row

WHERE our_1.X <= our_1.Y;