Table: Servers

+----------------+----------+
| Column Name    | Type     |
+----------------+----------+
| server_id      | int      |
| status_time    | datetime |
| session_status | enum     |
+----------------+----------+
(server_id, status_time, session_status) is the primary key (combination of columns with unique values) for this table.
session_status is an ENUM (category) type of ('start', 'stop').
Each row of this table contains server_id, status_time, and session_status.
Write a solution to find the total time when servers were running. The output should be rounded down to the nearest number of full days.

Return the result table in any order.


1.
WITH prev AS (
    SELECT
        *,
        LAG(status_time, 1) OVER() AS prev_time
    FROM Servers
),
dif AS (
    SELECT
        *,
        (CASE WHEN session_status = 'stop' THEN EXTRACT(EPOCH FROM AGE(status_time, prev_time)) END) AS dif
    FROM prev
)
SELECT
    FLOOR(SUM(dif) / 60 / 60 / 24) AS total_uptime_days
FROM dif;