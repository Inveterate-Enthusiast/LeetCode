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
--Table: Passes
--
--+-------------+---------+
--| Column Name | Type    |
--+-------------+---------+
--| pass_from   | int     |
--| time_stamp  | varchar |
--| pass_to     | int     |
--+-------------+---------+
--(pass_from, time_stamp) is the unique key for this table.
--pass_from is a foreign key to player_id from Teams table.
--Each row represents a pass made during a match, time_stamp represents the time in minutes (00:00-90:00) when the pass was made,
--pass_to is the player_id of the player receiving the pass.
--Write a solution to find the longest successful pass streak for each team during the match. The rules are as follows:
--
--A successful pass streak is defined as consecutive passes where:
--Both the pass_from and pass_to players belong to the same team
--A streak breaks when either:
--The pass is intercepted (received by a player from the opposing team)
--Return the result table ordered by team_name in ascending order.
--
--
--
--1.
WITH merged AS (
    SELECT
        sub1.team_name AS team_from,
        sub2.team_name AS team_to,
        main.time_stamp,
        (CASE WHEN sub1.team_name = sub2.team_name THEN 0 ELSE 1 END) AS our_bool
    FROM Passes AS main

    LEFT JOIN Teams AS sub1
        ON sub1.player_id = main.pass_from

    LEFT JOIN Teams AS sub2
        ON sub2.player_id = main.pass_to
),
our_window AS (
    SELECT
        *,
        SUM(our_bool) OVER(PARTITION BY team_from ORDER BY time_stamp ASC) AS groups
    FROM merged
),
with_count AS (
    SELECT
        *,
        COUNT(*) OVER(PARTITION BY team_from, team_to, groups) AS longest_streak
    FROM our_window
)
SELECT
    team_from AS team_name,
    MAX(longest_streak) AS longest_streak
FROM with_count

WHERE team_from = team_to
GROUP BY team_from
ORDER BY team_from ASC;