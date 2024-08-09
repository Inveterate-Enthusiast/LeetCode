Table: Logs

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| log_id        | int     |
+---------------+---------+
log_id is the column of unique values for this table.
Each row of this table contains the ID in a log Table.


Write a solution to find the start and end number of continuous ranges in the table Logs.

Return the result table ordered by start_id.



1.
WITH ranked AS
    (SELECT log_id,
    ROW_NUMBER() OVER(ORDER BY log_id ASC) AS our_rank
    FROM Logs
    ORDER BY log_id ASC),
new_rank AS
    (SELECT *, (our_rank - log_id) AS dif
    FROM ranked)
SELECT MIN(log_id) AS start_id, MAX(log_id) AS end_id
FROM new_rank
GROUP BY dif
ORDER BY start_id ASC;