--Table: SecretSanta
--
--+-------------+------+
--| Column Name | Type |
--+-------------+------+
--| giver_id    | int  |
--| receiver_id | int  |
--| gift_value  | int  |
--+-------------+------+
--(giver_id, receiver_id) is the unique key for this table.
--Each row represents a record of a gift exchange between two employees, giver_id represents the employee who gives a gift,
--receiver_id represents the employee who receives the gift and gift_value represents the value of the gift given.
--Write a solution to find the total gift value and length of circular chains of Secret Santa gift exchanges:
--
--A circular chain is defined as a series of exchanges where:
--
--Each employee gives a gift to exactly one other employee.
--Each employee receives a gift from exactly one other employee.
--The exchanges form a continuous loop (e.g., employee A gives a gift to B, B gives to C, and C gives back to A).
--Return the result ordered by the chain length and total gift value of the chain in descending order.
--
--
--1.
WITH RECURSIVE all_loops AS (
    SELECT
        giver_id,
        receiver_id,
        gift_value,
        1 AS len,
        receiver_id AS loop_id
    FROM SecretSanta

    UNION ALL

    SELECT
        main.giver_id,
        main.receiver_id,
        (sub.gift_value + main.gift_value) AS gift_value,
        (sub.len + 1) AS len,
        sub.loop_id
    FROM SecretSanta AS main

    INNER JOIN all_loops AS sub
        ON sub.giver_id = main.receiver_id
        AND NOT sub.loop_id = main.receiver_id
),
ranked AS (
    SELECT
        *,
        DENSE_RANK() OVER(PARTITION BY loop_id ORDER BY len DESC) AS our_rank
    FROM all_loops
)
SELECT DISTINCT
    DENSE_RANK() OVER(ORDER BY len DESC, gift_value DESC) AS chain_id,
    len AS chain_length,
    gift_value AS total_gift_value
FROM ranked

WHERE our_rank = 1

ORDER BY chain_length DESC, total_gift_value DESC;