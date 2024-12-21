--Table: Sessions
--
--+---------------+----------+
--| Column Name   | Type     |
--+---------------+----------+
--| user_id       | int      |
--| session_start | datetime |
--| session_end   | datetime |
--| session_id    | int      |
--| session_type  | enum     |
--+---------------+----------+
--session_id is column of unique values for this table.
--session_type is an ENUM (category) type of (Viewer, Streamer).
--This table contains user id, session start, session end, session id and session type.
--Write a solution to find the the users who have had at least one consecutive session of the same type
--(either 'Viewer' or 'Streamer') with a maximum gap of 12 hours between sessions.
--
--Return the result table ordered by user_id in ascending order.
--
--
--1.
WITH with_prev AS (
    SELECT
        *,
        LAG(session_end, 1) OVER(PARTITION BY user_id, session_type ORDER BY session_start ASC, session_end ASC) AS prev_end
    FROM Sessions
)
SELECT DISTINCT
    user_id
FROM with_prev

WHERE (NOT prev_end IS NULL) AND ((EXTRACT(EPOCH FROM AGE(session_start, prev_end)) / (60*60)) <= 12)

GROUP BY user_id
HAVING COUNT(*) >= 1

ORDER BY user_id ASC;