Table: Cinema

+----------------+----------+
| Column Name    | Type     |
+----------------+----------+
| id             | int      |
| movie          | varchar  |
| description    | varchar  |
| rating         | float    |
+----------------+----------+
id is the primary key (column with unique values) for this table.
Each row contains information about the name of a movie, its genre, and its rating.
rating is a 2 decimal places float in the range [0, 10]

Write a solution to report the movies with an odd-numbered ID and a description that is not "boring".

Return the result table ordered by rating in descending order.

1.
WITH not_boring AS
(SELECT * FROM Cinema WHERE description != 'boring')
SELECT * FROM not_boring WHERE (id % 2) != 0 ORDER BY rating DESC;
2.
SELECT * FROM Cinema WHERE description != 'boring' AND (id % 2) != 0 ORDER BY rating DESC;