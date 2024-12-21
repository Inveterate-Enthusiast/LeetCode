--Table: Teams
--
--+-------------+---------+
--| Column Name | Type    |
--+-------------+---------+
--| player_id   | int     |
--| team_name   | varchar |
--+-------------+---------+
--player_id is the unique key for this table.
--Each row contains the unique identifier for player and the name of one of the teams participating in that match.
--
--Table: Passes
--
--+-------------+---------+
--| Column Name | Type    |
--+-------------+---------+
--| pass_from   | int     |
--| time_stamp  | varchar |
--| pass_to     | int     |
--+-------------+---------+
--(pass_from, time_stamp) is the primary key for this table.
--pass_from is a foreign key to player_id from Teams table.
--Each row represents a pass made during a match, time_stamp represents the time in minutes (00:00-90:00) when the pass was made,
--pass_to is the player_id of the player receiving the pass.
--
--Write a solution to calculate the dominance score for each team in both halves of the match. The rules are as follows:
--
--A match is divided into two halves: first half (00:00-45:00 minutes) and second half (45:01-90:00 minutes)
--The dominance score is calculated based on successful and intercepted passes:
--When pass_to is a player from the same team: +1 point
--When pass_to is a player from the opposing team (interception): -1 point
--A higher dominance score indicates better passing performance
--Return the result table ordered by team_name and half_number in ascending order.
--
--
--
--
--
--1.
WITH sub AS (
    SELECT
        sub_from.team_name,
        (CASE WHEN time_stamp <= '45:00' THEN 1 ELSE 2 END) AS half_number,
        (CASE WHEN sub_from.team_name = sub_to.team_name THEN 1 ELSE (-1) END) AS our_bool
    FROM Passes AS main

    LEFT JOIN Teams AS sub_from
        ON sub_from.player_id = main.pass_from

    LEFT JOIN Teams AS sub_to
        ON sub_to.player_id = main.pass_to
)
SELECT
    team_name,
    half_number,
    SUM(our_bool) AS dominance
FROM sub
GROUP BY team_name, half_number
ORDER BY team_name ASC, half_number ASC;