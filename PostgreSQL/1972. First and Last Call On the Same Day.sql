Table: Calls

+--------------+----------+
| Column Name  | Type     |
+--------------+----------+
| caller_id    | int      |
| recipient_id | int      |
| call_time    | datetime |
+--------------+----------+
(caller_id, recipient_id, call_time) is the primary key (combination of columns with unique values) for this table.
Each row contains information about the time of a phone call between caller_id and recipient_id.


Write a solution to report the IDs of the users whose first and last calls on any day were with the same person.
Calls are counted regardless of being the caller or the recipient.

Return the result table in any order.


1.
WITH unioned AS (
    SELECT
        caller_id,
        recipient_id,
        call_time::DATE AS date,
        call_time
    FROM Calls

    UNION ALL

    SELECT
        recipient_id AS caller_id,
        caller_id AS recipient_id,
        call_time::DATE AS date,
        call_time
    FROM Calls
),
with_windows AS (
    SELECT
        caller_id,
        recipient_id,
        date,
        DENSE_RANK() OVER(PARTITION BY caller_id, date ORDER BY call_time ASC) AS first_call,
        DENSE_RANK() OVER(PARTITION BY caller_id, date ORDER BY call_time DESC) AS last_call
    FROM unioned
)
SELECT DISTINCT
    main.caller_id AS user_id
FROM with_windows AS main

INNER JOIN with_windows AS sub
    ON sub.caller_id = main.caller_id
    AND sub.recipient_id = main.recipient_id
    AND sub.first_call = 1
    AND main.last_call = 1;