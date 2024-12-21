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
--Write a solution to find the number of streaming sessions for users whose first session was as a viewer.
--
--Return the result table ordered by count of streaming sessions, user_id in descending order.
--
--
--
--1.
WITH ranked AS (
    SELECT
        *,
        DENSE_RANK() OVER(PARTITION BY user_id ORDER BY session_start ASC, session_end ASC) AS our_rank
    FROM Sessions
)
SELECT
    main.user_id,
    SUM(CASE WHEN main.session_type = 'Streamer' THEN 1 ELSE 0 END) AS sessions_count
FROM ranked AS main

LEFT JOIN (
    SELECT * FROM ranked WHERE our_rank = 1
) AS sub
    ON sub.user_id = main.user_id

WHERE sub.session_type = 'Viewer'
GROUP BY main.user_id
HAVING SUM(CASE WHEN main.session_type = 'Streamer' THEN 1 ELSE 0 END) > 0
ORDER BY sessions_count DESC, main.user_id DESC;