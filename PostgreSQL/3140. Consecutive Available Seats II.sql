Table: Cinema

+-------------+------+
| Column Name | Type |
+-------------+------+
| seat_id     | int  |
| free        | bool |
+-------------+------+
seat_id is an auto-increment column for this table.
Each row of this table indicates whether the ith seat is free or not. 1 means free while 0 means occupied.
Write a solution to find the length of longest consecutive sequence of available seats in the cinema.

Note:

There will always be at most one longest consecutive sequence.
If there are multiple consecutive sequences with the same length, include all of them in the output.
Return the result table ordered by first_seat_id in ascending order.



1.
WITH filtered AS (
    SELECT
        *,
        seat_id - ROW_NUMBER() OVER(ORDER BY seat_id ASC) AS our_group
    FROM Cinema
    WHERE free = 1
    ORDER BY seat_id ASC
),
sub AS (
    SELECT
        *,
        COUNT(*) OVER(PARTITION BY our_group) AS len
    FROM filtered
)
SELECT
    MIN(seat_id) AS first_seat_id,
    MAX(seat_id) AS last_seat_id,
    MAX(len) AS consecutive_seats_len
FROM sub
WHERE len = (SELECT MAX(len) FROM sub)
GROUP BY our_group;