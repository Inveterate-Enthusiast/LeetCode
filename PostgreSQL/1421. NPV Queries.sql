Table: NPV

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| year          | int     |
| npv           | int     |
+---------------+---------+
(id, year) is the primary key (combination of columns with unique values) of this table.
The table has information about the id and the year of each inventory and the corresponding net present value.
 

Table: Queries

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| year          | int     |
+---------------+---------+
(id, year) is the primary key (combination of columns with unique values) of this table.
The table has information about the id and the year of each inventory query.



1.
SELECT main.id, main.year, COALESCE(sub.npv, 0) AS npv FROM Queries AS main LEFT JOIN NPV AS sub ON main.id = sub.id AND main.year = sub.year;