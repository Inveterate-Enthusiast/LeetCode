Table: Triangles

+-------------+------+
| Column Name | Type |
+-------------+------+
| A           | int  |
| B           | int  |
| C           | int  |
+-------------+------+
(A, B, C) is the primary key for this table.
Each row include the lengths of each of a triangle's three sides.
Write a query to find the type of triangle. Output one of the following for each row:

--Equilateral: It's a triangle with 3 sides of equal length.
--Isosceles: It's a triangle with 2 sides of equal length.
--Scalene: It's a triangle with 3 sides of differing lengths.
Not A Triangle: The given values of A, B, and C don't form a triangle.
Return the result table in any order.


1.
SELECT (
CASE
    WHEN A >= (B + C) OR B >= (A + C) OR C >= (A + B) THEN 'Not A Triangle'
    WHEN A = B AND B = C THEN 'Equilateral'
    WHEN A = B OR B = C OR A = C THEN 'Isosceles'
    ELSE 'Scalene'
END
) AS triangle_type
FROM Triangles