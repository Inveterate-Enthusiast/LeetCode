Table: Seat

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| student     | varchar |
+-------------+---------+
id is the primary key (unique value) column for this table.
Each row of this table indicates the name and the ID of a student.
id is a continuous increment.


Write a solution to swap the seat id of every two consecutive students. If the number of students is odd, the id of the last student is not swapped.

Return the result table ordered by id in ascending order.

1.
WITH ranked AS
    (SELECT *, ROW_NUMBER() OVER() AS row
    FROM Seat)
SELECT id,
(CASE
    WHEN ((SELECT MAX(row) FROM ranked) % 2) != 0 AND row = (SELECT MAX(row) FROM ranked) THEN student
    WHEN (main.row % 2) != 0 THEN (SELECT sub.student FROM ranked AS sub WHERE sub.row = main.row+1)
    ELSE (SELECT sub.student FROM ranked AS sub WHERE sub.row = main.row-1)
END) AS student
FROM ranked AS main
ORDER BY id ASC;