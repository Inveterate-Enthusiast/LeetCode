Table: Boxes

+--------------+------+
| Column Name  | Type |
+--------------+------+
| box_id       | int  |
| chest_id     | int  |
| apple_count  | int  |
| orange_count | int  |
+--------------+------+
box_id is the column with unique values for this table.
chest_id is a foreign key (reference column) of the chests table.
This table contains information about the boxes and the number of oranges and apples they have.
Each box may include a chest, which also can contain oranges and apples.


Table: Chests

+--------------+------+
| Column Name  | Type |
+--------------+------+
| chest_id     | int  |
| apple_count  | int  |
| orange_count | int  |
+--------------+------+
chest_id is the column with unique values for this table.
This table contains information about the chests and the corresponding number of oranges and apples they have.


Write a solution to count the number of apples and oranges in all the boxes.
If a box contains a chest, you should also include the number of apples and oranges it has.


1.
SELECT
(COALESCE(SUM(main.apple_count), 0) + (COALESCE(SUM(sub.apple_count), 0))) AS apple_count,
(COALESCE(SUM(main.orange_count), 0) + COALESCE(SUM(sub.orange_count), 0)) AS orange_count
FROM Boxes AS main
LEFT JOIN
Chests AS sub
ON main.chest_id = sub.chest_id;